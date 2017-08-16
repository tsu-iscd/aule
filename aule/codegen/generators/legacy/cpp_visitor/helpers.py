from aule.codegen import ust as nodes
from .generator import INDENT


def gen_class_header(cls_node):
    """
    :type cls_node: ust.ClassDeclaration
    :rtype: str
    """
    header = "class {}".format(cls_node.name)
    if cls_node.parents:
        header += ': ' + ', '.join(
            'public {}'.format(p.name) for p in cls_node.parents
        )
    return header


def gen_init_list(init_node):
    """
    :type init_node: ust.Constructor
    """
    init_list = INDENT + ': {}'.format(
        gen_init_statement(init_node.arguments[0])
    )
    for f in init_node.arguments[1:]:
        init_list += '\n' + INDENT + ', {}'.format(f)
    return init_list


def gen_init_statement(field):
    """
    :type field: ust.FieldDeclaration
    :rtype: str
    """
    return "{field}({init_value})".format(
        field=field.name,
        init_value=field.name,
    )


def gen_modifiers(modifiers):
    """
    :type modifiers: list[ust.Modifier]
    :rtype: str
    """
    res = []
    if nodes.Modifier.PRIVATE in modifiers:
        res.append('private:')
    elif nodes.Modifier.PROTECTED in modifiers:
        res.append('protected:')
    else:
        res.append('public:')
    if nodes.Modifier.ABSTRACT in modifiers:
        res.append('virtual')
    if nodes.Modifier.STATIC in modifiers:
        res.append('static')
    if nodes.Modifier.CONST in modifiers:
        res.append('const')
    return ' '.join(res)
