from aule.codegen.ust import *
from ..python.generator import Generator as PythonGenerator


def inject_listener(cls):
    """
    :type cls: ust.ClassDeclaration
    """
    cls.methods.append(
        MethodDeclaration(
            name=Identifier("enterNode"),
            arguments=[
                Argument(
                    name=Identifier("listener"),
                    type=TypeReference(PythonGenerator.OBJECT_CLASS)
                )
            ],
            returns=[],
            body=Block([
                "if hasattr(listener, \"enter{}\")".format(cls.name),
                Block([
                    "listener.enter{}(self)".format(cls.name),
                ]),
            ]),
        )
    )

    cls.methods.append(
        MethodDeclaration(
            name=Identifier("exitNode"),
            arguments=[
                Argument(
                    name=Identifier("listener"),
                    type=TypeReference(PythonGenerator.OBJECT_CLASS)
                )
            ],
            returns=[],
            body=Block([
                "if hasattr(listener, \"exit{}\")".format(cls.name),
                Block([
                    "listener.exit{}(self)".format(cls.name),
                ]),
            ]),
        )
    )


def inject_visitor(cls):
    """
    :type cls: ust.ClassDeclaration
    """
    cls.methods.append(
        MethodDeclaration(
            name=Identifier("accept"),
            arguments=[
                Argument(
                    name=Identifier("visitor"),
                    type=TypeReference(PythonGenerator.OBJECT_CLASS)
                )
            ],
            returns=[],
            body=Block([
                "if hasattr(visitor, \"visit{}\")".format(cls.name),
                Block([
                    "return visitor.visit{}(self)".format(cls.name),
                ]),
            ]),
        )
    )
