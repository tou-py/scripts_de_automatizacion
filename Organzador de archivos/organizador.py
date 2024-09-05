"""
# Organizador de archivos

Como su nobre indica es simplemente un organizador de archivos.
Es simple, al ejecutar el programa solicitará una url de la carpeta que deseas organizar, creará las carpetas correspodientes para todos los archivos, cada una con el nombre de las extensiones de estos, moverá todos a su carpeta correspondiente si es que esta existe, si no, la crea.
Solo ejecuta "python organizador.py" en la terminal y proveele una ruta que deseas organizar.

"""

import os
import shutil


def organizador(path: str) -> None:
    files = os.listdir(path)
    for file in files:
        filename, extension = os.path.splitext(file)
        extension = extension[1:]

        if extension:
            if os.path.exists(os.path.join(path, extension)):
                shutil.move(
                    os.path.join(path, file), os.path.join(path, extension, file)
                )
            else:
                os.makedirs(os.path.join(path, extension))
                shutil.move(
                    os.path.join(path, file), os.path.join(path, extension, file)
                )
    print("Carpeta ordenada con exito!")


carpeta = input("Ingrese la dirección completa de la carpeta: ")
while True:
    if os.path.exists(carpeta):
        organizador(carpeta)
        break
    else:
        carpeta = input("Dirección no válida, intente de nuevo: ")
