from aule.generated.alfaAST import *
from aule.generated.alfaParserVisitor import alfaParserVisitor


class alfaASTVisitor(alfaParserVisitor):

    def visitApplyStatement(self, ctx):
        return ApplyStatement(ctx.algorithm.text)

    def visitEffectStatement(self, ctx):
        return EffectStatement(ctx.getText())

    def visitRulelist(self, ctx):
        return self.visitChildren(ctx)

    def visitCallExpression(self, ctx):
        callee = ctx.ID().getText()
        return CallExpression(callee)

    def visitAttributeAccessExpression(self, ctx):
        if not ctx.attributeAccessExpression():
            return Identifier(ctx.ID().getText())
        return AttributeAccessExpression(self.visit(ctx.attributeAccessExpression()), ctx.ID().getText() )

    def visitAttributeValue(self, ctx):
        text = ctx.getText()
        if text.lower() == "true" or text.lower() == "false":
            return LiteralBoolean(text)
        elif text[0] == '"':
            return LiteralString(text)
        else:
            return LiteralNumeric(text)

    def visitArrayExpression(self, ctx):
        elements = []
        e = None
        i = 0
        while ctx.literal(i):
            text = str(ctx.literal(i).getText())
            if text[0] in ['"', "'"]:
                e = LiteralString(text)
            else:
                e = LiteralNumeric(text)
            elements.append(e)
            i += 1
        return ArrayExpression(elements)

    def visitBinaryOperator(self, ctx):
        return ctx.getText()

    def visitTargetStatement(self, ctx):
        clauses = []
        i = 0
        while ctx.targetExpression(i):
            clauses.append(self.visit(ctx.targetExpression(i)))
            i += 1
        
        return TargetStatement(clauses)

    def visitConditionStatement(self, ctx):
        return self.visit(ctx.conditionExpression())

    def visitTargetAndExpression(self, ctx):
        left = self.visit(ctx.targetExpression(0))
        right = self.visit(ctx.targetExpression(1))
        return LogicalExpression("AND", left, right)

    def visitTargetOrExpression(self, ctx):
        left = self.visit(ctx.targetExpression(0))
        right = self.visit(ctx.targetExpression(1))
        return LogicalExpression("OR", left, right)

    def visitTargetBaseExpression(self, ctx):
        left = self.visit(ctx.targetExpression(0))
        right = self.visit(ctx.targetExpression(1))
        operator = self.visit(ctx.binaryOperator())
        return BinaryExpression(operator, left, right)

    def visitTargetAnyExpression(self, ctx):
        left = self.visit(ctx.children[0].children[1])
        right = self.visit(ctx.children[0].children[3])
        return AnyExpression(left, right)

    def visitTargetArrayExpression(self, ctx):
        return self.visit(ctx.arrayExpression())

    def visitTargetAtributeAccessExpression(self, ctx):
        return self.visit(ctx.attributeAccessExpression())

    def visitTargetAtributeValueExpression(self, ctx):
        return self.visit(ctx.attributeValue())

    def visitConditionAndExpression(self, ctx):
        left = self.visit(ctx.conditionExpression(0))
        right = self.visit(ctx.conditionExpression(1))
        return LogicalExpression("AND", left, right)

    def visitConditionOrExpression(self, ctx):
        left = self.visit(ctx.conditionExpression(0))
        right = self.visit(ctx.conditionExpression(1))
        return LogicalExpression("OR", left, right)

    def visitConditionBaseExpression(self, ctx):
        left = self.visit(ctx.conditionExpression(0))
        right = self.visit(ctx.conditionExpression(1))
        operator = self.visit(ctx.binaryOperator())
        return BinaryExpression(operator, left, right)

    def visitConditionCallExpression(self, ctx):
        return self.visit(ctx.callExpression())

    def visitConditionArrayExpression(self, ctx):
        return self.visit(ctx.arrayExpression())

    def visitConditionAtributeAccessExpression(self, ctx):
        return self.visit(ctx.attributeExpression())

    def visitConditionAtributeValueExpression(self, ctx):
        return self.visit(ctx.attributeValue())

    def visitEvent(self, ctx):
        body = []
        if ctx.PERMIT():
            type_ = "permit"
        elif ctx.DENY():
            type_ = "deny"
        else:
            raise ValueError("Unknown event type")
        i = 0
        while ctx.eventBody(i):
            body.append(self.visit(ctx.eventBody(i)))
            i += 1
        return Event(type_, body)

    def visitEventBody(self, ctx):
        if ctx.obligation():
            return self.visit(ctx.obligation())
        elif ctx.advice():
            return self.visit(ctx.advice())

    def visitObligation(self, ctx):
        if ctx.ID():
            return str(ctx.ID().getText())
    
    def visitAdvice(self, ctx):        
        if ctx.ID():
            return str(ctx.ID().getText())

    def visitRuleDeclaration(self, ctx):
        rule_id = None
        targetStatement = None
        conditionStatement = None
        events = []

        if ctx.ruleId:
            rule_id = ctx.ruleId.text

        effect = self.visit(ctx.effectStatement())

        if ctx.targetStatement():
            targetStatement = self.visit(ctx.targetStatement())

        if ctx.conditionStatement():
            conditionStatement = self.visit(ctx.conditionStatement())

        i = 0        
        while ctx.event(i):
            event = self.visit(ctx.event(i))
            events.append(event)
            i += 1

        return RuleDeclaration(rule_id, effect, targetStatement, conditionStatement, events)

    def visitPolicySetBody(self, ctx):
        if ctx.ID():
            return str(ctx.ID().getText())
        if ctx.policySetDeclaration():
            return self.visit(ctx.policySetDeclaration())
        if ctx.policyDeclaration():
            return self.visit(ctx.policyDeclaration())
    
    def visitPolicySetDeclaration(self, ctx):
        name = None
        targetStatement = None
        conditionStatement = None
        references = []
        policies = []
        policysets = []
        modifiers = []
        events = []

        if ctx.EXPORT():
            modifiers.append(ExportKeyword("export"))

        if ctx.policySetId:
            name = ctx.policySetId.text

        algorithm = self.visit(ctx.applyStatement())
        
        if ctx.targetStatement():
            targetStatement = self.visit(ctx.targetStatement())

        if ctx.conditionStatement():
            conditionStatement = self.visit(ctx.conditionStatement())
        
        i = 0
        while ctx.policySetBody(i):
            result = self.visit(ctx.policySetBody(i))
            if type(result) == str:
                references.append(result)
            elif isinstance(result, PolicyDeclaration):
                policies.append(result)
            elif isinstance(result, PolicySetDeclaration):
                policysets.append(result)
            else:
                raise ValueError("Unknown node type")
            i += 1

        i = 0        
        while ctx.event(i):
            event = self.visit(ctx.event(i))
            events.append(event)
            i += 1

        node = PolicySetDeclaration(name, algorithm, targetStatement, conditionStatement, references, policies, policysets, events, modifiers)
        return node

    def visitPolicyDeclaration(self, ctx):
        name = None
        targetStatement = None
        conditionStatement = None
        rules = []
        modifiers = []
        events = []

        if ctx.EXPORT():
            modifiers.append(ExportKeyword("export"))

        if ctx.policyId:
            name = ctx.policyId.text

        algorithm = self.visit(ctx.applyStatement())
        
        if ctx.targetStatement():
            targetStatement = self.visit(ctx.targetStatement())

        if ctx.conditionStatement():
            conditionStatement = self.visit(ctx.conditionStatement())
        
        i = 0
        while ctx.ruleDeclaration(i):
            rules.append(self.visit(ctx.ruleDeclaration(i)))
            i += 1

        i = 0        
        while ctx.event(i):
            event = self.visit(ctx.event(i))
            events.append(event)
            i += 1
        
        node = PolicyDeclaration(name, algorithm, targetStatement, conditionStatement, rules, events, modifiers)
        return node

    def visitNameSpaceBody(self, ctx):
        if ctx.policyDeclaration():
            return self.visit(ctx.policyDeclaration())
        if ctx.policySetDeclaration():
            return self.visit(ctx.policySetDeclaration())
        if ctx.nameSpaceDeclaration():
            return self.visit(ctx.nameSpaceDeclaration())

    def visitNameSpaceDeclaration(self, ctx):
        name = ctx.ID().getText()
        body = []
        i = 0
        while ctx.nameSpaceBody(i):
            body.append(self.visit(ctx.nameSpaceBody(i)))
            i += 1
        return NameSpaceDeclaration(name, body)

    def visitRoot(self, ctx):
        body = []
        i = 0
        while ctx.nameSpaceDeclaration(i):
            body.append(self.visit(ctx.nameSpaceDeclaration(i)))
            i += 1
        return Script(body)
