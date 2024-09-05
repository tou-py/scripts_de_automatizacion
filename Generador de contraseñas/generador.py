import secrets
import string


def generador(longitud: int) -> str:
    abcdario = string.ascii_letters + string.digits + "!@#$%&/()=+?[]~-_^"
    pwd = "".join(secrets.choice(abcdario) for i in range(longitud))
    return pwd


def almacenador(sitio: str, pwd: str) -> None:
    try:
        with open("pwds.txt", "a", encoding="utf-8") as file:
            file.write(f"{sitio}: {pwd}")
            file.write("\n")
        print("Guardado con exito!")
    except Exception as ex:
        print(f"No se pudo guardar. {ex}")


nombre = input("La contraseña es para (sitio, pagina, etc.):")
long = int(input("Elija la longitud de su contraseña: "))
while True:
    if long < 4 or long > 33:
        long = int(
            input(
                "La contraseña debe tener un minimo de 4 y un maximo de 32 digitos, intente de nuevo: "
            )
        )
    else:
        break

pwd = generador(long)
almacenador(sitio=nombre, pwd=pwd)
