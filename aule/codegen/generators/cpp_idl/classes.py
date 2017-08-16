from aule.codegen.ust import *


def create_listener(classes):
    """
    :type classes: list[ClassDeclaration]
    """
    methods = []
    for cls in classes:
        methods.append(gen_enter(cls.name))
        methods.append(gen_exit(cls.name))
    class_node = ClassDeclaration(
        name=Identifier("ASTListener"),
        methods=methods
    )
    return class_node


def create_visitor(classes):
    """
    :type classes: list[ClassDeclaration]
    """
    class_node = ClassDeclaration(
        name=Identifier("ASTVisitor"),
        methods=[
            MethodDeclaration(
                name=Identifier("visit{}".format(cls.name)),
                arguments=[
                    Argument(
                        name=Identifier("tree"),
                        type=TypeReference(Identifier(cls.name))
                    )
                ],
                returns=[TypeReference(Identifier("Any"))],
                body=Block([]),
                modifiers=[Modifier.ABSTRACT]
            )
            for cls in classes
            ]
    )
    return class_node


def gen_enter(name):
    """
    :type name: Identifier
    :rtype MethodDeclaration
    """
    return MethodDeclaration(
        name=Identifier("enter{}".format(name)),
        arguments=[
            Argument(
                name=Identifier("ctx"),
                type=TypeReference(Identifier(name))
            )
        ],
        returns=[TypeReference(SimpleType.VOID)],
        body=Block([]),
        modifiers=[Modifier.ABSTRACT]
    )


def gen_exit(name):
    """
    :type name: Identifier
    :rtype MethodDeclaration
    """
    return MethodDeclaration(
        name=Identifier("exit{}".format(name)),
        arguments=[
            Argument(
                name=Identifier("ctx"),
                type=TypeReference(Identifier(name))
            )
        ],
        returns=[],
        body=Block([]),
        modifiers=[Modifier.ABSTRACT]
    )