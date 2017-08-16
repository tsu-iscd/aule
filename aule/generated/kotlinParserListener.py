# Generated from kotlinParser.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .kotlinParser import kotlinParser
else:
    from kotlinParser import kotlinParser

# This class defines a complete listener for a parse tree produced by kotlinParser.
class kotlinParserListener(ParseTreeListener):

    # Enter a parse tree produced by kotlinParser#root.
    def enterRoot(self, ctx:kotlinParser.RootContext):
        pass

    # Exit a parse tree produced by kotlinParser#root.
    def exitRoot(self, ctx:kotlinParser.RootContext):
        pass


    # Enter a parse tree produced by kotlinParser#preamble.
    def enterPreamble(self, ctx:kotlinParser.PreambleContext):
        pass

    # Exit a parse tree produced by kotlinParser#preamble.
    def exitPreamble(self, ctx:kotlinParser.PreambleContext):
        pass


    # Enter a parse tree produced by kotlinParser#packageHeader.
    def enterPackageHeader(self, ctx:kotlinParser.PackageHeaderContext):
        pass

    # Exit a parse tree produced by kotlinParser#packageHeader.
    def exitPackageHeader(self, ctx:kotlinParser.PackageHeaderContext):
        pass


    # Enter a parse tree produced by kotlinParser#importHeader.
    def enterImportHeader(self, ctx:kotlinParser.ImportHeaderContext):
        pass

    # Exit a parse tree produced by kotlinParser#importHeader.
    def exitImportHeader(self, ctx:kotlinParser.ImportHeaderContext):
        pass


    # Enter a parse tree produced by kotlinParser#toplevelObject.
    def enterToplevelObject(self, ctx:kotlinParser.ToplevelObjectContext):
        pass

    # Exit a parse tree produced by kotlinParser#toplevelObject.
    def exitToplevelObject(self, ctx:kotlinParser.ToplevelObjectContext):
        pass


    # Enter a parse tree produced by kotlinParser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:kotlinParser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by kotlinParser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:kotlinParser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by kotlinParser#optionalProjection.
    def enterOptionalProjection(self, ctx:kotlinParser.OptionalProjectionContext):
        pass

    # Exit a parse tree produced by kotlinParser#optionalProjection.
    def exitOptionalProjection(self, ctx:kotlinParser.OptionalProjectionContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeParameters.
    def enterTypeParameters(self, ctx:kotlinParser.TypeParametersContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeParameters.
    def exitTypeParameters(self, ctx:kotlinParser.TypeParametersContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeParameter.
    def enterTypeParameter(self, ctx:kotlinParser.TypeParameterContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeParameter.
    def exitTypeParameter(self, ctx:kotlinParser.TypeParameterContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeArguments.
    def enterTypeArguments(self, ctx:kotlinParser.TypeArgumentsContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeArguments.
    def exitTypeArguments(self, ctx:kotlinParser.TypeArgumentsContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeConstraints.
    def enterTypeConstraints(self, ctx:kotlinParser.TypeConstraintsContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeConstraints.
    def exitTypeConstraints(self, ctx:kotlinParser.TypeConstraintsContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeConstraint.
    def enterTypeConstraint(self, ctx:kotlinParser.TypeConstraintContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeConstraint.
    def exitTypeConstraint(self, ctx:kotlinParser.TypeConstraintContext):
        pass


    # Enter a parse tree produced by kotlinParser#type_.
    def enterType_(self, ctx:kotlinParser.Type_Context):
        pass

    # Exit a parse tree produced by kotlinParser#type_.
    def exitType_(self, ctx:kotlinParser.Type_Context):
        pass


    # Enter a parse tree produced by kotlinParser#typeDescriptor.
    def enterTypeDescriptor(self, ctx:kotlinParser.TypeDescriptorContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeDescriptor.
    def exitTypeDescriptor(self, ctx:kotlinParser.TypeDescriptorContext):
        pass


    # Enter a parse tree produced by kotlinParser#userType.
    def enterUserType(self, ctx:kotlinParser.UserTypeContext):
        pass

    # Exit a parse tree produced by kotlinParser#userType.
    def exitUserType(self, ctx:kotlinParser.UserTypeContext):
        pass


    # Enter a parse tree produced by kotlinParser#simpleUserType_typeParam.
    def enterSimpleUserType_typeParam(self, ctx:kotlinParser.SimpleUserType_typeParamContext):
        pass

    # Exit a parse tree produced by kotlinParser#simpleUserType_typeParam.
    def exitSimpleUserType_typeParam(self, ctx:kotlinParser.SimpleUserType_typeParamContext):
        pass


    # Enter a parse tree produced by kotlinParser#simpleUserType.
    def enterSimpleUserType(self, ctx:kotlinParser.SimpleUserTypeContext):
        pass

    # Exit a parse tree produced by kotlinParser#simpleUserType.
    def exitSimpleUserType(self, ctx:kotlinParser.SimpleUserTypeContext):
        pass


    # Enter a parse tree produced by kotlinParser#variableDeclarationEntry.
    def enterVariableDeclarationEntry(self, ctx:kotlinParser.VariableDeclarationEntryContext):
        pass

    # Exit a parse tree produced by kotlinParser#variableDeclarationEntry.
    def exitVariableDeclarationEntry(self, ctx:kotlinParser.VariableDeclarationEntryContext):
        pass


    # Enter a parse tree produced by kotlinParser#functionType_paramOrType.
    def enterFunctionType_paramOrType(self, ctx:kotlinParser.FunctionType_paramOrTypeContext):
        pass

    # Exit a parse tree produced by kotlinParser#functionType_paramOrType.
    def exitFunctionType_paramOrType(self, ctx:kotlinParser.FunctionType_paramOrTypeContext):
        pass


    # Enter a parse tree produced by kotlinParser#extensionFunctionTypeNoReceiver.
    def enterExtensionFunctionTypeNoReceiver(self, ctx:kotlinParser.ExtensionFunctionTypeNoReceiverContext):
        pass

    # Exit a parse tree produced by kotlinParser#extensionFunctionTypeNoReceiver.
    def exitExtensionFunctionTypeNoReceiver(self, ctx:kotlinParser.ExtensionFunctionTypeNoReceiverContext):
        pass


    # Enter a parse tree produced by kotlinParser#functionTypeNoReceiver.
    def enterFunctionTypeNoReceiver(self, ctx:kotlinParser.FunctionTypeNoReceiverContext):
        pass

    # Exit a parse tree produced by kotlinParser#functionTypeNoReceiver.
    def exitFunctionTypeNoReceiver(self, ctx:kotlinParser.FunctionTypeNoReceiverContext):
        pass


    # Enter a parse tree produced by kotlinParser#multipleVariableDeclarations.
    def enterMultipleVariableDeclarations(self, ctx:kotlinParser.MultipleVariableDeclarationsContext):
        pass

    # Exit a parse tree produced by kotlinParser#multipleVariableDeclarations.
    def exitMultipleVariableDeclarations(self, ctx:kotlinParser.MultipleVariableDeclarationsContext):
        pass


    # Enter a parse tree produced by kotlinParser#propertyDeclaration.
    def enterPropertyDeclaration(self, ctx:kotlinParser.PropertyDeclarationContext):
        pass

    # Exit a parse tree produced by kotlinParser#propertyDeclaration.
    def exitPropertyDeclaration(self, ctx:kotlinParser.PropertyDeclarationContext):
        pass


    # Enter a parse tree produced by kotlinParser#getter.
    def enterGetter(self, ctx:kotlinParser.GetterContext):
        pass

    # Exit a parse tree produced by kotlinParser#getter.
    def exitGetter(self, ctx:kotlinParser.GetterContext):
        pass


    # Enter a parse tree produced by kotlinParser#setter.
    def enterSetter(self, ctx:kotlinParser.SetterContext):
        pass

    # Exit a parse tree produced by kotlinParser#setter.
    def exitSetter(self, ctx:kotlinParser.SetterContext):
        pass


    # Enter a parse tree produced by kotlinParser#modifiers.
    def enterModifiers(self, ctx:kotlinParser.ModifiersContext):
        pass

    # Exit a parse tree produced by kotlinParser#modifiers.
    def exitModifiers(self, ctx:kotlinParser.ModifiersContext):
        pass


    # Enter a parse tree produced by kotlinParser#modifier.
    def enterModifier(self, ctx:kotlinParser.ModifierContext):
        pass

    # Exit a parse tree produced by kotlinParser#modifier.
    def exitModifier(self, ctx:kotlinParser.ModifierContext):
        pass


    # Enter a parse tree produced by kotlinParser#modifierKeyword.
    def enterModifierKeyword(self, ctx:kotlinParser.ModifierKeywordContext):
        pass

    # Exit a parse tree produced by kotlinParser#modifierKeyword.
    def exitModifierKeyword(self, ctx:kotlinParser.ModifierKeywordContext):
        pass


    # Enter a parse tree produced by kotlinParser#hierarchyModifier.
    def enterHierarchyModifier(self, ctx:kotlinParser.HierarchyModifierContext):
        pass

    # Exit a parse tree produced by kotlinParser#hierarchyModifier.
    def exitHierarchyModifier(self, ctx:kotlinParser.HierarchyModifierContext):
        pass


    # Enter a parse tree produced by kotlinParser#classModifier.
    def enterClassModifier(self, ctx:kotlinParser.ClassModifierContext):
        pass

    # Exit a parse tree produced by kotlinParser#classModifier.
    def exitClassModifier(self, ctx:kotlinParser.ClassModifierContext):
        pass


    # Enter a parse tree produced by kotlinParser#accessModifier.
    def enterAccessModifier(self, ctx:kotlinParser.AccessModifierContext):
        pass

    # Exit a parse tree produced by kotlinParser#accessModifier.
    def exitAccessModifier(self, ctx:kotlinParser.AccessModifierContext):
        pass


    # Enter a parse tree produced by kotlinParser#varianceAnnotation.
    def enterVarianceAnnotation(self, ctx:kotlinParser.VarianceAnnotationContext):
        pass

    # Exit a parse tree produced by kotlinParser#varianceAnnotation.
    def exitVarianceAnnotation(self, ctx:kotlinParser.VarianceAnnotationContext):
        pass


    # Enter a parse tree produced by kotlinParser#annotations.
    def enterAnnotations(self, ctx:kotlinParser.AnnotationsContext):
        pass

    # Exit a parse tree produced by kotlinParser#annotations.
    def exitAnnotations(self, ctx:kotlinParser.AnnotationsContext):
        pass


    # Enter a parse tree produced by kotlinParser#annotation.
    def enterAnnotation(self, ctx:kotlinParser.AnnotationContext):
        pass

    # Exit a parse tree produced by kotlinParser#annotation.
    def exitAnnotation(self, ctx:kotlinParser.AnnotationContext):
        pass


    # Enter a parse tree produced by kotlinParser#annotationUseSiteTarget.
    def enterAnnotationUseSiteTarget(self, ctx:kotlinParser.AnnotationUseSiteTargetContext):
        pass

    # Exit a parse tree produced by kotlinParser#annotationUseSiteTarget.
    def exitAnnotationUseSiteTarget(self, ctx:kotlinParser.AnnotationUseSiteTargetContext):
        pass


    # Enter a parse tree produced by kotlinParser#valueArgument.
    def enterValueArgument(self, ctx:kotlinParser.ValueArgumentContext):
        pass

    # Exit a parse tree produced by kotlinParser#valueArgument.
    def exitValueArgument(self, ctx:kotlinParser.ValueArgumentContext):
        pass


    # Enter a parse tree produced by kotlinParser#valueArguments.
    def enterValueArguments(self, ctx:kotlinParser.ValueArgumentsContext):
        pass

    # Exit a parse tree produced by kotlinParser#valueArguments.
    def exitValueArguments(self, ctx:kotlinParser.ValueArgumentsContext):
        pass


    # Enter a parse tree produced by kotlinParser#unescapedAnnotation.
    def enterUnescapedAnnotation(self, ctx:kotlinParser.UnescapedAnnotationContext):
        pass

    # Exit a parse tree produced by kotlinParser#unescapedAnnotation.
    def exitUnescapedAnnotation(self, ctx:kotlinParser.UnescapedAnnotationContext):
        pass


    # Enter a parse tree produced by kotlinParser#jump.
    def enterJump(self, ctx:kotlinParser.JumpContext):
        pass

    # Exit a parse tree produced by kotlinParser#jump.
    def exitJump(self, ctx:kotlinParser.JumpContext):
        pass


    # Enter a parse tree produced by kotlinParser#labelReference.
    def enterLabelReference(self, ctx:kotlinParser.LabelReferenceContext):
        pass

    # Exit a parse tree produced by kotlinParser#labelReference.
    def exitLabelReference(self, ctx:kotlinParser.LabelReferenceContext):
        pass


    # Enter a parse tree produced by kotlinParser#labelDefinition.
    def enterLabelDefinition(self, ctx:kotlinParser.LabelDefinitionContext):
        pass

    # Exit a parse tree produced by kotlinParser#labelDefinition.
    def exitLabelDefinition(self, ctx:kotlinParser.LabelDefinitionContext):
        pass


    # Enter a parse tree produced by kotlinParser#parameter.
    def enterParameter(self, ctx:kotlinParser.ParameterContext):
        pass

    # Exit a parse tree produced by kotlinParser#parameter.
    def exitParameter(self, ctx:kotlinParser.ParameterContext):
        pass


    # Enter a parse tree produced by kotlinParser#functionParameter.
    def enterFunctionParameter(self, ctx:kotlinParser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by kotlinParser#functionParameter.
    def exitFunctionParameter(self, ctx:kotlinParser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by kotlinParser#primaryConstructor.
    def enterPrimaryConstructor(self, ctx:kotlinParser.PrimaryConstructorContext):
        pass

    # Exit a parse tree produced by kotlinParser#primaryConstructor.
    def exitPrimaryConstructor(self, ctx:kotlinParser.PrimaryConstructorContext):
        pass


    # Enter a parse tree produced by kotlinParser#secondaryConstructor.
    def enterSecondaryConstructor(self, ctx:kotlinParser.SecondaryConstructorContext):
        pass

    # Exit a parse tree produced by kotlinParser#secondaryConstructor.
    def exitSecondaryConstructor(self, ctx:kotlinParser.SecondaryConstructorContext):
        pass


    # Enter a parse tree produced by kotlinParser#constructorDelegationCall.
    def enterConstructorDelegationCall(self, ctx:kotlinParser.ConstructorDelegationCallContext):
        pass

    # Exit a parse tree produced by kotlinParser#constructorDelegationCall.
    def exitConstructorDelegationCall(self, ctx:kotlinParser.ConstructorDelegationCallContext):
        pass


    # Enter a parse tree produced by kotlinParser#callSuffix.
    def enterCallSuffix(self, ctx:kotlinParser.CallSuffixContext):
        pass

    # Exit a parse tree produced by kotlinParser#callSuffix.
    def exitCallSuffix(self, ctx:kotlinParser.CallSuffixContext):
        pass


    # Enter a parse tree produced by kotlinParser#constructorInvocation.
    def enterConstructorInvocation(self, ctx:kotlinParser.ConstructorInvocationContext):
        pass

    # Exit a parse tree produced by kotlinParser#constructorInvocation.
    def exitConstructorInvocation(self, ctx:kotlinParser.ConstructorInvocationContext):
        pass


    # Enter a parse tree produced by kotlinParser#explicitDelegation.
    def enterExplicitDelegation(self, ctx:kotlinParser.ExplicitDelegationContext):
        pass

    # Exit a parse tree produced by kotlinParser#explicitDelegation.
    def exitExplicitDelegation(self, ctx:kotlinParser.ExplicitDelegationContext):
        pass


    # Enter a parse tree produced by kotlinParser#delegationSpecifier.
    def enterDelegationSpecifier(self, ctx:kotlinParser.DelegationSpecifierContext):
        pass

    # Exit a parse tree produced by kotlinParser#delegationSpecifier.
    def exitDelegationSpecifier(self, ctx:kotlinParser.DelegationSpecifierContext):
        pass


    # Enter a parse tree produced by kotlinParser#classDeclaration.
    def enterClassDeclaration(self, ctx:kotlinParser.ClassDeclarationContext):
        pass

    # Exit a parse tree produced by kotlinParser#classDeclaration.
    def exitClassDeclaration(self, ctx:kotlinParser.ClassDeclarationContext):
        pass


    # Enter a parse tree produced by kotlinParser#supertypesSpecifiers.
    def enterSupertypesSpecifiers(self, ctx:kotlinParser.SupertypesSpecifiersContext):
        pass

    # Exit a parse tree produced by kotlinParser#supertypesSpecifiers.
    def exitSupertypesSpecifiers(self, ctx:kotlinParser.SupertypesSpecifiersContext):
        pass


    # Enter a parse tree produced by kotlinParser#objectDeclaration.
    def enterObjectDeclaration(self, ctx:kotlinParser.ObjectDeclarationContext):
        pass

    # Exit a parse tree produced by kotlinParser#objectDeclaration.
    def exitObjectDeclaration(self, ctx:kotlinParser.ObjectDeclarationContext):
        pass


    # Enter a parse tree produced by kotlinParser#companionObject.
    def enterCompanionObject(self, ctx:kotlinParser.CompanionObjectContext):
        pass

    # Exit a parse tree produced by kotlinParser#companionObject.
    def exitCompanionObject(self, ctx:kotlinParser.CompanionObjectContext):
        pass


    # Enter a parse tree produced by kotlinParser#classBody.
    def enterClassBody(self, ctx:kotlinParser.ClassBodyContext):
        pass

    # Exit a parse tree produced by kotlinParser#classBody.
    def exitClassBody(self, ctx:kotlinParser.ClassBodyContext):
        pass


    # Enter a parse tree produced by kotlinParser#members.
    def enterMembers(self, ctx:kotlinParser.MembersContext):
        pass

    # Exit a parse tree produced by kotlinParser#members.
    def exitMembers(self, ctx:kotlinParser.MembersContext):
        pass


    # Enter a parse tree produced by kotlinParser#valueParameters.
    def enterValueParameters(self, ctx:kotlinParser.ValueParametersContext):
        pass

    # Exit a parse tree produced by kotlinParser#valueParameters.
    def exitValueParameters(self, ctx:kotlinParser.ValueParametersContext):
        pass


    # Enter a parse tree produced by kotlinParser#functionDeclaration.
    def enterFunctionDeclaration(self, ctx:kotlinParser.FunctionDeclarationContext):
        pass

    # Exit a parse tree produced by kotlinParser#functionDeclaration.
    def exitFunctionDeclaration(self, ctx:kotlinParser.FunctionDeclarationContext):
        pass


    # Enter a parse tree produced by kotlinParser#statements.
    def enterStatements(self, ctx:kotlinParser.StatementsContext):
        pass

    # Exit a parse tree produced by kotlinParser#statements.
    def exitStatements(self, ctx:kotlinParser.StatementsContext):
        pass


    # Enter a parse tree produced by kotlinParser#functionBody.
    def enterFunctionBody(self, ctx:kotlinParser.FunctionBodyContext):
        pass

    # Exit a parse tree produced by kotlinParser#functionBody.
    def exitFunctionBody(self, ctx:kotlinParser.FunctionBodyContext):
        pass


    # Enter a parse tree produced by kotlinParser#block.
    def enterBlock(self, ctx:kotlinParser.BlockContext):
        pass

    # Exit a parse tree produced by kotlinParser#block.
    def exitBlock(self, ctx:kotlinParser.BlockContext):
        pass


    # Enter a parse tree produced by kotlinParser#anonymousInitializer.
    def enterAnonymousInitializer(self, ctx:kotlinParser.AnonymousInitializerContext):
        pass

    # Exit a parse tree produced by kotlinParser#anonymousInitializer.
    def exitAnonymousInitializer(self, ctx:kotlinParser.AnonymousInitializerContext):
        pass


    # Enter a parse tree produced by kotlinParser#enumClassBody.
    def enterEnumClassBody(self, ctx:kotlinParser.EnumClassBodyContext):
        pass

    # Exit a parse tree produced by kotlinParser#enumClassBody.
    def exitEnumClassBody(self, ctx:kotlinParser.EnumClassBodyContext):
        pass


    # Enter a parse tree produced by kotlinParser#enumEntries.
    def enterEnumEntries(self, ctx:kotlinParser.EnumEntriesContext):
        pass

    # Exit a parse tree produced by kotlinParser#enumEntries.
    def exitEnumEntries(self, ctx:kotlinParser.EnumEntriesContext):
        pass


    # Enter a parse tree produced by kotlinParser#enumEntry.
    def enterEnumEntry(self, ctx:kotlinParser.EnumEntryContext):
        pass

    # Exit a parse tree produced by kotlinParser#enumEntry.
    def exitEnumEntry(self, ctx:kotlinParser.EnumEntryContext):
        pass


    # Enter a parse tree produced by kotlinParser#ifExpression.
    def enterIfExpression(self, ctx:kotlinParser.IfExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#ifExpression.
    def exitIfExpression(self, ctx:kotlinParser.IfExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#tryExpression.
    def enterTryExpression(self, ctx:kotlinParser.TryExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#tryExpression.
    def exitTryExpression(self, ctx:kotlinParser.TryExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#catchBlock.
    def enterCatchBlock(self, ctx:kotlinParser.CatchBlockContext):
        pass

    # Exit a parse tree produced by kotlinParser#catchBlock.
    def exitCatchBlock(self, ctx:kotlinParser.CatchBlockContext):
        pass


    # Enter a parse tree produced by kotlinParser#finallyBlock.
    def enterFinallyBlock(self, ctx:kotlinParser.FinallyBlockContext):
        pass

    # Exit a parse tree produced by kotlinParser#finallyBlock.
    def exitFinallyBlock(self, ctx:kotlinParser.FinallyBlockContext):
        pass


    # Enter a parse tree produced by kotlinParser#loop.
    def enterLoop(self, ctx:kotlinParser.LoopContext):
        pass

    # Exit a parse tree produced by kotlinParser#loop.
    def exitLoop(self, ctx:kotlinParser.LoopContext):
        pass


    # Enter a parse tree produced by kotlinParser#forLoop.
    def enterForLoop(self, ctx:kotlinParser.ForLoopContext):
        pass

    # Exit a parse tree produced by kotlinParser#forLoop.
    def exitForLoop(self, ctx:kotlinParser.ForLoopContext):
        pass


    # Enter a parse tree produced by kotlinParser#whileLoop.
    def enterWhileLoop(self, ctx:kotlinParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by kotlinParser#whileLoop.
    def exitWhileLoop(self, ctx:kotlinParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by kotlinParser#doWhileLoop.
    def enterDoWhileLoop(self, ctx:kotlinParser.DoWhileLoopContext):
        pass

    # Exit a parse tree produced by kotlinParser#doWhileLoop.
    def exitDoWhileLoop(self, ctx:kotlinParser.DoWhileLoopContext):
        pass


    # Enter a parse tree produced by kotlinParser#expression.
    def enterExpression(self, ctx:kotlinParser.ExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#expression.
    def exitExpression(self, ctx:kotlinParser.ExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#disjunction.
    def enterDisjunction(self, ctx:kotlinParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by kotlinParser#disjunction.
    def exitDisjunction(self, ctx:kotlinParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by kotlinParser#conjunction.
    def enterConjunction(self, ctx:kotlinParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by kotlinParser#conjunction.
    def exitConjunction(self, ctx:kotlinParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by kotlinParser#equalityComparison.
    def enterEqualityComparison(self, ctx:kotlinParser.EqualityComparisonContext):
        pass

    # Exit a parse tree produced by kotlinParser#equalityComparison.
    def exitEqualityComparison(self, ctx:kotlinParser.EqualityComparisonContext):
        pass


    # Enter a parse tree produced by kotlinParser#comparison.
    def enterComparison(self, ctx:kotlinParser.ComparisonContext):
        pass

    # Exit a parse tree produced by kotlinParser#comparison.
    def exitComparison(self, ctx:kotlinParser.ComparisonContext):
        pass


    # Enter a parse tree produced by kotlinParser#namedInfix.
    def enterNamedInfix(self, ctx:kotlinParser.NamedInfixContext):
        pass

    # Exit a parse tree produced by kotlinParser#namedInfix.
    def exitNamedInfix(self, ctx:kotlinParser.NamedInfixContext):
        pass


    # Enter a parse tree produced by kotlinParser#elvisExpression.
    def enterElvisExpression(self, ctx:kotlinParser.ElvisExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#elvisExpression.
    def exitElvisExpression(self, ctx:kotlinParser.ElvisExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#infixFunctionCall.
    def enterInfixFunctionCall(self, ctx:kotlinParser.InfixFunctionCallContext):
        pass

    # Exit a parse tree produced by kotlinParser#infixFunctionCall.
    def exitInfixFunctionCall(self, ctx:kotlinParser.InfixFunctionCallContext):
        pass


    # Enter a parse tree produced by kotlinParser#rangeExpression.
    def enterRangeExpression(self, ctx:kotlinParser.RangeExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#rangeExpression.
    def exitRangeExpression(self, ctx:kotlinParser.RangeExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:kotlinParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:kotlinParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:kotlinParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:kotlinParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeRHS.
    def enterTypeRHS(self, ctx:kotlinParser.TypeRHSContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeRHS.
    def exitTypeRHS(self, ctx:kotlinParser.TypeRHSContext):
        pass


    # Enter a parse tree produced by kotlinParser#prefixUnaryExpression.
    def enterPrefixUnaryExpression(self, ctx:kotlinParser.PrefixUnaryExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#prefixUnaryExpression.
    def exitPrefixUnaryExpression(self, ctx:kotlinParser.PrefixUnaryExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#postfixUnaryExpression.
    def enterPostfixUnaryExpression(self, ctx:kotlinParser.PostfixUnaryExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#postfixUnaryExpression.
    def exitPostfixUnaryExpression(self, ctx:kotlinParser.PostfixUnaryExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#callableReference.
    def enterCallableReference(self, ctx:kotlinParser.CallableReferenceContext):
        pass

    # Exit a parse tree produced by kotlinParser#callableReference.
    def exitCallableReference(self, ctx:kotlinParser.CallableReferenceContext):
        pass


    # Enter a parse tree produced by kotlinParser#identifier.
    def enterIdentifier(self, ctx:kotlinParser.IdentifierContext):
        pass

    # Exit a parse tree produced by kotlinParser#identifier.
    def exitIdentifier(self, ctx:kotlinParser.IdentifierContext):
        pass


    # Enter a parse tree produced by kotlinParser#stringLiteral.
    def enterStringLiteral(self, ctx:kotlinParser.StringLiteralContext):
        pass

    # Exit a parse tree produced by kotlinParser#stringLiteral.
    def exitStringLiteral(self, ctx:kotlinParser.StringLiteralContext):
        pass


    # Enter a parse tree produced by kotlinParser#atomicExpression.
    def enterAtomicExpression(self, ctx:kotlinParser.AtomicExpressionContext):
        pass

    # Exit a parse tree produced by kotlinParser#atomicExpression.
    def exitAtomicExpression(self, ctx:kotlinParser.AtomicExpressionContext):
        pass


    # Enter a parse tree produced by kotlinParser#literalConstant.
    def enterLiteralConstant(self, ctx:kotlinParser.LiteralConstantContext):
        pass

    # Exit a parse tree produced by kotlinParser#literalConstant.
    def exitLiteralConstant(self, ctx:kotlinParser.LiteralConstantContext):
        pass


    # Enter a parse tree produced by kotlinParser#declaration.
    def enterDeclaration(self, ctx:kotlinParser.DeclarationContext):
        pass

    # Exit a parse tree produced by kotlinParser#declaration.
    def exitDeclaration(self, ctx:kotlinParser.DeclarationContext):
        pass


    # Enter a parse tree produced by kotlinParser#statement.
    def enterStatement(self, ctx:kotlinParser.StatementContext):
        pass

    # Exit a parse tree produced by kotlinParser#statement.
    def exitStatement(self, ctx:kotlinParser.StatementContext):
        pass


    # Enter a parse tree produced by kotlinParser#multiplicativeOperation.
    def enterMultiplicativeOperation(self, ctx:kotlinParser.MultiplicativeOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#multiplicativeOperation.
    def exitMultiplicativeOperation(self, ctx:kotlinParser.MultiplicativeOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#additiveOperation.
    def enterAdditiveOperation(self, ctx:kotlinParser.AdditiveOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#additiveOperation.
    def exitAdditiveOperation(self, ctx:kotlinParser.AdditiveOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#inOperation.
    def enterInOperation(self, ctx:kotlinParser.InOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#inOperation.
    def exitInOperation(self, ctx:kotlinParser.InOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#typeOperation.
    def enterTypeOperation(self, ctx:kotlinParser.TypeOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#typeOperation.
    def exitTypeOperation(self, ctx:kotlinParser.TypeOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#isOperation.
    def enterIsOperation(self, ctx:kotlinParser.IsOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#isOperation.
    def exitIsOperation(self, ctx:kotlinParser.IsOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#comparisonOperation.
    def enterComparisonOperation(self, ctx:kotlinParser.ComparisonOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#comparisonOperation.
    def exitComparisonOperation(self, ctx:kotlinParser.ComparisonOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#equalityOperation.
    def enterEqualityOperation(self, ctx:kotlinParser.EqualityOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#equalityOperation.
    def exitEqualityOperation(self, ctx:kotlinParser.EqualityOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#assignmentOperator.
    def enterAssignmentOperator(self, ctx:kotlinParser.AssignmentOperatorContext):
        pass

    # Exit a parse tree produced by kotlinParser#assignmentOperator.
    def exitAssignmentOperator(self, ctx:kotlinParser.AssignmentOperatorContext):
        pass


    # Enter a parse tree produced by kotlinParser#prefixUnaryOperation.
    def enterPrefixUnaryOperation(self, ctx:kotlinParser.PrefixUnaryOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#prefixUnaryOperation.
    def exitPrefixUnaryOperation(self, ctx:kotlinParser.PrefixUnaryOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#postfixUnaryOperation.
    def enterPostfixUnaryOperation(self, ctx:kotlinParser.PostfixUnaryOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#postfixUnaryOperation.
    def exitPostfixUnaryOperation(self, ctx:kotlinParser.PostfixUnaryOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#annotatedLambda.
    def enterAnnotatedLambda(self, ctx:kotlinParser.AnnotatedLambdaContext):
        pass

    # Exit a parse tree produced by kotlinParser#annotatedLambda.
    def exitAnnotatedLambda(self, ctx:kotlinParser.AnnotatedLambdaContext):
        pass


    # Enter a parse tree produced by kotlinParser#memberAccessOperation.
    def enterMemberAccessOperation(self, ctx:kotlinParser.MemberAccessOperationContext):
        pass

    # Exit a parse tree produced by kotlinParser#memberAccessOperation.
    def exitMemberAccessOperation(self, ctx:kotlinParser.MemberAccessOperationContext):
        pass


    # Enter a parse tree produced by kotlinParser#functionLiteral.
    def enterFunctionLiteral(self, ctx:kotlinParser.FunctionLiteralContext):
        pass

    # Exit a parse tree produced by kotlinParser#functionLiteral.
    def exitFunctionLiteral(self, ctx:kotlinParser.FunctionLiteralContext):
        pass


    # Enter a parse tree produced by kotlinParser#arrayAccess.
    def enterArrayAccess(self, ctx:kotlinParser.ArrayAccessContext):
        pass

    # Exit a parse tree produced by kotlinParser#arrayAccess.
    def exitArrayAccess(self, ctx:kotlinParser.ArrayAccessContext):
        pass


    # Enter a parse tree produced by kotlinParser#objectLiteral.
    def enterObjectLiteral(self, ctx:kotlinParser.ObjectLiteralContext):
        pass

    # Exit a parse tree produced by kotlinParser#objectLiteral.
    def exitObjectLiteral(self, ctx:kotlinParser.ObjectLiteralContext):
        pass


    # Enter a parse tree produced by kotlinParser#when.
    def enterWhen(self, ctx:kotlinParser.WhenContext):
        pass

    # Exit a parse tree produced by kotlinParser#when.
    def exitWhen(self, ctx:kotlinParser.WhenContext):
        pass


    # Enter a parse tree produced by kotlinParser#whenEntry.
    def enterWhenEntry(self, ctx:kotlinParser.WhenEntryContext):
        pass

    # Exit a parse tree produced by kotlinParser#whenEntry.
    def exitWhenEntry(self, ctx:kotlinParser.WhenEntryContext):
        pass


    # Enter a parse tree produced by kotlinParser#whenCondition.
    def enterWhenCondition(self, ctx:kotlinParser.WhenConditionContext):
        pass

    # Exit a parse tree produced by kotlinParser#whenCondition.
    def exitWhenCondition(self, ctx:kotlinParser.WhenConditionContext):
        pass


