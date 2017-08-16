from aule.codegen import ust as nodes


class GoType(nodes.TypeReference):
    types_map = {
        nodes.SimpleType.INTEGER.name: "int",
        nodes.SimpleType.FLOAT.name: "float",
        nodes.SimpleType.STRING.name: "string",
        nodes.SimpleType.BOOLEAN.name: "bool",
        nodes.SimpleType.NULL.name: "nil",
        nodes.SimpleType.VOID.name: None,
    }

    def __init__(self, name, is_pointer):
        """
        :type name: str | ust.SimpleType
        :type is_pointer: bool
        """
        super(GoType, self).__init__(name, is_pointer)

    @classmethod
    def from_node(cls, type_):
        """
        :type type_: ust.TypeReference
        """
        new_type = cls.types_map.get(type_.name, type_.name)
        return cls(new_type, type_.is_pointer)

    def __str__(self):
        if self.is_pointer:
            return "*" + self.name
        return self.name


class GoArgument(nodes.Argument):
    def __init__(self, name, type, default=None):
        """
        :type name: ust.Identifier
        :type type: GoType
        :type default: any
        """
        super(GoArgument, self).__init__(name, type, default)

    @classmethod
    def from_node(cls, arg):
        """
        :type arg: ust.Argument
        """
        return cls(
            name=arg.name,
            type=GoType.from_node(arg.type),
            default=arg.default,
        )

    def __str__(self):
        return "{} {}".format(self.name, self.type)


class StructField(nodes.FieldDeclaration):
    def __init__(self, name, type):
        """
        :type name: ust.Identifier
        :type type: GoType
        """
        super(StructField, self).__init__(name, type)

    @classmethod
    def from_node(cls, field):
        """
        :type field: ust.FieldDeclaration
        """
        return cls(
            name=apply_modifiers(field.name, field.modifiers),
            type=GoType.from_node(field.type),
        )


class StructMethod(nodes.MethodDeclaration):
    def __init__(self, name, arguments, returns, body):
        """
        :type name: ust.Identifier
        :type arguments: list[GoArgument]
        :type returns: list[GoType]
        """
        super(StructMethod, self).__init__(name, arguments, returns, body)

    @classmethod
    def from_node(cls, method):
        """
        :type method:  ust.MethodDeclaration
        """
        return cls(
            name=apply_modifiers(method.name, method.modifiers),
            arguments=[
                GoArgument.from_node(arg) for arg in method.arguments
            ],
            returns=[
                GoType.from_node(t) for t in method.returns if t != nodes.SimpleType.VOID
            ],
            body=method.body,
        )


class Struct(nodes.ClassDeclaration):
    """
    :type self_reference: ust.Identifier
    """
    def __init__(self, name, fields, methods, parents=None):
        """
        :type name: ust.Identifier
        :type parents: list[ust.Identifier]
        :type fields: list[StructField]
        :type methods: list[StructMethod]
        """
        super(Struct, self).__init__(name, fields=fields, methods=methods, parents=parents)
        self.self_reference = nodes.Identifier(str(self.name)[0].lower())
        self.constructor = self._create_constructor()

    @classmethod
    def from_node(cls, class_):
        """
        :type class_: ust.ClassDeclaration
        """
        struct = cls(
            name=apply_modifiers(class_.name, class_.modifiers),
            parents=class_.parents,
            fields=[
                StructField.from_node(f) for f in class_.fields
            ],
            methods=[
                StructMethod.from_node(m) for m in class_.methods
            ],
        )
        struct.self_reference = nodes.Identifier(str(struct.name)[0].lower())
        struct._rewrite_constructor(class_)
        return struct

    def _rewrite_constructor(self, class_):
        """
        :type class_: ust.ClassDeclaration
        """
        cls_ret = class_.constructor.returns[0]
        self.constructor = nodes.Constructor(
            name=nodes.Identifier("New{}".format(self.name)),
            arguments=[
                GoArgument(name=f.name, type=f.type) for f in self.fields
            ],
            returns=[
                GoType(name=str(self.name), is_pointer=cls_ret.is_pointer)
            ],
        )


def apply_modifiers(identifier, modifiers):
    """
    :type identifier: ust.Identifier
    :type modifiers: list[ust.Modifier]
    :rtype: ust.Identifier
    """
    if nodes.Modifier.PRIVATE in modifiers:
        return private(identifier)
    else:
        return public(identifier)


def public(i):
    """
    :type i: ust.Identifier
    :rtype: ust.Identifier
    """
    return nodes.Identifier(i.name[0].upper() + i.name[1:])


def private(i):
    """
    :type i: ust.Identifier
    :rtype: ust.Identifier
    """
    return nodes.Identifier(i.name[0].lower() + i.name[1:])
