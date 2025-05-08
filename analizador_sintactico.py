def analizar_tokens(nombre_archivo):
    errores = []
    pila_parentesis = []
    pila_corchetes = []

    try:
        with open(nombre_archivo, 'r') as archivo:
            lineas = archivo.readlines()
    except FileNotFoundError:
        print(f"No se encontró el archivo '{nombre_archivo}'")
        return

    tokens = []
    for linea in lineas:
        if "Error" in linea:
            errores.append(linea.strip())
            continue
        partes = linea.strip()[1:-1].split(',')
        if len(partes) != 4:
            errores.append(f"<0,0> Error de formato: {linea.strip()}")
            continue
        tipo, valor, fila, columna = partes
        tokens.append((tipo.strip(), valor.strip(), int(fila), int(columna)))

    i = 0
    while i < len(tokens):
        tipo, valor, fila, columna = tokens[i]

        # Verificar estructuras con dos puntos
        if tipo in {"if", "for", "while", "def"}:
            tiene_dos_puntos = False
            for j in range(i+1, len(tokens)):
                t, v, f, c = tokens[j]
                if f > fila:
                    break
                if t == "dos_puntos":
                    tiene_dos_puntos = True
                    break
            if not tiene_dos_puntos:
                errores.append(f"<{fila},{columna}> Error sintáctico: se esperaba ':' después de '{valor}'")

        # Verificar llamada sin paréntesis
        if tipo in {"print", "input", "id"}:
            if i + 1 < len(tokens):
                siguiente_tipo, _, _, _ = tokens[i + 1]
                if siguiente_tipo in {"cadena", "numero", "id"}:
                    errores.append(f"<{fila},{columna}> Error sintáctico: se esperaba '(' después de '{valor}' para llamada a función")

        # Seguimiento de paréntesis
        if tipo == "par_izq":
            pila_parentesis.append((fila, columna))
        elif tipo == "par_der":
            if pila_parentesis:
                pila_parentesis.pop()
            else:
                errores.append(f"<{fila},{columna}> Error sintáctico: paréntesis de cierre ')' sin apertura")

        # Seguimiento de corchetes
        if tipo == "cor_izq":
            pila_corchetes.append((fila, columna))
        elif tipo == "cor_der":
            if pila_corchetes:
                pila_corchetes.pop()
            else:
                errores.append(f"<{fila},{columna}> Error sintáctico: corchete de cierre ']' sin apertura")

        i += 1

    for fila, columna in pila_parentesis:
        errores.append(f"<{fila},{columna}> Error sintáctico: paréntesis '(' sin cerrar")
    for fila, columna in pila_corchetes:
        errores.append(f"<{fila},{columna}> Error sintáctico: corchete '[' sin cerrar")

    with open("salida.txt", "w") as archivo:
        archivo.write("Resultado del análisis:\n")
        if errores:
            for e in errores:
                archivo.write(e + "\n")
        else:
            archivo.write("El análisis sintáctico ha finalizado exitosamente.\n")

    print("\nResultado del análisis:")
    if errores:
        for e in errores:
            print(e)
    else:
        print("El análisis sintáctico ha finalizado exitosamente.")
