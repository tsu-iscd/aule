# Generated from lua.g4 by ANTLR 4.6
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .luaParser import luaParser
else:
    from luaParser import luaParser

# This class defines a complete listener for a parse tree produced by luaParser.
class luaListener(ParseTreeListener):

    # Enter a parse tree produced by luaParser#root.
    def enterRoot(self, ctx:luaParser.RootContext):
        pass

    # Exit a parse tree produced by luaParser#root.
    def exitRoot(self, ctx:luaParser.RootContext):
        pass


    # Enter a parse tree produced by luaParser#block.
    def enterBlock(self, ctx:luaParser.BlockContext):
        pass

    # Exit a parse tree produced by luaParser#block.
    def exitBlock(self, ctx:luaParser.BlockContext):
        pass


    # Enter a parse tree produced by luaParser#stat.
    def enterStat(self, ctx:luaParser.StatContext):
        pass

    # Exit a parse tree produced by luaParser#stat.
    def exitStat(self, ctx:luaParser.StatContext):
        pass


    # Enter a parse tree produced by luaParser#retstat.
    def enterRetstat(self, ctx:luaParser.RetstatContext):
        pass

    # Exit a parse tree produced by luaParser#retstat.
    def exitRetstat(self, ctx:luaParser.RetstatContext):
        pass


    # Enter a parse tree produced by luaParser#label.
    def enterLabel(self, ctx:luaParser.LabelContext):
        pass

    # Exit a parse tree produced by luaParser#label.
    def exitLabel(self, ctx:luaParser.LabelContext):
        pass


    # Enter a parse tree produced by luaParser#funcname.
    def enterFuncname(self, ctx:luaParser.FuncnameContext):
        pass

    # Exit a parse tree produced by luaParser#funcname.
    def exitFuncname(self, ctx:luaParser.FuncnameContext):
        pass


    # Enter a parse tree produced by luaParser#varlist.
    def enterVarlist(self, ctx:luaParser.VarlistContext):
        pass

    # Exit a parse tree produced by luaParser#varlist.
    def exitVarlist(self, ctx:luaParser.VarlistContext):
        pass


    # Enter a parse tree produced by luaParser#namelist.
    def enterNamelist(self, ctx:luaParser.NamelistContext):
        pass

    # Exit a parse tree produced by luaParser#namelist.
    def exitNamelist(self, ctx:luaParser.NamelistContext):
        pass


    # Enter a parse tree produced by luaParser#explist.
    def enterExplist(self, ctx:luaParser.ExplistContext):
        pass

    # Exit a parse tree produced by luaParser#explist.
    def exitExplist(self, ctx:luaParser.ExplistContext):
        pass


    # Enter a parse tree produced by luaParser#exp.
    def enterExp(self, ctx:luaParser.ExpContext):
        pass

    # Exit a parse tree produced by luaParser#exp.
    def exitExp(self, ctx:luaParser.ExpContext):
        pass


    # Enter a parse tree produced by luaParser#prefixexp.
    def enterPrefixexp(self, ctx:luaParser.PrefixexpContext):
        pass

    # Exit a parse tree produced by luaParser#prefixexp.
    def exitPrefixexp(self, ctx:luaParser.PrefixexpContext):
        pass


    # Enter a parse tree produced by luaParser#functioncall.
    def enterFunctioncall(self, ctx:luaParser.FunctioncallContext):
        pass

    # Exit a parse tree produced by luaParser#functioncall.
    def exitFunctioncall(self, ctx:luaParser.FunctioncallContext):
        pass


    # Enter a parse tree produced by luaParser#varOrExp.
    def enterVarOrExp(self, ctx:luaParser.VarOrExpContext):
        pass

    # Exit a parse tree produced by luaParser#varOrExp.
    def exitVarOrExp(self, ctx:luaParser.VarOrExpContext):
        pass


    # Enter a parse tree produced by luaParser#var.
    def enterVar(self, ctx:luaParser.VarContext):
        pass

    # Exit a parse tree produced by luaParser#var.
    def exitVar(self, ctx:luaParser.VarContext):
        pass


    # Enter a parse tree produced by luaParser#varSuffix.
    def enterVarSuffix(self, ctx:luaParser.VarSuffixContext):
        pass

    # Exit a parse tree produced by luaParser#varSuffix.
    def exitVarSuffix(self, ctx:luaParser.VarSuffixContext):
        pass


    # Enter a parse tree produced by luaParser#nameAndArgs.
    def enterNameAndArgs(self, ctx:luaParser.NameAndArgsContext):
        pass

    # Exit a parse tree produced by luaParser#nameAndArgs.
    def exitNameAndArgs(self, ctx:luaParser.NameAndArgsContext):
        pass


    # Enter a parse tree produced by luaParser#args.
    def enterArgs(self, ctx:luaParser.ArgsContext):
        pass

    # Exit a parse tree produced by luaParser#args.
    def exitArgs(self, ctx:luaParser.ArgsContext):
        pass


    # Enter a parse tree produced by luaParser#functiondef.
    def enterFunctiondef(self, ctx:luaParser.FunctiondefContext):
        pass

    # Exit a parse tree produced by luaParser#functiondef.
    def exitFunctiondef(self, ctx:luaParser.FunctiondefContext):
        pass


    # Enter a parse tree produced by luaParser#funcbody.
    def enterFuncbody(self, ctx:luaParser.FuncbodyContext):
        pass

    # Exit a parse tree produced by luaParser#funcbody.
    def exitFuncbody(self, ctx:luaParser.FuncbodyContext):
        pass


    # Enter a parse tree produced by luaParser#parlist.
    def enterParlist(self, ctx:luaParser.ParlistContext):
        pass

    # Exit a parse tree produced by luaParser#parlist.
    def exitParlist(self, ctx:luaParser.ParlistContext):
        pass


    # Enter a parse tree produced by luaParser#tableconstructor.
    def enterTableconstructor(self, ctx:luaParser.TableconstructorContext):
        pass

    # Exit a parse tree produced by luaParser#tableconstructor.
    def exitTableconstructor(self, ctx:luaParser.TableconstructorContext):
        pass


    # Enter a parse tree produced by luaParser#fieldlist.
    def enterFieldlist(self, ctx:luaParser.FieldlistContext):
        pass

    # Exit a parse tree produced by luaParser#fieldlist.
    def exitFieldlist(self, ctx:luaParser.FieldlistContext):
        pass


    # Enter a parse tree produced by luaParser#field.
    def enterField(self, ctx:luaParser.FieldContext):
        pass

    # Exit a parse tree produced by luaParser#field.
    def exitField(self, ctx:luaParser.FieldContext):
        pass


    # Enter a parse tree produced by luaParser#fieldsep.
    def enterFieldsep(self, ctx:luaParser.FieldsepContext):
        pass

    # Exit a parse tree produced by luaParser#fieldsep.
    def exitFieldsep(self, ctx:luaParser.FieldsepContext):
        pass


    # Enter a parse tree produced by luaParser#operatorOr.
    def enterOperatorOr(self, ctx:luaParser.OperatorOrContext):
        pass

    # Exit a parse tree produced by luaParser#operatorOr.
    def exitOperatorOr(self, ctx:luaParser.OperatorOrContext):
        pass


    # Enter a parse tree produced by luaParser#operatorAnd.
    def enterOperatorAnd(self, ctx:luaParser.OperatorAndContext):
        pass

    # Exit a parse tree produced by luaParser#operatorAnd.
    def exitOperatorAnd(self, ctx:luaParser.OperatorAndContext):
        pass


    # Enter a parse tree produced by luaParser#operatorComparison.
    def enterOperatorComparison(self, ctx:luaParser.OperatorComparisonContext):
        pass

    # Exit a parse tree produced by luaParser#operatorComparison.
    def exitOperatorComparison(self, ctx:luaParser.OperatorComparisonContext):
        pass


    # Enter a parse tree produced by luaParser#operatorStrcat.
    def enterOperatorStrcat(self, ctx:luaParser.OperatorStrcatContext):
        pass

    # Exit a parse tree produced by luaParser#operatorStrcat.
    def exitOperatorStrcat(self, ctx:luaParser.OperatorStrcatContext):
        pass


    # Enter a parse tree produced by luaParser#operatorAddSub.
    def enterOperatorAddSub(self, ctx:luaParser.OperatorAddSubContext):
        pass

    # Exit a parse tree produced by luaParser#operatorAddSub.
    def exitOperatorAddSub(self, ctx:luaParser.OperatorAddSubContext):
        pass


    # Enter a parse tree produced by luaParser#operatorMulDivMod.
    def enterOperatorMulDivMod(self, ctx:luaParser.OperatorMulDivModContext):
        pass

    # Exit a parse tree produced by luaParser#operatorMulDivMod.
    def exitOperatorMulDivMod(self, ctx:luaParser.OperatorMulDivModContext):
        pass


    # Enter a parse tree produced by luaParser#operatorBitwise.
    def enterOperatorBitwise(self, ctx:luaParser.OperatorBitwiseContext):
        pass

    # Exit a parse tree produced by luaParser#operatorBitwise.
    def exitOperatorBitwise(self, ctx:luaParser.OperatorBitwiseContext):
        pass


    # Enter a parse tree produced by luaParser#operatorUnary.
    def enterOperatorUnary(self, ctx:luaParser.OperatorUnaryContext):
        pass

    # Exit a parse tree produced by luaParser#operatorUnary.
    def exitOperatorUnary(self, ctx:luaParser.OperatorUnaryContext):
        pass


    # Enter a parse tree produced by luaParser#operatorPower.
    def enterOperatorPower(self, ctx:luaParser.OperatorPowerContext):
        pass

    # Exit a parse tree produced by luaParser#operatorPower.
    def exitOperatorPower(self, ctx:luaParser.OperatorPowerContext):
        pass


    # Enter a parse tree produced by luaParser#number.
    def enterNumber(self, ctx:luaParser.NumberContext):
        pass

    # Exit a parse tree produced by luaParser#number.
    def exitNumber(self, ctx:luaParser.NumberContext):
        pass


    # Enter a parse tree produced by luaParser#string.
    def enterString(self, ctx:luaParser.StringContext):
        pass

    # Exit a parse tree produced by luaParser#string.
    def exitString(self, ctx:luaParser.StringContext):
        pass


