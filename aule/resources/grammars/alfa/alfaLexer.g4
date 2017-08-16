lexer grammar alfaLexer;

// ----
// SKIP
// ----
SPACE:              [ \t\r\n]+    -> skip;
COMMENT:            '/*' .*? '*/' -> channel(HIDDEN);
LINE_COMMENT:       '//' ~[\r\n]* -> channel(HIDDEN);

LESS_THAN:             '<';
MORE_THAN:             '>';
GREAT_EQUAL:           '>=';
LESS_EQUAL:            '<=';
EQUALS:                '==';
NOT_EQUALS:            '!=';
IN:                     I N;
SUBSET:                 S U B S E T;
SUBSETEQ:               S U B S E T E Q;

OPEN_BRACE:            '{'; 
CLOSE_BRACE:           '}'; 
OPEN_BRACKET:          '[';
CLOSE_BRACKET:         ']';
COMMA:                 ',';
OPEN_PAREN:            '(';
CLOSE_PAREN:           ')';

ANY:                    A N Y;
EXPORT:                 E X P O R T;
NAMESPACE:              N A M E S P A C E;
POLICYSET:              P O L I C Y S E T;
POLICY:                 P O L I C Y;
RULE:                   R U L E;
APPLY:                  A P P L Y;
PEMIT_OVERRIDES:        P E R M I T O V E R R I D E S;
DENY_OVERRIDES:         D E N Y O V E R R I D E S;
FIRST_APPLICABLE:       F I R S T A P P L I C A B L E;
PERMIT_UNLESS_DENY:     P E R M I T U N L E S S D E N Y;
DENY_UNLESS_PERMIT:     D E N Y U N L E S S P E R M I T;
ONLY_ONE_APPLICABLE:    O N L Y O N E A P P L I C A B L E;
TARGET:                 T A R G E T;
TRUE:                   T R U E;
FALSE:                  F A L S E;
CLAUSE:                 C L A U S E;
CONDITION:              C O N D I T I O N;
OBLIGATION:             O B L I G A T I O N;
ADVICE:                 A D V I C E;
PERMIT:                 P E R M I T;
DENY:                   D E N Y;       
ON:                     O N;
OR:                     O R;
AND:                    A N D;
NOT:                    N O T;
DOT:                    '.';


STRING:          '"' ~('"'| '\\')* '"';

ID: ( 'a'..'z' | 'A'..'Z' | '_' ) ( 'a'..'z' | 'A'..'Z' | '_' | '0'..'9' )*;
INT: [0-9]+;


// -------
// Letters
// -------
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

// ----------------------------
// End. Catch not-defined cases
// ----------------------------
ERROR:      .;