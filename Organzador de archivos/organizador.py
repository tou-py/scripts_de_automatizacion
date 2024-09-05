import os
import shutil

path = input(r"Ingrese el directorio: ")
# path = r"C:\Users\sebas\Downloads"
files = os.listdir(path)

for file in files:
    filename, extension = os.path.splitext(file)
    extension = extension[1:]

    if os.path.exists(path + "/" + extension):
        shutil.move(f"{path}/{file}", f"{path}/{extension}/{file}")
    else:
        os.makedirs(f"{path}/{extension}")
        shutil.move(f"{path}/{file}", f"{path}/{extension}/{file}")
