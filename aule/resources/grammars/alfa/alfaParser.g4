/*
A minimalist ALFA grammar for DBFW PoC.
*/

parser grammar alfaParser;

options { tokenVocab=alfaLexer; }

root
    : nameSpaceDeclaration* EOF
    ;

nameSpaceDeclaration
    : NAMESPACE nameSpaceId=ID '{' nameSpaceBody* '}'
    ;

nameSpaceBody
    : policySetDeclaration
    | policyDeclaration
    | nameSpaceDeclaration
    ;

policySetDeclaration
    : EXPORT? POLICYSET policySetId=ID '{' targetStatement? conditionStatement? applyStatement policySetBody* event*  '}'
    ;

policySetBody
    : ID 
    | policyDeclaration 
    | policySetDeclaration
    ;

policyDeclaration
    : EXPORT? POLICY policyId=ID '{' targetStatement? conditionStatement? applyStatement ruleDeclaration* event* '}'
    ;

applyStatement
    : APPLY algorithm = (PEMIT_OVERRIDES | DENY_OVERRIDES | FIRST_APPLICABLE | PERMIT_UNLESS_DENY | DENY_UNLESS_PERMIT | ONLY_ONE_APPLICABLE )
    ;

ruleDeclaration
    : RULE ruleId=ID? '{' effectStatement targetStatement? conditionStatement? event* '}'
    ;

effectStatement
    : PERMIT | DENY
    ;

targetStatement
    : TARGET (CLAUSE targetExpression)+
    ;

conditionStatement
    : CONDITION conditionExpression
    ;

targetExpression
    : unaryOperator targetExpression                          #targetUnaryExpression
    | targetExpression binaryOperator targetExpression        #targetBaseExpression
    | targetExpression AND targetExpression                   #targetAndExpression
    | targetExpression OR  targetExpression                   #targetOrExpression
    | anyExpression                                           #targetAnyExpression
    | attributeAccessExpression                               #targetAttributeAccessExpression
    | attributeValue                                          #targetAttributeValueExpression
    | arrayExpression                                         #targetArrayExpression
    ;

conditionExpression
    : unaryOperator conditionExpression                       #conditionUnaryExpression
    | conditionExpression binaryOperator conditionExpression  #conditionBaseExpression
    | conditionExpression AND conditionExpression             #conditionAndExpression
    | conditionExpression OR  conditionExpression             #conditionOrExpression
    | attributeAccessExpression                               #conditionAttributeAccessExpression
    | attributeValue                                          #conditionAttributeValueExpression
    | arrayExpression                                         #conditionArrayExpression
    | callExpression                                          #conditionCallExpression
    ;

event: 
    ON (PERMIT|DENY) '{' eventBody+ '}'
    ;

eventBody
    : obligation 
    | advice
    ;


obligation
    : OBLIGATION ID
    ;

advice
    : ADVICE ID
    ;

unaryOperator
    : NOT
    ;

binaryOperator
    : EQUALS | NOT_EQUALS | LESS_THAN | MORE_THAN | LESS_EQUAL | GREAT_EQUAL | IN | SUBSET | SUBSETEQ
    ;

callExpression
    : ID arguments
    ;

arguments
    : '(' ')'
    ;

anyExpression
    : ANY (attributeAccessExpression | arrayExpression) IN (attributeAccessExpression | arrayExpression)
    ;

attributeAccessExpression
    : attributeAccessExpression '.' ID
    | ID
    ;

attributeValue
    : literal
    ;

arrayExpression
    : '[' literal (',' literal)* ']'
    ;

literal:
    INT 
    | STRING 
    | boolean_literal
    ;

boolean_literal:
    TRUE 
    | FALSE
    ;
