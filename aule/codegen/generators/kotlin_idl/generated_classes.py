from typing import List

from aule.codegen import ust


SERIALIZER_CLASS = ust.Identifier("Serializer")


def create_serializer(classes: List[ust.ClassDeclaration]) -> str:
    """ Here we create a class that's would be parent for every other class and
        is a helper for JSON serialization.

        Example:
            @JsonTypeInfo(
                    use = JsonTypeInfo.Id.NAME,
                    include = JsonTypeInfo.As.PROPERTY,
                    property = "type")
            @JsonSubTypes(
                    JsonSubTypes.Type(value = Cat::class, name = "cat"),
                    JsonSubTypes.Type(value = Dog::class, name = "dog")
            )
            open class Serializer {}
    """
    sub_types = []
    for cls in classes:
        sub_types.append(
            "JsonSubTypes.Type(value = {kotlin_name}::class, name = \"{real_name}\")".format(
                kotlin_name=cls.name, # TODO: that one should be mangled
                real_name=cls.name, # And that one shouldn't
         ))
    return """
@JsonTypeInfo(
    use = JsonTypeInfo.Id.NAME,
    include = JsonTypeInfo.As.PROPERTY,
    property = "type")
@JsonSubTypes(
    {subtypes})
open class {cls_name}
""".format(subtypes=",\n    ".join(sub_types), cls_name=SERIALIZER_CLASS.name)


def create_decoder():
    pass


def create_listener(classes: List[ust.ClassDeclaration],
                    root_context_type: str = "") -> ust.ClassDeclaration:
    methods = []
    for cls in classes:
        methods.append(gen_method("enter{}".format(cls.name), root_context_type))
        methods.append(gen_method("exit{}".format(cls.name), root_context_type))
    class_node = ust.ClassDeclaration(
        name=ust.Identifier("ASTListener"),
        methods=methods
    )
    # Add empty body to constructor
    class_node.constructor.body = ust.Block([""])
    # That class designed to be open - so inject "overridden" property
    setattr(class_node, "overridden", True)
    return class_node


def create_visitor(classes: List[ust.ClassDeclaration],
                   root_context_type: str = "") -> ust.ClassDeclaration:
    class_node = ust.ClassDeclaration(
        name=ust.Identifier("ASTVisitor"),
        methods=[
            gen_method("visit{}".format(cls.name), root_context_type)
            for cls in classes
        ]
    )
    # That class designed to be open - so inject "overridden" property
    setattr(class_node, "overridden", True)
    return class_node


def gen_method(name: str, arg_type: str = "") -> ust.MethodDeclaration:
    method_node = ust.MethodDeclaration(
        name=ust.Identifier(name),
        arguments=[
            ust.Argument(
                name=ust.Identifier("ctx"),
                type=ust.TypeReference(
                    ust.Identifier(arg_type or "Any", immutable=True)
                )
            )
        ],
        returns=[],
        body=ust.Block([]),
    )
    setattr(method_node, "overridden", True)
    return method_node
