import ply.lex as lex
import ply.yacc as yacc
import sys
import math
tokens = [
    'INT',
    'FLOAT',
    'NAME',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'EQUALS',
    'UP',
    'OPEN',
    'CLOSE',
    'FACTORIAL',
    'SIN',
    'COS',
    'TAN',
    'LOG',
    'NATURAL',
    'EXP',
    'SQUARE',
    'EULER',
    'PI'
    ]
#Análisis léxico de simbolos
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'\/'
t_MULTIPLY = r'\*'
t_EQUALS = r'\='
t_UP = r'\^'
t_OPEN = r'\('
t_CLOSE = r'\)'
t_FACTORIAL = r'\!'
t_ignore = r' '

#Análisis léxico con palabras

def t_EULER(t):
    r'e'
    t.value = math.e
    return t

def t_PI(t):
    r'pi'
    t.value = math.pi
    return t

def t_SIN(t):
    r'sin'
    t.type = 'SIN'
    return t

def t_COS(t):
    r'cos'
    t.type = 'COS'
    return t

def t_LOG(t):
    r'log'
    t.type = 'LOG'
    return t

def t_NATURAL(t):
    r'ln'
    t.type = 'NATURAL'
    return t
def t_SQUARE(t):
    r'sqrt'
    t.type = 'SQUARE'
    return t

def t_EXP(t):
    r'EXP'
    t.type = 'EXP'
    return t

def t_TAN(t):
    r'tan'
    t.type = 'TAN'
    return t

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Caracteres invalidos")
    t.lexer.skip(1)


lexer = lex.lex()

precedence = (

    ('left', 'PLUS', 'MINUS'),
    ('left', 'MULTIPLY', 'DIVIDE')

)
#Acá se añade la entrada a descomponer
lexer.input("")

while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
    

#------------------------------------------------------------------------------#
    
#Parser
def p_calc(p):
    '''
    calc : expression
         | empty
    '''
    print(p[1])

def p_expression_s_r_m_d(p):
    '''
    expression : expression MULTIPLY expression
               | expression DIVIDE expression 
               | expression PLUS expression
               | expression MINUS expression 
               | expression EXP expression
    '''
    #print(eval(str(p[1])+str(p[2])+str(p[3])))
    p[0] = (p[2], p[1], p[3])
    print (p[0])
    p[0] = eval(str(p[1])+str(p[2])+str(p[3]))

def p_expression_fact_pi(p):
    '''
    expression : expression FACTORIAL
               | expression MULTIPLY PI
    '''
    p[0] = (p[1], p[2])


def p_expression_trigonometria_log_exp_sqrt(p):
    '''
    expression : SIN OPEN expression CLOSE
               | COS OPEN expression CLOSE
               | TAN OPEN expression CLOSE
               | LOG OPEN expression CLOSE
               | SQUARE OPEN expression CLOSE
               | EULER OPEN expression CLOSE
               
    '''
    p[0] = (p[1], p[3])
    
def p_expression_log_natural(p):
    '''
    expression : LOG NATURAL OPEN expression CLOSE
    '''
    p[0] = (p[1],p[2],p[4])

def p_expression_int_float(p):
     '''
     expression : INT
                | FLOAT
     '''
     p[0] = p[1]

def p_empty(p):
    
    '''
    empty : 
    '''
    p[0] = None

def p_error(p):
    print("Syntax error found!")

"""
parser = yacc.yacc()

while True:
    try:
        s = input("calc >> ")
    except EOFError:
        break
    result = parser.parse(s)

"""
#Gabo tocó aquí
def calculate(s):
    parser = yacc.yacc()
    parser.parse(s)
    print(s)
    return eval(str(s))

    
