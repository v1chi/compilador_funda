import ply.yacc as yacc
from lexer import tokens
from parser import parser
from interpreter import Environment, execute_declarations

def testear(archivo):
    with open(archivo, 'r') as file:
        data = file.read()
    resultado = parser.parse(data)
    print("Resultado:")
    env = Environment()
    execute_declarations(resultado, env)

archivos_prueba = ['test1.txt', 'test2.txt', 'test3.txt', 'test4.txt']

for test_file in archivos_prueba:
    print(f"Probando archivo: {test_file}")
    testear(test_file)
    print("\n")