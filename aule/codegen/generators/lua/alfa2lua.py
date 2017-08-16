# Types
from typing import List
from aule.generated import alfaAST


class LegacyGenerator(object):

    LibrariesFunctions = [
        "test",
        "subseteq",
        "issubseteq",
        "iselement",
        "isany"
    ]

    def __init__(self) -> None:
        self.space = " "
        self.newline = "\n"
        self.indent = "    "
        self.rule_name = "rule_"
        # Rules belong to a policy scope.
        self.policy_rules: List[str] = []
        self.policies: List[str] = []
        self.namespaces_stack: List[str] = []
        self.is_main_specified = False
        self.main_name = ""
        self.next = 0
        # Stack to track parent node.
        self.stack: List[str] = []
        self.accessed_attributes: List[str] = []
        self.callee_functions: List[str] = []

    def reset(self):
        self.policy_rules = []
        self.policies = []
        self.namespaces_stack = []
        self.is_main_specified = False
        self.main_name = ""
        self.next = 0
        self.stack = []
        self.accessed_attributes = []
        self.callee_functions = []

    def Property(self, node):
        return node.property

    def ApplyStatement(self, node) -> str:
        return node.value

    def ArrayExpression(self, node) -> str:
        s = ("," + self.space).join(
            element.value for element in node.elements
        )
        return s.join("{}")

    def resolveAttributeName(self, node) -> str:
        if isinstance(node, alfaAST.Identifier):
            return node.name
        else:
            return self.resolveAttributeName(node.expression) + "." + node.name

    def AnyExpression(self, node) -> str:
        return self.internal("isany") + "(" \
               + self.generateCode(node.left) + ", " \
               + self.generateCode(node.right) \
               + ")"

    def AttributeAccessExpression(self, node) -> str:
        name = "ctx." + self.resolveAttributeName(node)
        self.accessed_attributes.append(name)
        return name

    def BinaryExpression(self, node) -> str:
        if node.operator == "in":
            return self.internal("iselement") + "(" \
                   + self.generateCode(node.right) + ", " \
                   + self.generateCode(node.left) \
                   + ")"
        elif node.operator == "subset":
            return self.internal("subset") + "(" \
                   + self.generateCode(node.right) + ", " \
                   + self.generateCode(node.left) \
                   + ")"
        elif node.operator == "subseteq":
            return self.internal("subseteq") + "(" \
                   + self.generateCode(node.right) + ", " \
                   + self.generateCode(node.left) \
                   + ")"
        elif node.operator == "!=":
            operator = "~="
        elif node.operator in ["==", ">", "<", ">=", "<="]:
            operator = node.operator
        else:
            raise ValueError("Unsupported operator in Binary Expression")
        return self.generateCode(node.left) \
               + self.space + operator \
               + self.space + self.generateCode(node.right)

    def CallExpression(self, node) -> str:
        name = "handlers:" + node.callee + "(ctx)"
        self.callee_functions.append("handlers." + node.callee)
        return name

    def ConditionStatement(self, node) -> str:
        expr = self.generateCode(node)
        return "(" + self.space + expr + self.space + ")"

    def LiteralBoolean(self, node) -> str:
        return node.value

    def LiteralNumeric(self, node) -> str:
        return str(node.value)

    def LiteralString(self, node) -> str:
        return node.value

    def LogicalExpression(self, node) -> str:
        operator = node.operator.lower()
        if operator in ["or", "and"]:
            return self.generateCode(node.left) \
                   + self.space + operator \
                   + self.space + self.generateCode(node.right)
        else:
            raise ValueError("Unsupported operator in Logical Expression")

    def Identifier(self, node) -> str:
        name = "ctx." + node.name
        self.accessed_attributes.append(name)
        return name

    def NameSpaceDeclaration(self, node):
        result = []
        self.namespaces_stack.append(node.name)
        self.stack.append("NameSpaceDeclaration")

        name = node.name
        result.append("-- " + name + " namespace begin")
        result.append(self.generateTableDeclaration(name))
        result.append("local " + self.internal(name) + " = function(" + name + ")")

        for stmt in node.body:
            fragment = [self.generateCode(stmt)]
            result.extend(fragment)

        self.namespaces_stack.pop()
        self.stack.pop()
        result.append(self.generateFunctionEnd())

        # Invoke function.
        result.append(self.internal(name) + "(" + name + ")")
        result.append("-- " + name + " namespace end")
        return result

    def PolicySetDeclaration(self, node):
        # Clone references list from node.
        self.policies = list(node.references)

        # PolicySet name.
        name = node.name
        namespace = self.namespaces_stack[-1]
        is_main = False
        result = ["-- " + name + " policy set begin"]

        if name.lower().startswith("main") or name.lower().endswith("main"):
            if self.is_main_specified:
                raise ValueError(namespace + "." + name
                                 + ": Only one policy or policy set can be main.")
            if not self.isexported(node):
                raise ValueError(namespace + "." + name
                                 + ": Main policy or policy set should be exported.")
            self.is_main_specified = True
            is_main = True

        if self.stack[-1] == "NameSpaceDeclaration":
            if self.isexported(node):
                name = namespace + "." + name
                result.append(self.generateFunctionDeclaration(name))
            else:
                result.append(self.generateFunctionDeclaration(name, is_local=True))
        else:
            result.append(self.generateFunctionDeclaration(name, is_local=True))

        if is_main:
            self.main_name = name

        # Target.
        if node.targetStatement:
            result.append(self.generateTarget(node.targetStatement))

        # Condition.
        if node.conditionStatement:
            result.append(self.generateCondition(node.conditionStatement))

        self.stack.append("PolicySet")

        # Policies.
        for policy in node.policies:
            fragment = [self.generateCode(policy)]
            result.extend(fragment)

        # Policy Sets.
        for policyset in node.policysets:
            fragment = [self.generateCode(policyset)]
            result.extend(fragment)

        result.append(self.generatePolicyEngine(self.generateCode(node.algorithm)))

        # End.
        self.stack.pop()
        result.append(self.generateFunctionEnd())
        result.append("-- " + name + " policy set end")
        result.append("")

        return result

    def PolicyDeclaration(self, node):
        self.policy_rules = []

        # Policy name from ALFA code or generated.
        name = node.name
        namespace = self.namespaces_stack[-1]
        is_main = False
        result = ["-- " + name + " policy begin"]

        if name.lower().startswith("main") or name.lower().endswith("main"):
            if self.is_main_specified:
                raise ValueError(namespace + "." + name
                                 + ": Only one policy or policy set can be main.")
            if not self.isexported(node):
                raise ValueError(namespace + "." + name
                                 + ": Main policy or policy set should be exported.")
            self.is_main_specified = True
            is_main = True

        if self.stack[-1] == "NameSpaceDeclaration":
            if self.isexported(node):
                name = namespace + "." + name
                result.append(self.generateFunctionDeclaration(name))

            else:
                result.append(self.generateFunctionDeclaration(name, is_local=True))
        else:
            result.append(self.generateFunctionDeclaration(name, is_local=True))

        if is_main:
            self.main_name = name

        # Append policy name to policies list.
        self.policies.append(name)

        # Target.
        if node.targetStatement:
            result.append(self.generateTarget(node.targetStatement))

        # Condition.
        if node.conditionStatement:
            result.append(self.generateCondition(node.conditionStatement))

        self.stack.append("Policy")

        # Body.
        for rule in node.rules:
            fragment = [self.generateCode(rule)]
            result.extend(fragment)

        # Rules.
        result.append(self.generateRuleEngine(self.generateCode(node.algorithm)))

        # End.
        self.stack.pop()
        result.append(self.generateFunctionEnd())
        result.append("-- " + name + " policy end")
        result.append("")
        return result

    def RuleDeclaration(self, node):
        self.accessed_attributes = []
        self.callee_functions = []
        result = []

        if node.name and node.name in self.policy_rules:
            raise (ValueError, "Several rules with the same name in a policy")

        name = self.generateFunctionName(node.name)
        self.policy_rules.append(name)

        result.append("")
        result.append("-- " + name + " rule begin")
        result.append("local" + self.space + self.generateFunctionDeclaration(name))

        if node.targetStatement:
            target = self.TargetStatement(node.targetStatement)
            attributes = set(self.accessed_attributes)
            attributes_if_stmt = self.generateAttributesCheck(attributes)
            target_stmt = [
                "if" + self.space + target + self.space + "then",
                ["return actions." + self.ApplyStatement(node.effect)],
                "end",
                "return actions.notapplicable"
            ]
            if attributes_if_stmt:
                result.append(attributes_if_stmt)
            result.append(target_stmt)

        if node.conditionStatement:
            condition = self.ConditionStatement(node.conditionStatement)
            attributes = set(self.accessed_attributes)
            functions = set(self.callee_functions)
            functions_if_stmt = self.generateFunctionsCheck(functions)
            attributes_if_stmt = self.generateAttributesCheck(attributes)
            condition_stmt = [
                "if" + self.space + condition + self.space + "then",
                ["return actions." + self.ApplyStatement(node.effect)],
                "end",
                "return actions.notapplicable"
            ]
            if functions_if_stmt:
                result.append(functions_if_stmt)
            if attributes_if_stmt:
                result.append(attributes_if_stmt)
            result.append(condition_stmt)

        self.accessed_attributes = []
        self.callee_functions = []

        result.append(self.generateFunctionEnd()),
        result.append("-- " + name + " rule end")
        result.append("")

        return result

    def Script(self, node):
        result = []
        for item in node.body:
            result.extend(self.generateCode(item))
        return result

    def TargetStatement(self, node):
        result = (self.space + "or" + self.space).join(
            "(" + self.space + self.generateCode(clause) + self.space + ")"
            for clause in node.clauses
        )
        return result

    def TargetClause(self, node):
        result = ""
        if isinstance(node, alfaAST.BinaryExpression):
            result += self.BinaryExpression(node)
        if isinstance(node, alfaAST.LogicalExpression):
            result += self.LogicalExpression(node)

        return result

    def internal(self, name) -> str:
        """
        Wraps an input name using special pattern.
        Example: in -> __in()
        """
        return "__" + name

    def isexported(self, node) -> bool:
        for item in node.modifiers:
            if item.text == "export":
                return True
        return False

    def generateFunctionParams(self) -> str:
        return "(ctx, actions, handlers)"

    def next_num(self) -> int:
        self.next += 1
        return self.next

    def generateFunctionName(self, name) -> str:
        # Generate name if a processed rule name is undefined.
        name = str(name) or (self.rule_name + str(self.next_num()))
        return name

    def generateFunctionDeclaration(self, name, is_local=False) -> str:
        name = self.generateFunctionName(name)
        local = "local " if is_local else ""
        return local + "function" + self.space + name + self.generateFunctionParams()

    def generateFunctionEnd(self) -> str:
        return "end"

    def generateTableDeclaration(self, name) -> str:
        return "local" + self.space + name + self.space + "= {}"

    def generateFunctionsCheck(self, functions):
        if not functions:
            return None
        test = (self.space + "or" + self.space).join(
            "not " + func for func in functions
        )
        return [
            "if" + self.space + test + self.space + "then",
                ["return actions.indeterminate"],
            "end"
        ]

    def generateAttributesCheck(self, attributes):
        if not attributes:
            return None
        test = (self.space + "or" + self.space).join(
            "not " + attr for attr in attributes
        )
        return [
            "if" + self.space + test + self.space + "then",
                ["return actions.indeterminate"],
            "end"
        ]

    def generateTarget(self, node):
        self.accessed_attributes = []
        target = self.TargetStatement(node)
        attributes = set(self.accessed_attributes)

        result = [
            "-- target begin"]
        result.extend(self.generateAttributesCheck(attributes))
        result.extend([
            "if" + self.space + "not" + self.space + target + self.space + "then",
                ["return actions.notapplicable"],
            "end",
            "-- target end",
        ])

        self.accessed_attributes = []
        return result

    def generateCondition(self, node):
        self.callee_functions = []
        condition = self.ConditionStatement(node)
        functions = set(self.callee_functions)

        result = [
            "-- condition begin"]
        result.extend(self.generateFunctionsCheck(functions))
        result.extend([
            "if" + self.space + "not" + self.space + condition + self.space + "then",
                ["return actions.notapplicable"],
            "end",
            "-- condition end",
        ])

        self.callee_functions = []
        return result

    def generatePolicyEngine(self, algorithm):
        # XACML-3.0. Appendix C. Combining algorithms (normative)
        # http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html#_Toc325047268                
        # Indeterminate result is not supported.

        algorithm = algorithm.lower()
        result = []
        result.append("")
        result.append("-- " + algorithm + " policy-combining algorithm begin")

        if algorithm == "permitoverrides":
            result.append("local atLeastOneError = false")
            result.append("local atLeastOneDeny = false")
        elif algorithm == "denyoverrides":
            result.append("local atLeastOneError = false")
            result.append("local atLeastOnePermit = false")
        elif algorithm == "onlyoneapplicable":
            result.append("local atLeastOne = false")
            result.append("local result = nil")

        policies = "{" + self.space
        policies += ("," + self.space).join(
            "p" + str(i) + self.space + "=" + self.space + policy
            for i, policy in enumerate(self.policies)
        )
        policies += self.space + "}"
        result.append("local policies = " + policies)
        result.append("for _, policy in pairs(policies) do")
        result.append(["local decision = policy(ctx, actions, handlers)"])

        if algorithm == "firstapplicable":
            result.append(["if decision == actions.deny then", ["return actions.deny"], "end"])
            result.append(["if decision == actions.permit then", ["return actions.permit"], "end"])
            result.append(["if decision == actions.notapplicable then", "end"])
            result.append(["if decision == actions.indeterminate then", ["return actions.indeterminate"], "end"])
        elif algorithm == "permitoverrides":
            result.append(["if decision == actions.permit then", ["return actions.permit"], "end"])
            result.append(["if decision == actions.deny then", ["atLeastOneDeny = true"], "end"])
            result.append(["if decision == actions.indeterminate then", ["atLeastOneError = true"], "end"])
        elif algorithm == "denyoverrides":
            result.append(["if decision == actions.deny then", ["return actions.deny"], "end"])
            result.append(["if decision == actions.permit then", ["atLeastOnePermit = true"], "end"])
            result.append(["if decision == actions.indeterminate then", ["atLeastOneError = true"], "end"])
        elif algorithm == "denyunlesspermit":
            result.append(["if decision == actions.permit then", ["return actions.permit"], "end"])
        elif algorithm == "permitunlessdeny":
            result.append(["if decision == actions.deny then", ["return actions.deny"], "end"])
        elif algorithm == "onlyoneapplicable":
            result.append(
                [
                    "if decision == actions.indeterminate then",
                        ["return actions.indeterminate"],
                    "end",
                    "if decision == actions.deny or decision == actions.permit then",
                        ["if atLeastOne == true then",
                            ["return actions.indeterminate"],
                        "else",
                            ["atLeastOne = true; result = decision"],
                        "end"],
                    "end",
                    "if decision == actions.notapplicable then",
                    "end",
                    "if atLeastOne == true then",
                        ["return result"],
                    "else",
                        ["return actions.notappicable"],
                    "end"
                ])
        else:
            raise ValueError("Unknown policy-combining algorithm type")
        result.append("end")

        if algorithm == "firstapplicable":
            result.append("return actions.notapplicable")
        elif algorithm == "permitoverrides":
            result.append("if atLeastOneError == true then")
            result.append(["return actions.indeterminate"])
            result.append("end")
            result.append("if atLeastOneDeny == true then")
            result.append(["return actions.deny"])
            result.append("end")
            result.append("return actions.notapplicable")
        elif algorithm == "denyoverrides":
            result.append("if atLeastOneError == true then")
            result.append(["return actions.indeterminate"])
            result.append("end")
            result.append("if atLeastOnePermit == true then")
            result.append(["return actions.permit"])
            result.append("end")
            result.append("return actions.notapplicable")
        elif algorithm == "denyunlesspermit":
            result.append("return actions.deny")
        elif algorithm == "permitunlessdeny":
            result.append("return actions.permit")
        elif algorithm == "onlyoneapplicable":
            result.append("if atLeastOne == true then"),
            result.append(["return result"])
            result.append("else")
            result.append(["return actions.notappicable"])
            result.append("end")

        result.append("-- " + algorithm + " policy-combining algorithm end")
        result.append("")

        return result

    def generateRuleEngine(self, algorithm):
        # XACML-3.0. Appendix C. Combining algorithms (normative)
        # http://docs.oasis-open.org/xacml/3.0/xacml-3.0-core-spec-os-en.html#_Toc325047268                
        # Indeterminate result is not supported.

        algorithm = algorithm.lower()
        result = []
        result.append("")
        result.append("-- " + algorithm + " rule-combining algorithm begin")

        if algorithm == "permitoverrides":
            result.append("local atLeastOneError = false")
            result.append("local atLeastOneDeny = false")
        elif algorithm == "denyoverrides":
            result.append("local atLeastOneError = false")
            result.append("local atLeastOnePermit = false")

        rules = "{" + self.space
        rules += ("," + self.space).join(
            "r" + str(i) + self.space + "=" + self.space + policy
            for i, policy in enumerate(self.policy_rules)
        )
        rules += self.space + "}"

        result.append("local rules = " + rules)
        result.append("for _, rule in pairs(rules) do")
        result.append(["local decision = rule(ctx, actions, handlers)"])

        if algorithm == "firstapplicable":
            result.append(["if decision == actions.deny then", [" return actions.deny"], "end"])
            result.append(["if decision == actions.permit then", ["return actions.permit"], "end"])
            result.append(["if decision == actions.notapplicable then", "end"])
            result.append(["if decision == actions.indeterminate then", ["return actions.indeterminate"], "end"])
        elif algorithm == "permitoverrides":
            result.append(["if decision == actions.permit then", ["return actions.permit"], "end"])
            result.append(["if decision == actions.deny then", ["atLeastOneDeny = true"], "end"])
            result.append(["if decision == actions.indeterminate then", ["atLeastOneError = true"], "end"])
        elif algorithm == "denyoverrides":
            result.append(["if decision == actions.deny then", ["return actions.deny"], "end"])
            result.append(["if decision == actions.permit then", ["atLeastOnePermit = true"], "end"])
            result.append(["if decision == actions.indeterminate then", ["atLeastOneError = true"], "end"])
        elif algorithm == "denyunlesspermit":
            result.append(["if decision == actions.permit then", ["return actions.permit"], "end"])
        elif algorithm == "permitunlessdeny":
            result.append(["if decision == actions.deny then", ["return actions.deny"], "end"])
        else:
            raise ValueError("Unknown rule-combining algorithm type")
        result.append("end")

        if algorithm == "firstapplicable":
            result.append("return actions.notapplicable")
        elif algorithm == "permitoverrides":
            result.append("if atLeastOneError == true then")
            result.append(["return actions.indeterminate"])
            result.append("end")
            result.append("if atLeastOneDeny == true then")
            result.append(["return actions.deny"])
            result.append("end")
            result.append("return actions.notapplicable")
        elif algorithm == "denyoverrides":
            result.append("if atLeastOneError == true then")
            result.append(["return actions.indeterminate"])
            result.append("end")
            result.append("if atLeastOnePermit == true then")
            result.append(["return actions.permit"])
            result.append("end")
            result.append("return actions.notapplicable")
        elif algorithm == "denyunlesspermit":
            result.append("return actions.deny")
        elif algorithm == "permitunlessdeny":
            result.append("return actions.permit")

        result.append("-- " + algorithm + " rule-combining algorithm end")
        result.append("")
        return result

    def generateLibrariesFunctions(self):
        result = []
        for name in LegacyGenerator.LibrariesFunctions:
            result.append("local"
                          + self.space + self.internal(name)
                          + self.space + "="
                          + self.space + "lib." + name)
        return self.stringify(result)

    def generateMain(self):
        # Declare main function.
        result = ["function " + self.internal("main") + self.generateFunctionParams()]
        if not self.is_main_specified or self.main_name == "":
            raise ValueError("Main policy or policy set not found.")
        result.append(["return" + self.space + self.main_name + self.generateFunctionParams()])
        result.append(self.generateFunctionEnd())
        return self.stringify(result)

    def generateCode(self, node):
        method = node.__class__.__name__
        return self.__getattribute__(method)(node)

    def flatten(self, arr, indent) -> str:
        result = ""
        for elem in arr:
            if isinstance(elem, list):
                result += self.flatten(elem, indent + self.indent)
            else:
                result += indent + str(elem) + "\n"
        return result

    def stringify(self, generated) -> str:
        if isinstance(generated, list):
            return self.flatten(generated, "")
        else:
            return generated

    def generate(self, node) -> str:
        if isinstance(node, alfaAST.Statement) or isinstance(node, alfaAST.Script):
            result = self.stringify(self.generateCode(node))
        elif isinstance(node, alfaAST.Expression):
            result = self.stringify(self.generateCode(node))
        else:
            raise ValueError("Unknown node type")
        libs = self.generateLibrariesFunctions()
        main = self.generateMain()
        return libs + "\n" + result + "\n" + main
