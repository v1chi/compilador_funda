import ply.yacc as yacc
from lexer import tokens 

# programa general
def p_program(p):
    '''program : declarations'''
    p[0] = p[1]

# una declaracion o muchas en el programa, son como las lineas
def p_declarations(p):
    '''declarations : declaration
                    | declarations declaration'''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[2]]

# para declarar general, funciones, when, loop etc etc
def p_declaration(p):
    '''declaration : variable_declaration
                   | function_declaration
                   | conditional
                   | loop
                   | output'''
    p[0] = p[1]

# declarar variablem: number decimal o text
def p_variable_declaration(p):
    '''variable_declaration : INTEGER_TYPE ID ASSIGN expression SEMI
                            | FLOAT_TYPE ID ASSIGN expression SEMI
                            | STRING_TYPE ID ASSIGN TXT SEMI'''
    p[0] = ('declare', p[1], p[2], p[4])


# declarar funcion, con o sin return
def p_function_declaration(p):
    '''function_declaration : FUNCTION ID LPAREN parameters RPAREN LBRACE declarations return_statement RBRACE
                            | FUNCTION ID LPAREN parameters RPAREN LBRACE declarations RBRACE'''
    if len(p) == 10:  # Caso con return_statement
        p[0] = ('function', p[2], p[4], p[7], p[8])  # Separar declaraciones y return_statement
    else:  # Caso sin return_statement
        p[0] = ('function', p[2], p[4], p[7], None)


# define parametros de una funcion
def p_parameters(p):
    '''parameters : parameter
                  | parameters COMA parameter
                  | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] is not None else []
    else:
        p[0] = p[1] + [p[3]]

# parametro de funcion, tipo
def p_parameter(p):
    '''parameter : INTEGER_TYPE ID
                 | FLOAT_TYPE ID
                 | STRING_TYPE ID'''
    p[0] = (p[1], p[2])

# return de funciones
def p_return_statement(p):
    '''return_statement : RETURN expression SEMI'''
    p[0] = ('return', p[2])

# condicional when
def p_conditional(p):
    '''conditional : WHEN logical_expression LBRACE declarations RBRACE ELSE LBRACE declarations RBRACE
                   | WHEN logical_expression LBRACE declarations RBRACE'''
    if len(p) == 9:
        p[0] = ('if_else', p[2], p[4], p[8])
    else:
        p[0] = ('if', p[2], p[4])

# bucle loop
def p_loop(p):
    '''loop : LOOP ID LPAREN expression COMA expression RPAREN LBRACE declarations RBRACE'''
    p[0] = ('loop', p[2], p[4], p[6], p[9])

# print en este caso out
def p_output(p):
    '''output : OUT expression SEMI
              | OUT TXT SEMI'''
    p[0] = ('out', p[2])

# suma, resta, llamar funcion, 1 solo termino: para out
def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | function_call'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '+':
        p[0] = ('add', p[1], p[3])
    elif p[2] == '-':
        p[0] = ('subtract', p[1], p[3])

# como se llama a una funcion
def p_function_call(p):
    '''function_call : ID LPAREN arguments RPAREN'''
    p[0] = ('call', p[1], p[3])

# los argumentos de una funcion, como se separan (por coma)
def p_arguments(p):
    '''arguments : expression
                 | arguments COMA expression
                 | empty'''
    if len(p) == 2:
        p[0] = [p[1]] if p[1] is not None else []
    else:
        p[0] = p[1] + [p[3]]

# multiplicar, dividir, modulo
def p_term(p):
    '''term : factor
            | term TIMES factor
            | term DIVIDE factor
            | term MOD factor'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '*':
        p[0] = ('multiply', p[1], p[3])
    elif p[2] == '/':
        p[0] = ('divide', p[1], p[3])
    elif p[2] == '%':
        p[0] = ('mod', p[1], p[3])

# factor para operaciones
def p_factor(p):
    '''factor : NUM
              | DEC
              | ID
              | LPAREN expression RPAREN'''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]

# comparaciones mayor que menor que e igual
def p_comparison(p):
    '''comparison : expression GT expression
                  | expression LT expression
                  | expression EQ expression'''
    if p[2] == '>':
        p[0] = ('>', p[1], p[3])
    elif p[2] == '<':
        p[0] = ('<', p[1], p[3])
    elif p[2] == '==':
        p[0] = ('==', p[1], p[3])

# operaciones logicas, o y 
def p_logical_expression(p):
    '''logical_expression : comparison
                          | logical_expression OR comparison
                          | logical_expression AND comparison'''
    if len(p) == 2:
        p[0] = p[1]
    elif p[2] == '||':
        p[0] = ('or', p[1], p[3])
    elif p[2] == '&&':
        p[0] = ('and', p[1], p[3])

# vacio
def p_empty(p):
    'empty :'
    pass

# manejar errores sintacticos
def p_error(p):
    if p:
        print(f"Error de sintaxis en el token '{p.value}'")
    else:
        print("Error de sintaxis en la entrada")

# orden de operaciones
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'NOT'),
    ('left', 'GT', 'LT', 'EQ'),
    ('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIVIDE', 'MOD'),
)

parser = yacc.yacc()

"""
# testear parser
testea = '''
    function calcular(number x, number y) {
        number sum = x + y;
        out sum;
        return sum;
    }

    number result = calcular(a, b);
'''
result = parser.parse(testea)
print(result)
"""