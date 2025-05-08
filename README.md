# Proyecto 2

Este proyecto implementa un analizador léxico y sintáctico en Python que permite identificar errores en programas escritos en Python, sin usar bibliotecas externas como PLY, ANTLR, YACC.

El sistema está dividido en tres partes principales:

analizador_lexico.py: analiza el código fuente y genera los tokens.

analizador_sintactico.py: verifica la validez sintáctica de esos tokens.

main.py: orquesta la ejecución de los dos analizadores.

### 1. Analizador Lexico 

Lee un archivo .py.

Usa expresiones regulares para identificar tokens (números, operadores, identificadores, palabras clave, etc.).
Guarda los tokens en tokens.txt con el formato:

<tipo,valor,fila,columna>


### 2. Analizador Sintactico

Lee los tokens desde tokens.txt.

Detecta errores como:

- Falta de : después de if, for, while, def.

- Paréntesis o corchetes sin cerrar.

- Llamadas a funciones sin paréntesis.

Escribe el resultado del análisis en salida.txt con mensajes como:

<2,5> Error sintáctico: se esperaba ':' después de 'if'


### 3. main.py

Pide al usuario el nombre del archivo fuente.

Ejecuta el analizador léxico.

Luego ejecuta el analizador sintáctico.

Muestra en consola el contenido de salida.txt.


