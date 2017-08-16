# Generated from lua.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .luaParser import luaParser
else:
    from luaParser import luaParser

# This class defines a complete generic visitor for a parse tree produced by luaParser.

class luaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by luaParser#root.
    def visitRoot(self, ctx:luaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#block.
    def visitBlock(self, ctx:luaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#stat.
    def visitStat(self, ctx:luaParser.StatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#retstat.
    def visitRetstat(self, ctx:luaParser.RetstatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#label.
    def visitLabel(self, ctx:luaParser.LabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#funcname.
    def visitFuncname(self, ctx:luaParser.FuncnameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#varlist.
    def visitVarlist(self, ctx:luaParser.VarlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#namelist.
    def visitNamelist(self, ctx:luaParser.NamelistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#explist.
    def visitExplist(self, ctx:luaParser.ExplistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#exp.
    def visitExp(self, ctx:luaParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#prefixexp.
    def visitPrefixexp(self, ctx:luaParser.PrefixexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#functioncall.
    def visitFunctioncall(self, ctx:luaParser.FunctioncallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#varOrExp.
    def visitVarOrExp(self, ctx:luaParser.VarOrExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#var.
    def visitVar(self, ctx:luaParser.VarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#varSuffix.
    def visitVarSuffix(self, ctx:luaParser.VarSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#nameAndArgs.
    def visitNameAndArgs(self, ctx:luaParser.NameAndArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#args.
    def visitArgs(self, ctx:luaParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#functiondef.
    def visitFunctiondef(self, ctx:luaParser.FunctiondefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#funcbody.
    def visitFuncbody(self, ctx:luaParser.FuncbodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#parlist.
    def visitParlist(self, ctx:luaParser.ParlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#tableconstructor.
    def visitTableconstructor(self, ctx:luaParser.TableconstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#fieldlist.
    def visitFieldlist(self, ctx:luaParser.FieldlistContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#field.
    def visitField(self, ctx:luaParser.FieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#fieldsep.
    def visitFieldsep(self, ctx:luaParser.FieldsepContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorOr.
    def visitOperatorOr(self, ctx:luaParser.OperatorOrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorAnd.
    def visitOperatorAnd(self, ctx:luaParser.OperatorAndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorComparison.
    def visitOperatorComparison(self, ctx:luaParser.OperatorComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorStrcat.
    def visitOperatorStrcat(self, ctx:luaParser.OperatorStrcatContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorAddSub.
    def visitOperatorAddSub(self, ctx:luaParser.OperatorAddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorMulDivMod.
    def visitOperatorMulDivMod(self, ctx:luaParser.OperatorMulDivModContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorBitwise.
    def visitOperatorBitwise(self, ctx:luaParser.OperatorBitwiseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorUnary.
    def visitOperatorUnary(self, ctx:luaParser.OperatorUnaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#operatorPower.
    def visitOperatorPower(self, ctx:luaParser.OperatorPowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#number.
    def visitNumber(self, ctx:luaParser.NumberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by luaParser#string.
    def visitString(self, ctx:luaParser.StringContext):
        return self.visitChildren(ctx)



del luaParser