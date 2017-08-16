from typing import List, Union, Callable
from aule.codegen import ust


# Type shortcut.
TypedNode = Union[ust.SimpleType, ust.Identifier, ust.UnionType, ust.TypeReference]


class TypeHelpers(object):
    TYPES_MAP = {
        ust.SimpleType.INTEGER: "Int",
        ust.SimpleType.FLOAT: "Double",
        ust.SimpleType.STRING: "String",
        ust.SimpleType.BOOLEAN: "Boolean",
    }

    def __init__(self, class_reference: ust.helpers.ClassesReference) -> None:
        self.reference = class_reference
        self.name_resolver: Callable[[ust.Identifier], str] = None

    def translate_type(self, node: TypedNode) -> str:
        """ Recursively translates IDL type into Kotlin type declaration """
        if isinstance(node, ust.SimpleType) and node in self.TYPES_MAP:
            # If it's a simple type translate it via map
            return "{}".format(self.TYPES_MAP[node])
        elif isinstance(node, ust.Identifier):
            # If it's an Identifier type - just cast it to string
            return "{}".format(self._resolve_name(node.name))
        elif isinstance(node, ust.TypeReference):
            # If it's a type reference - translate it recursively and then apply
            # necessary modifiers.
            kttype = "{}".format(self.translate_type(node.type))
            if node.is_sequence:
                # Probably in most cases we want to use mutable list (i suppose)
                kttype = "MutableList<{}>".format(kttype)
            if self.is_nullable(node):
                kttype = "{}?".format(kttype)
            return kttype
        elif isinstance(node, ust.UnionType):
            # If that's is a union - look for the common ancestor
            return self.translate_type(
                self.__translate_union_type(node)
            )
        raise TypeError("Unknown node {}".format(node))

    def typed_arg(self, arg: ust.Argument) -> str:
        if arg.default is not None:
            return "{}: {} = {}".format(
                self._resolve_name(arg.name), self.translate_type(arg.type), arg.default
            )
        elif self.is_nullable(arg.type):
            return "{}: {} = null".format(
                self._resolve_name(arg.name), self.translate_type(arg.type)
            )
        return "{}: {}".format(
            self._resolve_name(arg.name), self.translate_type(arg.type)
        )

    def typed_var(self, typed: ust.FieldDeclaration) -> str:
        """ To declare variable or field we need to add var/val keyword """
        if ust.Modifier.CONST in typed.modifiers:
            return "val {}: {}".format(
                self._resolve_name(typed.name), self.translate_type(typed.type)
            )
        return "var {}: {}".format(
            self._resolve_name(typed.name), self.translate_type(typed.type)
        )

    def gen_return(self, returns: List[ust.TypeReference]) -> str:
        """ Void return in Kotlin is absence of the return """
        if len(returns) == 0 or ust.SimpleType.VOID in returns:
            return ""
        return ": {}".format(self.translate_type(returns[0]))

    @staticmethod
    def gen_modifiers(modifiers: List[ust.Modifier]) -> str:
        """
        Everything is public by default.
        Constants and statics is processed via val/var and companion objects.
        """
        res = []
        if ust.Modifier.PRIVATE in modifiers:
            res.append("private")
        elif ust.Modifier.PROTECTED in modifiers:
            res.append("protected")
        if ust.Modifier.ABSTRACT in modifiers:
            res.append("abstract")
        return " ".join(res)

    @staticmethod
    def is_nullable(t: ust.TypeReference) -> bool:
        if isinstance(t.type, ust.UnionType):
            if ust.SimpleType.NULL in (x.type for x in t.type.types):
                return True
        return False

    def __translate_union_type(self, union_node: ust.UnionType) -> ust.TypeReference:
        # Got all alternatives except null itself.
        alternvatives = [
            t for t in union_node.types if t.type != ust.SimpleType.NULL
        ]
        # If that's just optional - return it.
        if len(alternvatives) == 1:
            return alternvatives[0]
        # Firstly check that all alternatives are Identifiers - o/w they can't have
        # common parents.
        to_solve = []
        for t in alternvatives:
            if not isinstance(t.type, ust.Identifier):
                return ust.TypeReference(ust.Identifier("Any", immutable=True))
            to_solve.append(t.type)
        # Then try to find the nearest common ancestor and return it if any found.
        parent = self.reference.get_common_ancestor(*to_solve)
        if parent is None:
            return ust.TypeReference(ust.Identifier("Any", immutable=True))
        return ust.TypeReference(parent)

    def _resolve_name(self, identifier: ust.Identifier) -> str:
        if self.name_resolver is None:
            return str(identifier)
        return self.name_resolver(identifier)

