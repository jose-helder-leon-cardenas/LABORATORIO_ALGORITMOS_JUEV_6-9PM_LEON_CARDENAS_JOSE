import random
import string


longitud=input("ingrese la longitud de la contaseña que se va generar:")
def generar_contrasena():
    return ''.join(random.sample(string.ascii_letters + string.digits + "!@#$%^&*()", int(longitud)))

print(generar_contrasena())

"""
def generar_contrasena(longitud):
    if longitud < 8:
        return "La longitud de la contraseña debe ser al menos de 8 caracteres."

    todos_los_caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = [random.choice((string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation)[i % 4]) for i in range(longitud)]
    random.shuffle(contrasena)

    return ''.join(contrasena)

print(generar_contrasena(10))

"""
#
#print("los caracteres que se va usar son : ")
#caracteres = string.ascii_letters + string.digits + string.punctuation
#print(caracteres)
#
#def generar_contras_aleatoria(long):
#    contrasena = ''
#
#    while len(contrasena) < long :
#        caracter = random.choice(caracteres)
#        contrasena += caracter
#
#        """if caracter.isupper():
#            tiene_mayuscula = True
#        elif caracter.islower():
#            tiene_minuscula = True
#        elif caracter.isdigit():
#            tiene_numero = True
#        elif not caracter.isalnum():
#            tiene_caracter_especial = True"""
#
#long = int(input("ingresa un numero para generar una contraseña con esa longitud : "))
#contrasena = generar_contras_aleatoria(long)
#print(contrasena)


############################################################################

"""
import string
import random

def generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales):
    caracteres = ""
    if mayusculas: caracteres += string.ascii_uppercase
    if minusculas: caracteres += string.ascii_lowercase
    if numeros: caracteres += string.digits
    if especiales: caracteres += string.punctuation

    if not caracteres or longitud <= 0:
        raise ValueError("Parámetros inválidos")

    return ''.join(random.choice(caracteres) for _ in range(longitud))

def main():
    try:
        longitud = int(input("Longitud de la contraseña: "))
        mayusculas = input("Incluir mayúsculas (si/no): ").lower() == 'si'
        minusculas = input("Incluir minúsculas (si/no): ").lower() == 's'
        numeros = input("Incluir números (s/n): ").lower() == 's'
        especiales = input("Incluir caracteres especiales (s/n): ").lower() == 's'

        contrasena = generar_contrasena(longitud, mayusculas, minusculas, numeros, especiales)
        print(f"Contraseña generada: {contrasena}")

    except ValueError:
        print("Entrada inválida. Por favor, ingrese valores válidos.")

if __name__ == "__main__":
    main()"""
