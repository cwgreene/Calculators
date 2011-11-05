import ply.lex as lex

reserved = {r'forall':'FORALL',
            r'exists':'EXISTS'}

tokens = ['SYMBOL','LPAREN','RPAREN','COMMA']+list(reserved.values())+['NOT','IMPLIES','EQUIV','EQUALS','OR','AND']

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_COMMA = r','
t_NOT = r'!'
t_IMPLIES = r'->'
t_EQUIV = r'<=>'
t_OR    = r'\|'
t_AND    = r'\&'

def t_SYMBOL(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'SYMBOL')    # Check for reserved words
    return t

def t_error(t):
    print "Illegal character '%s'" % t.value[0],"in",t

t_ignore = ' \t'

lexer = lex.lex()

def parse_tokens():
    while True:
        try:
            lexer.input(raw_input())
            while True:
                tok = lexer.token()
                if not tok: break
                print tok
        except lex.LexError,e:
            print e
        except EOFError:
            break

if __name__=='__main__':
    parse_tokens()
