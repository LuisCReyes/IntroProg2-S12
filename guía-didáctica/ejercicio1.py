""" Ejercicio 1: Diario Personal
• Problema: Escribe un programa que funcione como un diario simple. Cada vez que se
ejecute, debe solicitar al usuario una entrada de texto y la guardará, junto con la fecha y hora
actual, en un archivo llamado diario.txt. Cada nueva entrada debe añadirse al final del
archivo sin borrar las anteriores.
• Paso a paso:
1. Importar el módulo datetime para obtener la fecha y hora.
2. Solicitar al usuario que ingrese el texto para su entrada del diario.
3. Abrir el archivo diario.txt en modo de adición ('a').
4. Escribir la fecha y hora actual, seguida de la entrada del usuario. Asegurarse de
añadir un salto de línea para separar las entradas.
5. Cerrar el archivo.
6. Mostrar un mensaje de confirmación al usuario
"""
import datetime

try:
    mi_ruta = "C:\\Users\\lcrf_\\OneDrive\\Desktop\\UAM\\Introducción a la programación\\Repositorios de git\\IntroProg2-S12\\archivostxt\\"
    mi_archivo = open(mi_ruta + "diario.txt", "a")
    
    texto = input("Escribe tu entrada del diario: \n")
    ahora = datetime.datetime.now()
    fecha = ahora.strftime("%d-%m-%Y")
    hora = ahora.strftime("%H:%M %p")
    mi_archivo.write(f"{fecha} a las {hora}:\n {texto}\n")
    mi_archivo.close()
except FileNotFoundError:
    print("Error: El archivo diario.txt no se encuentra en la ruta especificada.")