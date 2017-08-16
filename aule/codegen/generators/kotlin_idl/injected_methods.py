from aule.codegen import ust


def inject_listener(cls: ust.ClassDeclaration, listener_type: str):
    cls.methods.append(
        ust.MethodDeclaration(
            name=ust.Identifier("enterNode"),
            arguments=[
                ust.Argument(
                    name=ust.Identifier("listener"),
                    type=ust.TypeReference(
                        ust.Identifier(listener_type or "Any", immutable=True)
                    )
                )
            ],
            returns=[],
            body=generate_method_call(
                object_name="listener",
                object_type=listener_type,
                method_name="enter{}".format(cls.name),
                arg_type=str(cls.name),
                needs_return=False,
            ),
        )
    )

    cls.methods.append(
        ust.MethodDeclaration(
            name=ust.Identifier("exitNode"),
            arguments=[
                ust.Argument(
                    name=ust.Identifier("listener"),
                    type=ust.TypeReference(
                        ust.Identifier(listener_type or "Any", immutable=True)
                    )
                )
            ],
            returns=[],
            body=generate_method_call(
                object_name="listener",
                object_type=listener_type,
                method_name="exit{}".format(cls.name),
                arg_type=str(cls.name),
                needs_return=False,
            ),
        )
    )


def inject_visitor(cls: ust.ClassDeclaration, visitor_type: str):
    cls.methods.append(
        ust.MethodDeclaration(
            name=ust.Identifier("accept"),
            arguments=[
                ust.Argument(
                    name=ust.Identifier("visitor"),
                    type=ust.TypeReference(
                        ust.Identifier(visitor_type or "Any", immutable=True)
                    )
                )
            ],
            returns=[
                ust.TypeReference(
                    ust.UnionType([
                        ust.TypeReference(ust.Identifier("Any", immutable=True)),
                        ust.TypeReference(ust.SimpleType.NULL),
                    ])
                )
            ],
            body=generate_method_call(
                object_name="visitor",
                object_type=visitor_type,
                method_name="visit{}".format(cls.name),
                arg_type=str(cls.name),
                needs_return=True,
            ),
        )
    )


def generate_method_call(object_name: str, object_type: str,
                         method_name: str, arg_type: str,
                         needs_return: bool) -> ust.Block:
    prefix = "return" if needs_return else ""
    # That's simple if we know the exact type of the object - just generate method call
    if object_type:
        return ust.Block([
            prefix + " {name}.{method}(self)".format(name=object_name, method=method_name)
        ])
    # Otherwise we have "Any" object and going to dynamically find the method
    return ust.Block([
         prefix + " {}::class.memberFunctions".format(object_name),
        "          .filter { it.visibility == KVisibility.PUBLIC }",
        "          .filter { it.name == \""+method_name+"\"  }",
        "          .filter { it.parameters.count() == 2 }",
        "          .filter { it.parameters[1].type.isSubtypeOf("+arg_type+"::class.starProjectedType) }",
        "          .firstOrNull()?.call({}, this)".format(object_name),
    ])