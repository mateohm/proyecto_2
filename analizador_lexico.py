import re

def analizar_codigo_fuente(nombre_archivo):
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    patrones = [
        ("numero", r"\d+"),
        ("id", r"[a-zA-Z_][a-zA-Z_0-9]*"),
        ("igual", r"="),
        ("suma", r"\+"),
        ("resta", r"-"),
        ("multiplicacion", r"\*"),
        ("division", r"/"),
        ("coma", r","),
        ("punto", r"\."),
        ("dos_puntos", r":"),
        ("par_izq", r"\("),
        ("par_der", r"\)"),
        ("cor_izq", r"\["),
        ("cor_der", r"\]"),
        ("mayor", r">"),
        ("menor", r"<"),
        ("igualdad", r"=="),
        ("diferente", r"!="),
        ("cadena", r"\".*?\"|'.*?'"),
        ("espacio", r"[ \t]+"),
        ("nueva_linea", r"\n")
    ]

    palabras_reservadas = {"if", "else", "for", "while", "def", "print", "in", "return"}

    tokens = []
    for fila, linea in enumerate(lineas, start=1):
        columna = 1
        while linea:
            coincidencia = None
            for tipo, patron in patrones:
                regex = re.compile(patron)
                coincidencia = regex.match(linea)
                if coincidencia:
                    lexema = coincidencia.group(0)
                    if tipo == "espacio":
                        columna += len(lexema)
                    elif tipo != "nueva_linea":
                        if tipo == "id" and lexema in palabras_reservadas:
                            tipo = lexema
                        tokens.append(f"<{tipo},{lexema},{fila},{columna}>")
                        columna += len(lexema)
                    linea = linea[len(lexema):]
                    break
            if not coincidencia:
                tokens.append(f"<Error,{linea[0]},{fila},{columna}>")
                linea = linea[1:]
                columna += 1

    with open("tokens.txt", "w") as archivo:
        for token in tokens:
            archivo.write(token + "\n")

    print("Tokens guardados en 'tokens.txt'")
