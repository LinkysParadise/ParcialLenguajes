grammar CalcTrig;

// Define the main program
prog:   stat+ ;

// Define statements
stat:   function                        # printExpr                  
    ;


function: SIN '(' INT ')'          # SinFunction
        | COS '(' INT ')'          # CosFunction
        | TAN '(' INT ')'          # TanFunction
        ;

SIN     : 'sin' ;
COS     : 'cos' ;
TAN     : 'tan' ;
INT     : [0-9]+ ;                          
WS      : [ \t\n\r]+ -> skip ;              
