mi_ruta = "C:\\Users\\lcrf_\\OneDrive\\Desktop\\UAM\\Introducción a la programación\\Repositorios de git\\IntroProg2-S12\\archivostxt\\"

mi_archivo = open(mi_ruta + "datos.txt", "w")

texto = input("Dime algo: ")
mi_archivo.write(texto)
mi_archivo.close()