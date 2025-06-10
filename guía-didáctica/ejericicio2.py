""" Ejercicio 2: Contador de Líneas
• Problema: Desarrolla un programa que pida al usuario el nombre de un archivo de texto. El
programa deberá leer el archivo y mostrar en pantalla el número total de líneas que contiene.
Debe manejar el error en caso de que el archivo no exista.
• Paso a paso:
1. Solicitar al usuario el nombre del archivo (ej: poema.txt).
2. Usar un bloque try...except para manejar la excepción FileNotFoundError.
3. Dentro del try, abrir el archivo en modo lectura ('r').
4. Utilizar el método readlines() para leer todas las líneas en una lista.
5. Calcular la longitud de la lista (que es igual al número de líneas) y mostrarla.
6. En el bloque except, si el archivo no se encuentra, imprimir un mensaje de error
amigable.
"""
try:
    mi_ruta = "C:\\Users\\lcrf_\\OneDrive\\Desktop\\UAM\\Introducción a la programación\\Repositorios de git\\IntroProg2-S12\\archivostxt\\"
    leerArchivo = input("Introduce el nombre del archivo (ej: poema.txt): ")
    mi_archivo = open(mi_ruta + leerArchivo, "r")
    mostrar = mi_archivo.readlines()
    print("=" * 50)
    print(f"Contenido del archivo {leerArchivo}:")
    print(f" ".join(mostrar))
    print("=" * 50)
    contarLineas = len(mostrar)
    print(f"El archivo {leerArchivo} contiene {contarLineas} líneas.")
    
except FileNotFoundError:
    print(f"Error: El archivo {leerArchivo} no se encuentra en la ruta especificada o el nombre es incorrecto.")