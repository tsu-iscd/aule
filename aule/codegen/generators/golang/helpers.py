from ... import ust

TYPES_MAP = {
    ust.SimpleType.INTEGER: "int",
    ust.SimpleType.FLOAT: "float",
    ust.SimpleType.STRING: "string",
    ust.SimpleType.BOOLEAN: "bool",
    ust.SimpleType.NULL: "nil",
    ust.SimpleType.VOID: None,
}


def translate_type(type_node):
    """
    :type type_node: nodes.TypeReference
    :rtype: str
    """
    if isinstance(type_node, ust.UnionType):
        type_node = type_node.types[0]
    if isinstance(type_node.type, ust.SimpleType):
        gotype = TYPES_MAP.get(type_node.type, type_node.type)
    else:
        gotype = str(type_node.type)
    if type_node.is_sequence:
        gotype = "[]{}".format(gotype)
    elif type_node.is_pointer:
        gotype = "*{}".format(gotype)
    return gotype


def typed(typed):
    """
    :type typed: nodes.Argument | nodes.FieldDeclaration
    :rtype: str
    """
    return "{} {}".format(typed.name, translate_type(typed.type))


def apply_modifiers(identified):
    """
    :type identified: nodes.FieldDeclaration | nodes.MethodDeclaration
    """
    name = identified.name.name
    if ust.Modifier.PRIVATE in identified.modifiers:
        identified.name.name = name[0].lower() + name[1:]
    else:
        identified.name.name = name[0].upper() + name[1:]
    return identified


def self_reference(struct_name):
    """
    :type struct_name: nodes.Identifier
    :rtype str
    """
    return str(struct_name)[0].lower()
