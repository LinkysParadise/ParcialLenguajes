grammar CalcTrig;

prog:   stat+ ;

stat:   function                   # printExpr                  
    ;


function: SIN '(' num ')'          # SinFunction
        | COS '(' num ')'          # CosFunction
        | TAN '(' num ')'          # TanFunction
        ;

num:  INT  #int
    ;
SIN     : 'sin' ;
COS     : 'cos' ;
TAN     : 'tan' ;
INT     : [0-9]+ ;                          
WS      : [ \t\n\r]+ -> skip ;              
