grammar CalcTrig;

prog:   stat+ ;

stat:   expr                        # printExpr
    ;

expr:   SIN '(' expr ')'            # SinFunction
    |   COS '(' expr ')'            # CosFunction
    |   TAN '(' expr ')'            # TanFunction
    |   INT                         # int
    ;

INT     : [0-9]+ ;                          // match integers
WS      : [ \t]+ -> skip ;
SIN     : 'sin' ;
COS     : 'cos' ;
TAN     : 'tan' ;