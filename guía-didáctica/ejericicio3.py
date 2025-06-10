""" Ejercicio 3: Generador de Listas de Compras
• Problema: Crea un programa que permita al usuario crear una lista de compras. El programa
solicitará al usuario que ingrese productos uno por uno y los guardará en un archivo llamado
compras.txt. El usuario indicará que ha terminado de añadir productos introduciendo la
palabra "fin".
• Paso a paso:
1. Abrir el archivo compras.txt en modo de escritura ('w') para iniciar una nueva lista.
2. Crear un bucle infinito (while True).
3. Dentro del bucle, pedir al usuario que ingrese un producto.
4. Comprobar si la entrada del usuario es "fin". Si lo es, romper el bucle.
5. Si no es "fin", escribir el producto en el archivo, seguido de un salto de línea (\n).
6. Una vez que el bucle termina, cerrar el archivo y notificar al usuario que la lista ha
sido guardada. """

my_ruta = "C:\\Users\\lcrf_\\OneDrive\\Desktop\\UAM\\Introducción a la programación\\Repositorios de git\\IntroProg2-S12\\archivostxt\\"
mi_archivo = open(my_ruta + "compras.txt", "w")
print("Bienvenido al generador de listas de compras.")
while True:
    productoUsuario = input("Introduce un producto (o escribe 'fin' para terminar): ")
    if productoUsuario.lower() == "fin":
        print("Lista de compras guardada.")
        break
    elif productoUsuario.strip() == "":
        print("No se puede añadir un producto vacío. Por favor, introduce un nombre de producto.")
    else:
        mi_archivo.write(productoUsuario + "\n")