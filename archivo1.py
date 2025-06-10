try: 
    mi_ruta = "C:\\Users\\lcrf_\\OneDrive\\Desktop\\UAM\\Introducción a la programación\\Repositorios de git\\IntroProg2-S12\\archivostxt\\"
    mi_archivo = open (mi_ruta + "datos.txt", "r")
    contenido = mi_archivo.read()
    print(contenido)
    mi_archivo.close
except FileNotFoundError:
    print("El archivo no se encuentra en la ruta especificada.")