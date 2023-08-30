import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation

def generar_contrasena(longitud):
    contrasena = ''
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    tiene_caracter_especial = False

    while len(contrasena) < longitud or not (tiene_mayuscula and tiene_minuscula and tiene_numero and tiene_caracter_especial):
        caracter = random.choice(caracteres)
        contrasena += caracter

        if caracter.isupper():
            tiene_mayuscula = True
        elif caracter.islower():
            tiene_minuscula = True
        elif caracter.isdigit():
            tiene_numero = True
        elif not caracter.isalnum():
            tiene_caracter_especial = True

    return contrasena

longitud = int(input("ingresa un numero para generar una contraseña con esa longitud : "))
contrasena = generar_contrasena(longitud)
print(contrasena)
