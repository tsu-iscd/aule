# Generated from kotlinParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kotlinParser import kotlinParser
else:
    from kotlinParser import kotlinParser

# This class defines a complete generic visitor for a parse tree produced by kotlinParser.

class kotlinParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by kotlinParser#root.
    def visitRoot(self, ctx:kotlinParser.RootContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#preamble.
    def visitPreamble(self, ctx:kotlinParser.PreambleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#packageHeader.
    def visitPackageHeader(self, ctx:kotlinParser.PackageHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#importHeader.
    def visitImportHeader(self, ctx:kotlinParser.ImportHeaderContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#toplevelObject.
    def visitToplevelObject(self, ctx:kotlinParser.ToplevelObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:kotlinParser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#optionalProjection.
    def visitOptionalProjection(self, ctx:kotlinParser.OptionalProjectionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeParameters.
    def visitTypeParameters(self, ctx:kotlinParser.TypeParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeParameter.
    def visitTypeParameter(self, ctx:kotlinParser.TypeParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeArguments.
    def visitTypeArguments(self, ctx:kotlinParser.TypeArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeConstraints.
    def visitTypeConstraints(self, ctx:kotlinParser.TypeConstraintsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeConstraint.
    def visitTypeConstraint(self, ctx:kotlinParser.TypeConstraintContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#type_.
    def visitType_(self, ctx:kotlinParser.Type_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeDescriptor.
    def visitTypeDescriptor(self, ctx:kotlinParser.TypeDescriptorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#userType.
    def visitUserType(self, ctx:kotlinParser.UserTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#simpleUserType_typeParam.
    def visitSimpleUserType_typeParam(self, ctx:kotlinParser.SimpleUserType_typeParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#simpleUserType.
    def visitSimpleUserType(self, ctx:kotlinParser.SimpleUserTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#variableDeclarationEntry.
    def visitVariableDeclarationEntry(self, ctx:kotlinParser.VariableDeclarationEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#functionType_paramOrType.
    def visitFunctionType_paramOrType(self, ctx:kotlinParser.FunctionType_paramOrTypeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#extensionFunctionTypeNoReceiver.
    def visitExtensionFunctionTypeNoReceiver(self, ctx:kotlinParser.ExtensionFunctionTypeNoReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#functionTypeNoReceiver.
    def visitFunctionTypeNoReceiver(self, ctx:kotlinParser.FunctionTypeNoReceiverContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#multipleVariableDeclarations.
    def visitMultipleVariableDeclarations(self, ctx:kotlinParser.MultipleVariableDeclarationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#propertyDeclaration.
    def visitPropertyDeclaration(self, ctx:kotlinParser.PropertyDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#getter.
    def visitGetter(self, ctx:kotlinParser.GetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#setter.
    def visitSetter(self, ctx:kotlinParser.SetterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#modifiers.
    def visitModifiers(self, ctx:kotlinParser.ModifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#modifier.
    def visitModifier(self, ctx:kotlinParser.ModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#modifierKeyword.
    def visitModifierKeyword(self, ctx:kotlinParser.ModifierKeywordContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#hierarchyModifier.
    def visitHierarchyModifier(self, ctx:kotlinParser.HierarchyModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#classModifier.
    def visitClassModifier(self, ctx:kotlinParser.ClassModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#accessModifier.
    def visitAccessModifier(self, ctx:kotlinParser.AccessModifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#varianceAnnotation.
    def visitVarianceAnnotation(self, ctx:kotlinParser.VarianceAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#annotations.
    def visitAnnotations(self, ctx:kotlinParser.AnnotationsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#annotation.
    def visitAnnotation(self, ctx:kotlinParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#annotationUseSiteTarget.
    def visitAnnotationUseSiteTarget(self, ctx:kotlinParser.AnnotationUseSiteTargetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#valueArgument.
    def visitValueArgument(self, ctx:kotlinParser.ValueArgumentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#valueArguments.
    def visitValueArguments(self, ctx:kotlinParser.ValueArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#unescapedAnnotation.
    def visitUnescapedAnnotation(self, ctx:kotlinParser.UnescapedAnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#jump.
    def visitJump(self, ctx:kotlinParser.JumpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#labelReference.
    def visitLabelReference(self, ctx:kotlinParser.LabelReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#labelDefinition.
    def visitLabelDefinition(self, ctx:kotlinParser.LabelDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#parameter.
    def visitParameter(self, ctx:kotlinParser.ParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#functionParameter.
    def visitFunctionParameter(self, ctx:kotlinParser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#primaryConstructor.
    def visitPrimaryConstructor(self, ctx:kotlinParser.PrimaryConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#secondaryConstructor.
    def visitSecondaryConstructor(self, ctx:kotlinParser.SecondaryConstructorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#constructorDelegationCall.
    def visitConstructorDelegationCall(self, ctx:kotlinParser.ConstructorDelegationCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#callSuffix.
    def visitCallSuffix(self, ctx:kotlinParser.CallSuffixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#constructorInvocation.
    def visitConstructorInvocation(self, ctx:kotlinParser.ConstructorInvocationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#explicitDelegation.
    def visitExplicitDelegation(self, ctx:kotlinParser.ExplicitDelegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#delegationSpecifier.
    def visitDelegationSpecifier(self, ctx:kotlinParser.DelegationSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#classDeclaration.
    def visitClassDeclaration(self, ctx:kotlinParser.ClassDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#supertypesSpecifiers.
    def visitSupertypesSpecifiers(self, ctx:kotlinParser.SupertypesSpecifiersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#objectDeclaration.
    def visitObjectDeclaration(self, ctx:kotlinParser.ObjectDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#companionObject.
    def visitCompanionObject(self, ctx:kotlinParser.CompanionObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#classBody.
    def visitClassBody(self, ctx:kotlinParser.ClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#members.
    def visitMembers(self, ctx:kotlinParser.MembersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#valueParameters.
    def visitValueParameters(self, ctx:kotlinParser.ValueParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#functionDeclaration.
    def visitFunctionDeclaration(self, ctx:kotlinParser.FunctionDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#statements.
    def visitStatements(self, ctx:kotlinParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#functionBody.
    def visitFunctionBody(self, ctx:kotlinParser.FunctionBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#block.
    def visitBlock(self, ctx:kotlinParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#anonymousInitializer.
    def visitAnonymousInitializer(self, ctx:kotlinParser.AnonymousInitializerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#enumClassBody.
    def visitEnumClassBody(self, ctx:kotlinParser.EnumClassBodyContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#enumEntries.
    def visitEnumEntries(self, ctx:kotlinParser.EnumEntriesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#enumEntry.
    def visitEnumEntry(self, ctx:kotlinParser.EnumEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#ifExpression.
    def visitIfExpression(self, ctx:kotlinParser.IfExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#tryExpression.
    def visitTryExpression(self, ctx:kotlinParser.TryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#catchBlock.
    def visitCatchBlock(self, ctx:kotlinParser.CatchBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#finallyBlock.
    def visitFinallyBlock(self, ctx:kotlinParser.FinallyBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#loop.
    def visitLoop(self, ctx:kotlinParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#forLoop.
    def visitForLoop(self, ctx:kotlinParser.ForLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#whileLoop.
    def visitWhileLoop(self, ctx:kotlinParser.WhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#doWhileLoop.
    def visitDoWhileLoop(self, ctx:kotlinParser.DoWhileLoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#expression.
    def visitExpression(self, ctx:kotlinParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#disjunction.
    def visitDisjunction(self, ctx:kotlinParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#conjunction.
    def visitConjunction(self, ctx:kotlinParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#equalityComparison.
    def visitEqualityComparison(self, ctx:kotlinParser.EqualityComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#comparison.
    def visitComparison(self, ctx:kotlinParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#namedInfix.
    def visitNamedInfix(self, ctx:kotlinParser.NamedInfixContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#elvisExpression.
    def visitElvisExpression(self, ctx:kotlinParser.ElvisExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#infixFunctionCall.
    def visitInfixFunctionCall(self, ctx:kotlinParser.InfixFunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#rangeExpression.
    def visitRangeExpression(self, ctx:kotlinParser.RangeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:kotlinParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:kotlinParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeRHS.
    def visitTypeRHS(self, ctx:kotlinParser.TypeRHSContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#prefixUnaryExpression.
    def visitPrefixUnaryExpression(self, ctx:kotlinParser.PrefixUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#postfixUnaryExpression.
    def visitPostfixUnaryExpression(self, ctx:kotlinParser.PostfixUnaryExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#callableReference.
    def visitCallableReference(self, ctx:kotlinParser.CallableReferenceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#identifier.
    def visitIdentifier(self, ctx:kotlinParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#stringLiteral.
    def visitStringLiteral(self, ctx:kotlinParser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#atomicExpression.
    def visitAtomicExpression(self, ctx:kotlinParser.AtomicExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#literalConstant.
    def visitLiteralConstant(self, ctx:kotlinParser.LiteralConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#declaration.
    def visitDeclaration(self, ctx:kotlinParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#statement.
    def visitStatement(self, ctx:kotlinParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#multiplicativeOperation.
    def visitMultiplicativeOperation(self, ctx:kotlinParser.MultiplicativeOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#additiveOperation.
    def visitAdditiveOperation(self, ctx:kotlinParser.AdditiveOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#inOperation.
    def visitInOperation(self, ctx:kotlinParser.InOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#typeOperation.
    def visitTypeOperation(self, ctx:kotlinParser.TypeOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#isOperation.
    def visitIsOperation(self, ctx:kotlinParser.IsOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#comparisonOperation.
    def visitComparisonOperation(self, ctx:kotlinParser.ComparisonOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#equalityOperation.
    def visitEqualityOperation(self, ctx:kotlinParser.EqualityOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#assignmentOperator.
    def visitAssignmentOperator(self, ctx:kotlinParser.AssignmentOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#prefixUnaryOperation.
    def visitPrefixUnaryOperation(self, ctx:kotlinParser.PrefixUnaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#postfixUnaryOperation.
    def visitPostfixUnaryOperation(self, ctx:kotlinParser.PostfixUnaryOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#annotatedLambda.
    def visitAnnotatedLambda(self, ctx:kotlinParser.AnnotatedLambdaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#memberAccessOperation.
    def visitMemberAccessOperation(self, ctx:kotlinParser.MemberAccessOperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#functionLiteral.
    def visitFunctionLiteral(self, ctx:kotlinParser.FunctionLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#arrayAccess.
    def visitArrayAccess(self, ctx:kotlinParser.ArrayAccessContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#objectLiteral.
    def visitObjectLiteral(self, ctx:kotlinParser.ObjectLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#when.
    def visitWhen(self, ctx:kotlinParser.WhenContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#whenEntry.
    def visitWhenEntry(self, ctx:kotlinParser.WhenEntryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by kotlinParser#whenCondition.
    def visitWhenCondition(self, ctx:kotlinParser.WhenConditionContext):
        return self.visitChildren(ctx)



del kotlinParser