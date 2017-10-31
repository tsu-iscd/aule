from aule.codegen import ust


TYPES_MAP = {
    ust.SimpleType.INTEGER: "int",
    ust.SimpleType.FLOAT: "double",
    ust.SimpleType.STRING: "String",
    ust.SimpleType.BOOLEAN: "boolean",
    ust.SimpleType.VOID: "void",
}


def translate_type(type_node):
    """
    :type type_node: nodes.TypeReference
    :rtype: str
    """
    if isinstance(type_node.type, ust.UnionType):
        return "UnionTypeNotImplemented"
    if isinstance(type_node.type, ust.SimpleType):
        javatype = TYPES_MAP.get(type_node.type, type_node.type)
    else:
        javatype = str(type_node.type)
    if type_node.is_pointer or type_node.is_sequence:
        javatype = "List<{}>".format(javatype)
    return javatype


def typed(typed):
    """
    :type typed: nodes.Argument | nodes.FieldDeclaration
    :rtype: str
    """
    return "{} {}".format(translate_type(typed.type), typed.name)



def gen_modifiers(modifiers):
    """
    :type modifiers: [ust.Modifier]
    :rtype str
    """
    res = []
    if ust.Modifier.PRIVATE in modifiers:
        res.append('private ')
    elif ust.Modifier.PROTECTED in modifiers:
        res.append('protected ')
    else:
        res.append('public ')
    if ust.Modifier.ABSTRACT in modifiers:
        res.append('abstract ')
    if ust.Modifier.STATIC in modifiers:
        res.append('static')
    if ust.Modifier.CONST in modifiers:
        res.append('const')
    return ' '.join(res)
