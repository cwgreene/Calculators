from firstorder_lex import tokens

import ply.yacc as yacc
import traceback

#grammar
"""
sentence: predicate commutative_operator predicate | unary_operator predicate 
unary_operator : NOT
binary_operator : IMPLIES EQUIV 
pexpression : LPAREN expression RPAREN
sentence: pexpression binary_operator pexpression
expression: sentence | quantified_expression
quantified_expression : quantifier symbol_list expression
predicate: SYMBOL LPAREN symbol_list RPAREN
symbol_list: (SYMBOL COMMA)* SYMBOL
"""

def p_expression(p):
    """
    expression : sentence
               | quantified_expression
    """
    p[0] = p[1]


def p_sentence(p):
    """ 
    sentence : predicate
             | NOT predicate
             | NOT pexpression
             | LPAREN expression binary_operator expression RPAREN
             | pexpression
    """
    if len(p) == 2: #predicate
        p[0] = p[1]
    if len(p) == 3: #not predicate, expression
        p[0] = (p[1],p[2])
    if len(p) == 6: # x binop x
        p[0] = p[3],p[2],p[4]

def p_pexpression(p):
    """
    pexpression : LPAREN expression RPAREN
    """
    p[0] = p[2]

def p_predicate(p):
    """
    predicate : SYMBOL LPAREN symbol_list RPAREN
    """
    p[0] = (p[1],list(p[3]))

def p_symbol_list(p):
    """
    symbol_list : SYMBOL
                | SYMBOL COMMA symbol_list
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1]] + p[3]

def p_quantified_expression(p):
    """
    quantified_expression : quantifier symbol_list expression
    """
    p[0] = (p[1],p[2],p[3])

def p_quantifier(p):
    """ 
    quantifier : FORALL
               | EXISTS
    """
    p[0] = p[1]

def p_binary_operator(p):
    """
    binary_operator : OR
                    | AND
                    | EQUIV
                    | IMPLIES
    """
    print dir(p)
    p[0] = p[1]

yacc.yacc()
def parse_cfg():
    while True:
        try:
            while True:
                string = raw_input()
                ast = yacc.parse(string)
                if not ast: break
                print ast
        except EOFError:
            break
        except Exception,e:
            traceback.print_exc()
            raw_input()

if __name__=='__main__':
    parse_cfg()
