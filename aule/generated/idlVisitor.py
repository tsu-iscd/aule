# Generated from idl.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .idlParser import idlParser
else:
    from idlParser import idlParser

# This class defines a complete generic visitor for a parse tree produced by idlParser.

class idlVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by idlParser#root.
    def visitRoot(self, ctx:idlParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#statement.
    def visitStatement(self, ctx:idlParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#interface_statement.
    def visitInterface_statement(self, ctx:idlParser.Interface_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#enum_statement.
    def visitEnum_statement(self, ctx:idlParser.Enum_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#enum_member.
    def visitEnum_member(self, ctx:idlParser.Enum_memberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#interface_header.
    def visitInterface_header(self, ctx:idlParser.Interface_headerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#interface_inheritance.
    def visitInterface_inheritance(self, ctx:idlParser.Interface_inheritanceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#interface_body.
    def visitInterface_body(self, ctx:idlParser.Interface_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#field_statement.
    def visitField_statement(self, ctx:idlParser.Field_statementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#field_body.
    def visitField_body(self, ctx:idlParser.Field_bodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#element_type.
    def visitElement_type(self, ctx:idlParser.Element_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#array_type.
    def visitArray_type(self, ctx:idlParser.Array_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#interface_name.
    def visitInterface_name(self, ctx:idlParser.Interface_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#type_name.
    def visitType_name(self, ctx:idlParser.Type_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#enum_name.
    def visitEnum_name(self, ctx:idlParser.Enum_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#field_name.
    def visitField_name(self, ctx:idlParser.Field_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#tag_string.
    def visitTag_string(self, ctx:idlParser.Tag_stringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#tag.
    def visitTag(self, ctx:idlParser.TagContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#simple_type.
    def visitSimple_type(self, ctx:idlParser.Simple_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by idlParser#literal_value.
    def visitLiteral_value(self, ctx:idlParser.Literal_valueContext):
        return self.visitChildren(ctx)



del idlParser