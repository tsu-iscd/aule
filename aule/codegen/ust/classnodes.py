from .simplenodes import *
from typing import List


class FieldTag(object):
    def __init__(self,
                 name: Identifier,
                 value: str) -> None:
        """
        :type name: Identifier
        :type value: str
        """
        self.node = "FieldDeclaration"
        self.name = name
        self.value = value

    def __repr__(self):
        return "<Tag {0.name}: {0.value}>".format(self)


class FieldDeclaration(VariableDeclaration):
    def __init__(self,
                 name: Identifier,
                 type: TypeReference,
                 modifiers: List[Modifier] = None,
                 tags: List[FieldTag] = None,
                 default: Any = None) -> None:
        """
        :type name: Identifier
        :type type: TypeReference
        :type modifiers: list[Modifier]
        :type tags: list[FieldTag]
        :type default: any
        """
        super(FieldDeclaration, self).__init__(name, type)
        self.node = "FieldDeclaration"
        self.modifiers = modifiers or []
        self.tags = tags or []
        self.default = default

    def __repr__(self):
        return "<Field {0.modifiers} {0.name}: {0.type} = {0.default} `{0.tags}`>".format(self)


class MethodDeclaration(FunctionDeclaration):
    def __init__(self,
                 name: Identifier,
                 arguments: List[Argument],
                 returns: List[TypeReference],
                 body: Union[Block, List[Any]],
                 modifiers: List[Modifier] = None) -> None:
        """
        :type name: Identifier
        :type arguments: list[Argument]
        :type returns: list[TypeReference]
        :type body: Block
        :type modifiers: list[Modifier]
        """
        super(MethodDeclaration, self).__init__(name, arguments, returns, body)
        self.node = "MethodDeclaration"
        self.modifiers = modifiers or []

    def __repr__(self):
        return "<Method {0.modifiers} {0.name}({0.arguments}) {0.returns}>".format(self)


class Constructor(MethodDeclaration):
    def __init__(self,
                 name: Identifier,
                 arguments: List[Argument],
                 returns: List[TypeReference],
                 body: Union[Block, List[Any]] = None,
                 modifiers: List[Modifier] = None) -> None:
        """
        :type name: Identifier
        :type arguments: list[Argument1]
        :type returns: list[TypeReference]
        :type body: Block
        :type modifiers: list[Modifier]
        """
        body = body or Block([])
        super(Constructor, self).__init__(name, arguments, returns, body, modifiers)
        self.node = "Constructor"

    def __repr__(self):
        return "<Constructor {}>".format(super(Constructor, self).__repr__())


class ClassDeclaration(object):
    def __init__(self,
                 name: Identifier,
                 parents: List[Identifier] = None,
                 fields: List[FieldDeclaration] = None,
                 methods: List[MethodDeclaration] = None,
                 constructor: Constructor = None,
                 modifiers: List[Modifier] = None) -> None:
        """
        :type name: Identifier
        :type parents: list[Identifier]
        :type constructor: Constructor
        :type fields: list[FieldDeclaration]
        :type methods: list[MethodDeclaration]
        :type modifiers: list[Modifier]
        """
        self.node = "ClassDeclaration"
        self.name = name
        self.modifiers = modifiers or []
        self.parents = parents or []
        self.fields = fields or []
        self.methods = methods or []
        self.constructor = constructor or self._create_constructor()

    def _create_constructor(self) -> Constructor:
        return Constructor(
            name=Identifier("{}Constructor".format(self.name)),
            arguments=[
                Argument(f.name, f.type)
                for f in self.fields
                if f.default is None and Modifier.ABSTRACT not in f.modifiers
            ],
            returns=[TypeReference(self.name)],
        )

    def __repr__(self):
        return "<Class {0.modifiers} {0.name}: extends {0.parents}>".format(self)
