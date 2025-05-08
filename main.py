import analizador_lexico
import analizador_sintactico

def main():
    nombre_archivo = input("Ingresa el nombre del archivo fuente (.py): ").strip()
    
    print("\nEjecutando analizador léxico...")
    analizador_lexico.analizar_codigo_fuente(nombre_archivo)

    print("Ejecutando analizador sintáctico...")
    analizador_sintactico.analizar_tokens("tokens.txt")

if __name__ == "__main__":
    main()
