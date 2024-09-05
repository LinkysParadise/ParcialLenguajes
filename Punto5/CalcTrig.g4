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
WS      : [ \n\r\t]+ -> skip ;
SIN     : 'sin'|'Sin' ;
COS     : 'cos'|'Cos' ;
TAN     : 'tan'|'Tan' ;