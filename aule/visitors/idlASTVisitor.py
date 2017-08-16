from aule.codegen.ust import *
from aule.generated.idlVisitor import idlVisitor


class idlASTVisitor(idlVisitor):
    def visitRoot(self, ctx):
        nodes = []
        i = 0
        while ctx.statement(i):
            nodes.append(self.visit(ctx.statement(i)))
            i += 1
        return nodes

    def visitEnum_statement(self, ctx):
        enum_name = Identifier(ctx.name.getText())
        members = []
        i = 0
        while ctx.enum_member(i):
            member_name = ctx.enum_member(i).name.text
            member_value = ctx.enum_member(i).literal_value().getText()
            member = EnumMember(Identifier(member_name), member_value)
            members.append(member)
            i += 1
        return EnumDeclaration(enum_name, members)

    def visitInterface_statement(self, ctx):
        name, parents = self.visit(ctx.interface_header())
        fields = self.visit(ctx.interface_body())
        return ClassDeclaration(name=name, parents=parents, fields=fields)

    def visitInterface_header(self, ctx):
        name = "undefined"
        if ctx.name:
            name = Identifier(str(ctx.name.getText()))
        parents = []
        if ctx.interface_inheritance():
            parents = self.visit(ctx.interface_inheritance())
        return name, parents

    def visitInterface_body(self, ctx):
        fields = []
        i = 0
        while ctx.field_statement(i):
            fields.append(self.visit(ctx.field_statement(i)))
            i += 1
        return fields

    def visitField_statement(self, ctx):
        field_name = Identifier(str(ctx.name.getText()))
        modifiers = []
        default = None

        if ctx.ABSTRACT():
            modifiers.append(Modifier.ABSTRACT)
        if ctx.PUBLIC():
            modifiers.append(Modifier.PUBLIC)
        if ctx.PRIVATE():
            modifiers.append(Modifier.PRIVATE)
        if ctx.PROTECTED():
            modifiers.append(Modifier.PROTECTED)
        if ctx.CONST():
            modifiers.append(Modifier.CONST)
        if ctx.STATIC():
            modifiers.append(Modifier.STATIC)

        type_ = self.visit(ctx.field_body())
        tags = self.visit(ctx.tag_string()) if ctx.tag_string() else None
        return FieldDeclaration(field_name, type_, modifiers, tags, default)

    def visitField_body(self, ctx):
        i = 0
        elements = []
        if(ctx.element_type(0) is None):
            return TypeReference(SimpleType("str"))
        while ctx.element_type(i):
            elements.append(self.visit(ctx.element_type(i)))
            i += 1
        if len(elements) == 1:
            return elements[0]
        else:
            return TypeReference(UnionType(elements))

    def visitElement_type(self, ctx):
        if ctx.type_name():
            type_ = self.visit(ctx.type_name())
            return TypeReference(type_, is_pointer=False, is_sequence=False)
        elif ctx.array_type():
            type_ = self.visit(ctx.array_type())
            return TypeReference(type_, is_pointer=False, is_sequence=True)

    def visitArray_type(self, ctx):
        if not ctx.PIPE_SYMBOL(0):
            return self.visit(ctx.type_name(0))
        else:
            types = []
            i = 0
            while ctx.type_name(i):
                type_ = self.visit(ctx.type_name(i))
                types.append(TypeReference(type_, is_pointer=False, is_sequence=False))
                i += 1
            return UnionType(types)

    def visitType_name(self, ctx):
        if ctx.ID():
            return Identifier(str(ctx.ID().getText()))
        else:
            return SimpleType(str(ctx.simple_type().getText()))

    def visitTag_string(self, ctx):
        tags = []
        i = 0
        while ctx.tag(i):
            tags.append(FieldTag(
                name=Identifier(str(ctx.tag(i).ID().getText())),
                value=str(ctx.tag(i).STRING_VALUE().getText()),
            ))
            i += 1
        return tags

    def visitInterface_inheritance(self, ctx):
        parents = []
        i = 0
        while ctx.interface_name(i):
            parents.append(Identifier(str(ctx.interface_name(i).ID())))
            i += 1
        return parents
