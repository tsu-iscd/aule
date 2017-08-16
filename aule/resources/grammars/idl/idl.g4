/*
Aule IDL grammar.
The MIT License (MIT)
Copyright (C) 2017, Ivan Khudyashov (ihudyashov@ptsecurity.com), Denis Kolegov (dkolegov@ptsecurity.com)
IDL - Interface description language
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
*/

grammar idl;

// --------------------------------------------
// Parser
// --------------------------------------------

root:
    statement+ EOF
    ;

statement:
    interface_statement
    | enum_statement
    ;

interface_statement:
    interface_header interface_body
    ;

enum_statement:
    ENUM name=enum_name CURVE_BRACKET_OPEN enum_member+ CURVE_BRACKET_CLOSE
    ;

enum_member:
    name=(ID
        | ANY_TYPE
        | INT_TYPE
        | FLOAT_TYPE
        | STR_TYPE
        | BOOL_TYPE
        | VOID_TYPE
        | NULL_TYPE
        | ENUM
        )
    EQUALS_SYMBOL literal_value SEMI_SYMBOL
    ;

interface_header:
    INTERFACE name=interface_name interface_inheritance?
    ;

interface_inheritance:
    INHERITANCE_SYMBOL interface_name (COMMA_SYMBOL interface_name)*
    ;

interface_body:
    CURVE_BRACKET_OPEN field_statement* CURVE_BRACKET_CLOSE
    ;

field_statement:
    ABSTRACT?
    PRIVATE?
    PUBLIC?
    CONST?
    STATIC?
    PROTECTED?
    name=field_name (COLON_SYMBOL field_body)? tag_string? SEMI_SYMBOL
    ;

field_body:
    element_type (PIPE_SYMBOL element_type)*
    | literal_value
    ;

element_type:
    type_name | array_type
    ;

array_type:
    SQUARE_BRACKET_OPEN type_name (PIPE_SYMBOL type_name)* SQUARE_BRACKET_CLOSE
    ;

interface_name:
    ID
    ;

type_name:
    simple_type
    | ID
    ;

enum_name:
    ID
    ;

field_name:
    ID
    ;

tag_string:
    '`' tag+ '`'
    ;

tag:
    ID ':' STRING_VALUE
    ;

simple_type: STR_TYPE | INT_TYPE | BOOL_TYPE | VOID_TYPE | NULL_TYPE | ANY_TYPE | FLOAT_TYPE
    ;

literal_value:
    STRING_VALUE
    ;

// --------------------------------------------
// Lexer
// --------------------------------------------

SPACE:                              [ \t\r\n]+     -> channel(HIDDEN);
LINE_COMMENT:                       ('//' | '#') ~[\r\n]* -> channel(HIDDEN);
ABSTRACT:                           A B S T R A C T;
INTERFACE:                          I N T E R F A C E;
ENUM:                               E N U M;
BACKTICK:                           '`';
INHERITANCE_SYMBOL:                 '<:';
CURVE_BRACKET_OPEN:                 '{';
CURVE_BRACKET_CLOSE:                '}';
SEMI_SYMBOL:                        ';';
COLON_SYMBOL:                       ':';
EQUALS_SYMBOL:                      '=';
CONST:                              C O N S T;
PIPE_SYMBOL:                        '|';
PRIVATE:                            P R I V A T E;
PROTECTED:                          P R O T E C T E D;
PUBLIC:                             P U B L I C;
STATIC:                             S T A T I C;
COMMA_SYMBOL:                       ',';
SQUARE_BRACKET_OPEN:                '[';
SQUARE_BRACKET_CLOSE:               ']';
STR_TYPE:                           S T R;
INT_TYPE:                           I N T;
FLOAT_TYPE:                         F L O A T;
BOOL_TYPE:                          B O O L;
VOID_TYPE:                          V O I D;
NULL_TYPE:                          N U L L;
ANY_TYPE:                           A N Y;
ID:                                 [a-zA-Z_][a-zA-Z_0-9]*;
STRING_VALUE:                       '"' ~'"'*  '"';


fragment A: [aA];
fragment B: [bB];
fragment C: [cC];
fragment D: [dD];
fragment E: [eE];
fragment F: [fF];
fragment G: [gG];
fragment H: [hH];
fragment I: [iI];
fragment J: [jJ];
fragment K: [kK];
fragment L: [lL];
fragment M: [mM];
fragment N: [nN];
fragment O: [oO];
fragment P: [pP];
fragment Q: [qQ];
fragment R: [rR];
fragment S: [sS];
fragment T: [tT];
fragment U: [uU];
fragment V: [vV];
fragment W: [wW];
fragment X: [xX];
fragment Y: [yY];
fragment Z: [zZ];

ERROR: .;