from typing import List, Union, Any
from .mixins import PicklableEnum


class SimpleType(PicklableEnum):
    STRING = "str"
    FLOAT = "float"
    INTEGER = "int"
    BOOLEAN = "bool"
    NULL = "null"
    VOID = "void"
    ANY = "any"

    def __repr__(self):
        return self.name


class Modifier(PicklableEnum):
    PUBLIC = "public"
    PRIVATE = "private"
    PROTECTED = "protected"
    STATIC = "static"
    ABSTRACT = "abstract"
    CONST = "const"

    def __repr__(self):
        return self.name


class Identifier(object):
    def __init__(self,
                 name: str,
                 immutable: bool = False) -> None:
        """
        :type name: str
        :type immutable: bool
        """
        self.node = "Identifier"
        self.name = name
        self.immutable = immutable

    def __str__(self):
        return self.name.__str__()

    def __repr__(self):
        return "<Identifier {}>".format(self.__str__())

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return self.__str__().__hash__()


class UnionType(object):
    def __init__(self,
                 types: List['TypeReference']) -> None:
        """
        :type types: List[TypeReference]
        """
        self.node = "UnionType"
        self.types = types

    def __repr__(self):
        return " | ".join(t.__repr__() for t in self.types)


class TypeReference(object):
    def __init__(self,
                 type_: Union[Identifier, SimpleType, UnionType],
                 is_pointer: bool = False,
                 is_sequence: bool = False) -> None:
        """
        :type type_: Identifier | SimpleType | UnionType
        :type is_pointer: bool
        :type is_sequence: bool
        """
        self.node = "TypeReference"
        self.type = type_
        self.is_pointer = is_pointer
        self.is_sequence = is_sequence

    def __eq__(self, other):
        return isinstance(other, TypeReference) and\
               self.type == other.type and \
               self.is_pointer == other.is_pointer and \
               self.is_sequence == other.is_sequence

    def __repr__(self):
        typestring = self.type.__repr__()
        if self.is_sequence:
            typestring = "[{}]".format(typestring)
        if self.is_pointer:
            typestring = "*{}".format(typestring)
        return "<Type: {}>".format(typestring)


class Block(object):
    def __init__(self,
                 body: List[Union['Block', str]]) -> None:
        """
        :type body: list[Union['Block', str]]
        """
        self.node = "Block"
        self.body = body

    def __iter__(self):
        return self.body.__iter__()

    def __repr__(self):
        return "<Block {\n%s\n}>" % (
            "\n".join(l.__repr__() for l in self.body)
        )


class VariableDeclaration(object):
    def __init__(self,
                 name: Identifier,
                 type: TypeReference) -> None:
        """
        :type name: Identifier
        :type type: TypeReference
        """
        self.node = "VariableDeclaration"
        self.name = name
        self.type = type

    def __repr__(self):
        return "<Variable {0.name}: {0.type}>".format(self)


class Argument(object):
    def __init__(self,
                 name: Identifier,
                 type: TypeReference,
                 default: Any=None) -> None:
        """
        :type name: Identifier
        :type type: TypeReference
        :type default: any
        """
        self.node = "Argument"
        self.name = name
        self.type = type
        self.default = default

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return "<Argument {0.name}: {0.type} = {0.default}>".format(self)


class FunctionDeclaration(object):
    def __init__(self,
                 name: Identifier,
                 arguments: List[Argument],
                 returns: List[TypeReference],
                 body: Union[Block, List[Any]]) -> None:
        """
        :type name: Identifier
        :type arguments: list[Argument]
        :type returns: list[TypeReference]
        :type body: Block
        """
        self.node = "FunctionDeclaration"
        self.name = name
        self.arguments = arguments
        self.returns = returns
        self.body = body

    def __eq__(self, other):
        # TODO: That's unfair cos we ignore possibility of polymorphism, but
        # now it works good enough.
        return self.name == other.name

    def __repr__(self):
        return "<Function {0.name}({0.arguments}) {0.returns}>".format(self)


class EnumMember(object):
    def __init__(self, name: Identifier, value: Any = None) -> None:
        self.node = "EnumMember"
        self.name = name
        self.value = value

    def __repr__(self):
        return "EnumMember.{0.name}({0.value})".format(self)


class EnumDeclaration(object):
    def __init__(self, name: Identifier, members: List[EnumMember]) -> None:
        self.node = "EnumDeclaration"
        self.name = name
        self.members = members

    def __repr__(self):
        return "<Enum {} [{}]>".format(
            self.name, ", ".join([m.name.__str__() for m in self.members])
        )