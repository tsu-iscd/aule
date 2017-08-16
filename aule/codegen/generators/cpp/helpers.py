from typing import Tuple, Union, List
from aule.codegen import ust
from pprint import pprint

# Type shortcut.
TypedNode = Union[ust.SimpleType, ust.Identifier, ust.UnionType, ust.TypeReference]


class TypeHelpers(object):
    TYPES_MAP = {
        ust.SimpleType.INTEGER: "int",
        ust.SimpleType.FLOAT: "double",
        ust.SimpleType.STRING: "string",
        ust.SimpleType.BOOLEAN: "bool",
        ust.SimpleType.VOID: "void",
    }
    
    POINTER_FIELD = "{}*"
    
    ARRAY_FIELD = "vector<{}>"
    
    OPTIONAL_FIELD = "Optional<{}>"
    
    ANY_FIELD = "Any"

    def __init__(self, class_reference: ust.helpers.ClassesReference) -> None:
        self.reference = class_reference

    def translate_type(self, node: TypedNode) -> str:
        """ Recursively translates IDL type into C++ type declaration """
        if isinstance(node, ust.SimpleType) and node in self.TYPES_MAP:
            # If it's a simple type translate it via map
            return "{}".format(self.TYPES_MAP[node])
        elif isinstance(node, ust.Identifier):
            # If it's an Identifier type - just cast it to string and make pointer
            # ! if is's Any there don't need to make pointer
            if(str(node) == self.ANY_FIELD):
                return node.name
            return self.POINTER_FIELD.format(node.name)
        elif isinstance(node, ust.TypeReference):
            # If it's a type reference - translate it recursively and then apply
            # necessary modifiers.
            new_type = self.translate_type(node.type)
            # vector and basic types can't store null, so they are wrapped in Optional
            # other nullable types wrapped in POINTER_FIELD
            if self.is_nullable(node) and (self.is_array(node) or new_type in self.TYPES_MAP.values()):
                return self.OPTIONAL_FIELD.format(new_type)
            if node.is_sequence:
                new_type = self.ARRAY_FIELD.format(new_type)
            return new_type
        elif isinstance(node, ust.UnionType):
            # If that's is a union - look for the common ancestor
            return self.translate_type(
                self.__translate_union_type(node)
                )
        raise TypeError("Unknown node {}".format(node))

    def typed(self, typed: Union[ust.FieldDeclaration, ust.Argument]) -> str:
        """ Description """
        return "{}".format(self.translate_type(typed.type))

    def gen_return(self, returns: List[ust.TypeReference]) -> str:
        """ Description """
        if len(returns) == 0:
            ret = ust.SimpleType.VOID
        else:
            ret = ust.UnionType(types=returns)
        return self.translate_type(ret)

    @staticmethod
    def gen_modifiers(modifiers: List[ust.Modifier]) -> str:
        """ Description """
        res = []
        if ust.Modifier.PRIVATE in modifiers:
            res.append('private:')
        elif ust.Modifier.PROTECTED in modifiers:
            res.append('protected:')
        else:
            res.append('public:')
        if ust.Modifier.ABSTRACT in modifiers:
            res.append('virtual')
        if ust.Modifier.STATIC in modifiers:
            res.append('static')
        if ust.Modifier.CONST in modifiers:
            res.append('const')
        return ' '.join(res)

    @staticmethod
    def is_nullable(t: ust.TypeReference) -> bool:
        if isinstance(t.type, ust.UnionType):
            if ust.SimpleType.NULL in (x.type for x in t.type.types):
                return True
        return False

    @staticmethod
    def is_array(t: ust.TypeReference) -> bool:
        if t.is_sequence:
            return True
        if isinstance(t.type, ust.UnionType):
            return any(TypeHelpers.is_array(s) for s in t.type.types)

    def __translate_union_type(self, union_node: ust.UnionType) -> ust.TypeReference:
        # Got all alternatives except null itself.
        alternatives = [
            t for t in union_node.types if t.type != ust.SimpleType.NULL
        ]
        # If that's just optional - return it.
        if len(alternatives) == 1:
            return alternatives[0]
        # Firstly check that all alternatives are Identifiers - o/w they can't have
        # common parents.
        to_solve = []
        for t in alternatives:
            if not isinstance(t.type, ust.Identifier):
                return ust.TypeReference(ust.Identifier(ANY_FIELD))
            to_solve.append(t.type)
        # Then try to find the nearest common ancestor and return it if any found.
        parent = self.reference.get_common_ancestor(*to_solve)
        if parent is None:
            return ust.TypeReference(ust.Identifier(ANY_FIELD))
        return ust.TypeReference(parent)

    @staticmethod
    def _get_names(some_list: Union[ List[ust.FieldDeclaration], List[ust.Argument] ] ) -> List[ust.Identifier]:
        f_names = []
        for f in some_list:
            f_names.append(f.name)
        return f_names

    def separate_args(self, cls: ust.ClassDeclaration ) -> Tuple[List[ust.Argument], List[ust.Argument]]:
        """ Separates the args into two parts: those that occur in `fields` and the others """
        in_fields = []
        other = []
        fields_names = self._get_names(cls.fields)
        for arg in cls.constructor.arguments:
            if arg.name in fields_names:
                in_fields.append(arg)
            else:
                other.append(arg)
        return (in_fields, other)


ENUMEXCEPTION = """
#include <exception>

/* Enums */
class EnumException : public exception {
    string enum_name, err_value;
public:
    EnumException(string enum_name_, string err_value_) : enum_name(enum_name_), err_value(err_value_){};
    virtual const string what(){
        ostringstream ss;
        ss << "\\"" << err_value << "\\" is incorrect value for " << enum_name;
        return ss.str();
    }
};
"""


INCLUDES = """\
#pragma once

#include <string>
#include <memory>
#include <vector>
#include <sstream>

#include "Optional.h"

#include "Any.h"

using namespace std;
"""