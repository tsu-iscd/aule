from typing import Union

from ..classnodes import *


def is_abstract(node: Union[FieldDeclaration, MethodDeclaration, ClassDeclaration]) -> bool:
    """ Tests whether the given node is abstract
    :type node: FieldDeclaration | MethodDeclaration | ClassDeclaration
    :rtype: bool
    """
    if isinstance(node, ClassDeclaration):
        return any(is_abstract(m) for m in node.methods) \
                or any(is_abstract(f) for f in node.fields)
    if not hasattr(node, "modifiers"):
        return False
    return Modifier.ABSTRACT in node.modifiers
