# Documentación del Compilador

## Integrantes: María Victoria Quiroga y Constanza Vazquez

## Descripción de la Gramática del Lenguaje

Gramática utilizada:

1. **Declaraciones**:
   - **Declaración de variables**: Permite declarar variables tipo `number` (entero), `decimal`(float) y `text`(string).
   - **Declaración de funciones**: Define funciones con parámetros y un cuerpo de declaraciones (function).
   - **Condicionales**: Utiliza `when` para evaluar condiciones y `else` para manejar el caso contrario.
   - **Bucles**: Utiliza `loop` para iterar sobre un rango de valores.
   - **Salida**: Utiliza `out` para imprimir valores.

2. **Expresiones**:
   - **Aritméticas**: Soporta suma, resta, multiplicación, división y módulo.
   - **Lógicas**: Soporta comparaciones (`>`, `<` y `==`) y operaciones lógicas (`and` y `or`).

3. **Llamadas a funciones**:
   - Permite llamar a funciones con argumentos.

## Explicación de la Estructura Interna del Compilador

1. **Análisis Léxico**:
   - **Lexer**: Utilizamos `ply.lex` para definir el lexer. Este se encarga de convertir el código fuente en una lista de tokens. 

2. **Análisis Sintáctico**:
   - **Parser**: Utilizamos `ply.yacc` para definir el parser. Este se encarga de analizar la estructura gramatical del código fuente utilizando las reglas. Este construye un árbol de sintaxis abstracta (AST) que representa la estructura del programa.

3. **Interpreter**:
   - Ejecuta el código representado por el AST, para manejar la declaración, evaluación y ejecución de variables y funciones.

## Sintaxis del Compilador

### Declaración de Variables

- **Número Entero**:
  number x = 5;

- **Número Decimal**:
  decimal y = 3.14;


- **Texto**:
text saludo = "Hola Mundo";


- **Declaración de Funciones**:
function suma(number a, number b) {
    number resultado = a + b;
    return resultado;
}

Las variables utilizadas en la función tienen que ser pasadas como parámetros o declaradas dentro de la misma.

- **Llamada a Funciones**:
number resultado = suma(10, 20);


- **Condicional when**:
when resultado > 20 {
    out "El resultado es mayor que 20";
} else {
    out "El resultado es 20 o menor";
}


- **Bucle For**:
number i = 0;
loop i (1, 10) {
    out i;
}

En este caso la variable i parte siendo 1 y va aumentando de 1 en 1 hasta llegar a 10, i siempre tiene que declararse e inicializarse antes de la sentencia loop

- **Salida de Datos**:
out resultado;
