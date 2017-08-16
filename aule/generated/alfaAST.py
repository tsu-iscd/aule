
class Pickler(object):
    def __init__(*args, **kwargs):
        # We have it for compatibility reasons (all node classes has same
        # init signature)
        pass

    @classmethod
    def get_mangled(cls):
        mangled_names = {}
        for c in cls.mro():
            mangled_names.update(getattr(c, "__mangled__", {}).items())
        return mangled_names

    @classmethod
    def mangle_dict(cls, obj):
        # mangle_map is map form normal name to python mangled one.
        mangle_map = cls.get_mangled()
        for k, v in obj.items():
            if k in mangle_map:
                del obj[k]
                obj[mangle_map[k]] = v

    def __getstate__(self):
        # mangled_names is a map from python name to unmangled one.
        mangled_names = {k: v for v, k in self.get_mangled().items()}
        to_pickle = {}
        for k, v in self.__dict__.items():
            to_pickle[mangled_names.get(k,k)] = v
        return {"type": self.__class__.__name__, **to_pickle}


class Node(Pickler):
    def __init__(self, *args, **kwargs):
        super(Node, self).__init__(*args, **kwargs)    
        pass
    
    __mangled__ = {}

class Statement(Node,Pickler):
    def __init__(self, *args, **kwargs):
        super(Statement, self).__init__(*args, **kwargs)    
        pass
    
    __mangled__ = {}

class Expression(Node,Pickler):
    def __init__(self, *args, **kwargs):
        super(Expression, self).__init__(*args, **kwargs)    
        pass
    
    __mangled__ = {}

class Script(Statement,Pickler):
    def __init__(self, body=None, *args, **kwargs):
        super(Script, self).__init__(*args, **kwargs)
        self.body = body    
    
    __mangled__ = {}

class NameSpaceDeclaration(Statement,Pickler):
    def __init__(self, name=None, body=None, *args, **kwargs):
        super(NameSpaceDeclaration, self).__init__(*args, **kwargs)
        self.name = name
        self.body = body    
    
    __mangled__ = {}

class PolicySetDeclaration(Statement,Pickler):
    def __init__(self, name=None, algorithm=None, targetStatement=None, conditionStatement=None, references=None, policies=None, policysets=None, events=None, modifiers=None, *args, **kwargs):
        super(PolicySetDeclaration, self).__init__(*args, **kwargs)
        self.name = name
        self.algorithm = algorithm
        self.targetStatement = targetStatement
        self.conditionStatement = conditionStatement
        self.references = references
        self.policies = policies
        self.policysets = policysets
        self.events = events
        self.modifiers = modifiers    
    
    __mangled__ = {}

class PolicyDeclaration(Statement,Pickler):
    def __init__(self, name=None, algorithm=None, targetStatement=None, conditionStatement=None, rules=None, events=None, modifiers=None, *args, **kwargs):
        super(PolicyDeclaration, self).__init__(*args, **kwargs)
        self.name = name
        self.algorithm = algorithm
        self.targetStatement = targetStatement
        self.conditionStatement = conditionStatement
        self.rules = rules
        self.events = events
        self.modifiers = modifiers    
    
    __mangled__ = {}

class RuleDeclaration(Statement,Pickler):
    def __init__(self, name=None, effect=None, targetStatement=None, conditionStatement=None, events=None, *args, **kwargs):
        super(RuleDeclaration, self).__init__(*args, **kwargs)
        self.name = name
        self.effect = effect
        self.targetStatement = targetStatement
        self.conditionStatement = conditionStatement
        self.events = events    
    
    __mangled__ = {}

class Event(Statement,Pickler):
    def __init__(self, eventType=None, body=None, *args, **kwargs):
        super(Event, self).__init__(*args, **kwargs)
        self.eventType = eventType
        self.body = body    
    
    __mangled__ = {}

class Obligation(Statement,Pickler):
    def __init__(self, name=None, *args, **kwargs):
        super(Obligation, self).__init__(*args, **kwargs)
        self.name = name    
    
    __mangled__ = {}

class Advice(Statement,Pickler):
    def __init__(self, name=None, *args, **kwargs):
        super(Advice, self).__init__(*args, **kwargs)
        self.name = name    
    
    __mangled__ = {}

