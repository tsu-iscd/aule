# Generated from alfaParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .alfaParser import alfaParser
else:
    from alfaParser import alfaParser

# This class defines a complete generic visitor for a parse tree produced by alfaParser.

class alfaParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by alfaParser#root.
    def visitRoot(self, ctx:alfaParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#nameSpaceDeclaration.
    def visitNameSpaceDeclaration(self, ctx:alfaParser.NameSpaceDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#nameSpaceBody.
    def visitNameSpaceBody(self, ctx:alfaParser.NameSpaceBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#policySetDeclaration.
    def visitPolicySetDeclaration(self, ctx:alfaParser.PolicySetDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#policySetBody.
    def visitPolicySetBody(self, ctx:alfaParser.PolicySetBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#policyDeclaration.
    def visitPolicyDeclaration(self, ctx:alfaParser.PolicyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#applyStatement.
    def visitApplyStatement(self, ctx:alfaParser.ApplyStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#ruleDeclaration.
    def visitRuleDeclaration(self, ctx:alfaParser.RuleDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#effectStatement.
    def visitEffectStatement(self, ctx:alfaParser.EffectStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetStatement.
    def visitTargetStatement(self, ctx:alfaParser.TargetStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionStatement.
    def visitConditionStatement(self, ctx:alfaParser.ConditionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetAnyExpression.
    def visitTargetAnyExpression(self, ctx:alfaParser.TargetAnyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetAndExpression.
    def visitTargetAndExpression(self, ctx:alfaParser.TargetAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetOrExpression.
    def visitTargetOrExpression(self, ctx:alfaParser.TargetOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetUnaryExpression.
    def visitTargetUnaryExpression(self, ctx:alfaParser.TargetUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetArrayExpression.
    def visitTargetArrayExpression(self, ctx:alfaParser.TargetArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetAttributeValueExpression.
    def visitTargetAttributeValueExpression(self, ctx:alfaParser.TargetAttributeValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetAttributeAccessExpression.
    def visitTargetAttributeAccessExpression(self, ctx:alfaParser.TargetAttributeAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#targetBaseExpression.
    def visitTargetBaseExpression(self, ctx:alfaParser.TargetBaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionOrExpression.
    def visitConditionOrExpression(self, ctx:alfaParser.ConditionOrExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionAttributeValueExpression.
    def visitConditionAttributeValueExpression(self, ctx:alfaParser.ConditionAttributeValueExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionUnaryExpression.
    def visitConditionUnaryExpression(self, ctx:alfaParser.ConditionUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionAndExpression.
    def visitConditionAndExpression(self, ctx:alfaParser.ConditionAndExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionCallExpression.
    def visitConditionCallExpression(self, ctx:alfaParser.ConditionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionBaseExpression.
    def visitConditionBaseExpression(self, ctx:alfaParser.ConditionBaseExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionAttributeAccessExpression.
    def visitConditionAttributeAccessExpression(self, ctx:alfaParser.ConditionAttributeAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#conditionArrayExpression.
    def visitConditionArrayExpression(self, ctx:alfaParser.ConditionArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#event.
    def visitEvent(self, ctx:alfaParser.EventContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#eventBody.
    def visitEventBody(self, ctx:alfaParser.EventBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#obligation.
    def visitObligation(self, ctx:alfaParser.ObligationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#advice.
    def visitAdvice(self, ctx:alfaParser.AdviceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#unaryOperator.
    def visitUnaryOperator(self, ctx:alfaParser.UnaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#binaryOperator.
    def visitBinaryOperator(self, ctx:alfaParser.BinaryOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#callExpression.
    def visitCallExpression(self, ctx:alfaParser.CallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#arguments.
    def visitArguments(self, ctx:alfaParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#anyExpression.
    def visitAnyExpression(self, ctx:alfaParser.AnyExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#attributeAccessExpression.
    def visitAttributeAccessExpression(self, ctx:alfaParser.AttributeAccessExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#attributeValue.
    def visitAttributeValue(self, ctx:alfaParser.AttributeValueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#arrayExpression.
    def visitArrayExpression(self, ctx:alfaParser.ArrayExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#literal.
    def visitLiteral(self, ctx:alfaParser.LiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by alfaParser#boolean_literal.
    def visitBoolean_literal(self, ctx:alfaParser.Boolean_literalContext):
        return self.visitChildren(ctx)



del alfaParser