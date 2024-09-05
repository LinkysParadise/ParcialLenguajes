%{
#include <stdio.h>
%}
NUMBER [0-9]+
ID [a-zA-Z_][a-zA-Z0-9_]*
EQUAL_TK "="
POW_TK "**"
SUM_TK "+"
SUB_TK "-"
MULT_TK "*"
DIV_TK "/"
LAMBDA "lambda"

%%


{ID}" "?{EQUAL_TK}" "?{LAMBDA}" "{ID}":"({NUMBER}|{ID})" "?({POW_TK}|{SUM_TK}|{SUB_TK}|{MULT_TK}|{DIV_TK})" "?({NUMBER}|{ID})    { printf("ACEPTA\n"); }
.+        { printf("NO ACEPTA\n"); }

%%

int main(int argc, char **argv)
{
    if (argc > 1) {
        FILE *input = fopen(argv[1], "r");
        if (!input) {
            perror(argv[1]);
            return 1;
        }
        yyin = input;
        yylex();
        fclose(input);
    } else {
        yylex();
    }
    return 0;
}

int yywrap() {
    return 1;
}