class ApplyStatement(Statement,Pickler):
    def __init__(self, value=None, *args, **kwargs):
        super(ApplyStatement, self).__init__(*args, **kwargs)
        self.value = value    
    
    __mangled__ = {}

class EffectStatement(Statement,Pickler):
    def __init__(self, value=None, *args, **kwargs):
        super(EffectStatement, self).__init__(*args, **kwargs)
        self.value = value    
    
    __mangled__ = {}

class TargetStatement(Statement,Pickler):
    def __init__(self, clauses=None, *args, **kwargs):
        super(TargetStatement, self).__init__(*args, **kwargs)
        self.clauses = clauses    
    
    __mangled__ = {}

class ConditionStatement(Statement,Pickler):
    def __init__(self, statement=None, *args, **kwargs):
        super(ConditionStatement, self).__init__(*args, **kwargs)
        self.statement = statement    
    
    __mangled__ = {}

class TargetClause(Statement,Pickler):
    def __init__(self, statement=None, *args, **kwargs):
        super(TargetClause, self).__init__(*args, **kwargs)
        self.statement = statement    
    
    __mangled__ = {}

class AttributeAccessExpression(Expression,Pickler):
    def __init__(self, expression=None, name=None, *args, **kwargs):
        super(AttributeAccessExpression, self).__init__(*args, **kwargs)
        self.expression = expression
        self.name = name    
    
    __mangled__ = {}

class CallExpression(Expression,Pickler):
    def __init__(self, callee=None, arguments=None, *args, **kwargs):
        super(CallExpression, self).__init__(*args, **kwargs)
        self.callee = callee
        self.arguments = arguments    
    
    __mangled__ = {}

class AnyExpression(Expression,Pickler):
    def __init__(self, left=None, right=None, *args, **kwargs):
        super(AnyExpression, self).__init__(*args, **kwargs)
        self.left = left
        self.right = right    
    
    __mangled__ = {}

class ArrayExpression(Expression,Pickler):
    def __init__(self, elements=None, *args, **kwargs):
        super(ArrayExpression, self).__init__(*args, **kwargs)
        self.elements = elements    
    
    __mangled__ = {}

class Identifier(Expression,Pickler):
    def __init__(self, name=None, *args, **kwargs):
        super(Identifier, self).__init__(*args, **kwargs)
        self.name = name    
    
    __mangled__ = {}

class LiteralString(Expression,Pickler):
    def __init__(self, value=None, *args, **kwargs):
        super(LiteralString, self).__init__(*args, **kwargs)
        self.value = value    
    
    __mangled__ = {}

class LiteralNumeric(Expression,Pickler):
    def __init__(self, value=None, *args, **kwargs):
        super(LiteralNumeric, self).__init__(*args, **kwargs)
        self.value = value    
    
    __mangled__ = {}

class LiteralBoolean(Expression,Pickler):
    def __init__(self, value=None, *args, **kwargs):
        super(LiteralBoolean, self).__init__(*args, **kwargs)
        self.value = value    
    
    __mangled__ = {}

class BinaryExpression(Expression,Pickler):
    def __init__(self, operator=None, left=None, right=None, *args, **kwargs):
        super(BinaryExpression, self).__init__(*args, **kwargs)
        self.operator = operator
        self.left = left
        self.right = right    
    
    __mangled__ = {}

class LogicalExpression(Expression,Pickler):
    def __init__(self, operator=None, left=None, right=None, *args, **kwargs):
        super(LogicalExpression, self).__init__(*args, **kwargs)
        self.operator = operator
        self.left = left
        self.right = right    
    
    __mangled__ = {}

class BooleanExpression(Expression,Pickler):
    def __init__(self, operator=None, left=None, right=None, *args, **kwargs):
        super(BooleanExpression, self).__init__(*args, **kwargs)
        self.operator = operator
        self.left = left
        self.right = right    
    
    __mangled__ = {}

class ExportKeyword(Node,Pickler):
    def __init__(self, text=None, *args, **kwargs):
        super(ExportKeyword, self).__init__(*args, **kwargs)
        self.text = text    
    
    __mangled__ = {}

