# Generated from idl.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .idlParser import idlParser
else:
    from idlParser import idlParser

# This class defines a complete listener for a parse tree produced by idlParser.
class idlListener(ParseTreeListener):

    # Enter a parse tree produced by idlParser#root.
    def enterRoot(self, ctx:idlParser.RootContext):
        pass

    # Exit a parse tree produced by idlParser#root.
    def exitRoot(self, ctx:idlParser.RootContext):
        pass


    # Enter a parse tree produced by idlParser#statement.
    def enterStatement(self, ctx:idlParser.StatementContext):
        pass

    # Exit a parse tree produced by idlParser#statement.
    def exitStatement(self, ctx:idlParser.StatementContext):
        pass


    # Enter a parse tree produced by idlParser#interface_statement.
    def enterInterface_statement(self, ctx:idlParser.Interface_statementContext):
        pass

    # Exit a parse tree produced by idlParser#interface_statement.
    def exitInterface_statement(self, ctx:idlParser.Interface_statementContext):
        pass


    # Enter a parse tree produced by idlParser#enum_statement.
    def enterEnum_statement(self, ctx:idlParser.Enum_statementContext):
        pass

    # Exit a parse tree produced by idlParser#enum_statement.
    def exitEnum_statement(self, ctx:idlParser.Enum_statementContext):
        pass


    # Enter a parse tree produced by idlParser#enum_member.
    def enterEnum_member(self, ctx:idlParser.Enum_memberContext):
        pass

    # Exit a parse tree produced by idlParser#enum_member.
    def exitEnum_member(self, ctx:idlParser.Enum_memberContext):
        pass


    # Enter a parse tree produced by idlParser#interface_header.
    def enterInterface_header(self, ctx:idlParser.Interface_headerContext):
        pass

    # Exit a parse tree produced by idlParser#interface_header.
    def exitInterface_header(self, ctx:idlParser.Interface_headerContext):
        pass


    # Enter a parse tree produced by idlParser#interface_inheritance.
    def enterInterface_inheritance(self, ctx:idlParser.Interface_inheritanceContext):
        pass

    # Exit a parse tree produced by idlParser#interface_inheritance.
    def exitInterface_inheritance(self, ctx:idlParser.Interface_inheritanceContext):
        pass


    # Enter a parse tree produced by idlParser#interface_body.
    def enterInterface_body(self, ctx:idlParser.Interface_bodyContext):
        pass

    # Exit a parse tree produced by idlParser#interface_body.
    def exitInterface_body(self, ctx:idlParser.Interface_bodyContext):
        pass


    # Enter a parse tree produced by idlParser#field_statement.
    def enterField_statement(self, ctx:idlParser.Field_statementContext):
        pass

    # Exit a parse tree produced by idlParser#field_statement.
    def exitField_statement(self, ctx:idlParser.Field_statementContext):
        pass


    # Enter a parse tree produced by idlParser#field_body.
    def enterField_body(self, ctx:idlParser.Field_bodyContext):
        pass

    # Exit a parse tree produced by idlParser#field_body.
    def exitField_body(self, ctx:idlParser.Field_bodyContext):
        pass


    # Enter a parse tree produced by idlParser#element_type.
    def enterElement_type(self, ctx:idlParser.Element_typeContext):
        pass

    # Exit a parse tree produced by idlParser#element_type.
    def exitElement_type(self, ctx:idlParser.Element_typeContext):
        pass


    # Enter a parse tree produced by idlParser#array_type.
    def enterArray_type(self, ctx:idlParser.Array_typeContext):
        pass

    # Exit a parse tree produced by idlParser#array_type.
    def exitArray_type(self, ctx:idlParser.Array_typeContext):
        pass


    # Enter a parse tree produced by idlParser#interface_name.
    def enterInterface_name(self, ctx:idlParser.Interface_nameContext):
        pass

    # Exit a parse tree produced by idlParser#interface_name.
    def exitInterface_name(self, ctx:idlParser.Interface_nameContext):
        pass


    # Enter a parse tree produced by idlParser#type_name.
    def enterType_name(self, ctx:idlParser.Type_nameContext):
        pass

    # Exit a parse tree produced by idlParser#type_name.
    def exitType_name(self, ctx:idlParser.Type_nameContext):
        pass


    # Enter a parse tree produced by idlParser#enum_name.
    def enterEnum_name(self, ctx:idlParser.Enum_nameContext):
        pass

    # Exit a parse tree produced by idlParser#enum_name.
    def exitEnum_name(self, ctx:idlParser.Enum_nameContext):
        pass


    # Enter a parse tree produced by idlParser#field_name.
    def enterField_name(self, ctx:idlParser.Field_nameContext):
        pass

    # Exit a parse tree produced by idlParser#field_name.
    def exitField_name(self, ctx:idlParser.Field_nameContext):
        pass


    # Enter a parse tree produced by idlParser#tag_string.
    def enterTag_string(self, ctx:idlParser.Tag_stringContext):
        pass

    # Exit a parse tree produced by idlParser#tag_string.
    def exitTag_string(self, ctx:idlParser.Tag_stringContext):
        pass


    # Enter a parse tree produced by idlParser#tag.
    def enterTag(self, ctx:idlParser.TagContext):
        pass

    # Exit a parse tree produced by idlParser#tag.
    def exitTag(self, ctx:idlParser.TagContext):
        pass


    # Enter a parse tree produced by idlParser#simple_type.
    def enterSimple_type(self, ctx:idlParser.Simple_typeContext):
        pass

    # Exit a parse tree produced by idlParser#simple_type.
    def exitSimple_type(self, ctx:idlParser.Simple_typeContext):
        pass


    # Enter a parse tree produced by idlParser#literal_value.
    def enterLiteral_value(self, ctx:idlParser.Literal_valueContext):
        pass

    # Exit a parse tree produced by idlParser#literal_value.
    def exitLiteral_value(self, ctx:idlParser.Literal_valueContext):
        pass


