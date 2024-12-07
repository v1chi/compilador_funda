import ply.lex as lex

# palabras clave
reserved = {
    'function': 'FUNCTION',
    'out': 'OUT',
    'when': 'WHEN',
    'else': 'ELSE',
    'loop': 'LOOP',
    'number': 'INTEGER_TYPE', 
    'decimal': 'FLOAT_TYPE',   
    'text': 'STRING_TYPE', 
    'return': 'RETURN', 
    'lambda': 'LAMBDA', 
}

# todos los tokens, incluyendo palabras clave
tokens = (
    'NUM',    #  enteros
    'DEC',   #  decimales
    'TXT',      #  strings
    'PLUS',      
    'MINUS',     
    'TIMES',    
    'DIVIDE',    
    'MOD',       
    'ASSIGN',    
    'GT',        
    'LT',        
    'EQ',        
    'AND',       
    'OR',        
    'NOT',       
    'LPAREN',    
    'RPAREN',    
    'LBRACE',    
    'RBRACE',    
    'SEMI',      
    'COMA',      
    'ID'      
) + tuple(reserved.values())

# definicio de cada token
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_MOD     = r'%'
t_ASSIGN  = r'='
t_GT      = r'>'
t_LT      = r'<'
t_EQ      = r'=='
t_AND     = r'&&'
t_OR      = r'\|\|'
t_NOT     = r'!'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMA    = r','


def t_DEC(t):
    r'\d+\.\d+' 
    t.value = float(t.value)  
    return t


def t_NUM(t):
    r'\d+'
    t.value = int(t.value) 
    return t


def t_TXT(t):
    r'"([^\\"]|\\.)*"'  
    t.value = t.value[1:-1]  # eliminar comillas
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')  # ver si es una palabra reservada
    return t


# ignorar
t_ignore  = ' \t'

# saltar lineas o espacios
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f"Carácter ilegal '{t.value[0]}'")
    t.lexer.skip(1)

# lexer
lexer = lex.lex()


"""
# testeando lexer 
datos = '''
    number b = 5;
    decimal a = 10.5;
    text s = "Hola";
'''

lexer.input(datos)

# pasar a token
while True:
    tok = lexer.token()
    if not tok:
        break  
    print(tok)

"""