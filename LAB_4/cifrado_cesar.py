

"""def cifrar_cesar(letra, desplazamiento):
    mensaje_cifrado = ''
    for letra in mensaje:
        if letra.isalpha():
            mayuscula = letra.isupper()
            letra = letra.lower()
            indice = ord(letra) - ord('a')
            indice_cifrado = (float(indice) + desplazamiento) % 26
            letra_cifrada = chr(ord('a') + indice_cifrado)
            if mayuscula:
                letra_cifrada = letra_cifrada.upper()
            mensaje_cifrado += letra_cifrada
        else:
            mensaje_cifrado += letra
    return mensaje_cifrado

mensaje = input("ingrese el mensaje a cifrar con el método cesar : ")
desplazamiento = input("cuantos espacios o caracteres quieres que se despalze : ")

# Cifrar el mensaje original
mensaje_cifrado = ''
for letra in mensaje:
    mensaje_cifrado += cifrar_cesar(letra, desplazamiento)

print("Mensaje cifrado:", mensaje_cifrado)"""


"""
texto=input ("tu texto:  ")


if texto==texto.upper ():
    abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ" #PARA MAYUSCULAS
else:
      abc="abcdefghijklmnñopqrstuvwxyz" #PARA MINUSCULAS

desplazamiento = int (input ("Valor de desplazamiento: "))
cifrado=""

#CREAMOS CADENA DE CARÁCTERES

if texto==texto.upper () : #PARA MAYUSCULAS

      abc="ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

else:

      abc="abcdefghijklmnñopqrstuvwxyz" #PARA MINUSCULAS

#REALIZAMOS CIFRADO.
for c in texto:
 if c in abc:
      cifrado += abc[(abc.index(c)+k%(len(abc))]
 else:
     cifrad+=c

print("texto cifrado: ",cifrado)"""

# Cifrado César
mensaje_original = input("ingrese el mensaje a cifrar con el método cesar : ")  #Hola, esto es un ejemplo de cifrado Cesar!
desplazamiento = 3

# Función para cifrar una letra
def cifrar_letra(letra, desplazamiento):
    if letra.isalpha():
        mayuscula = letra.isupper()
        letra = letra.lower()
        indice = ord(letra) - ord('a')
        indice_cifrado = (indice + desplazamiento) % 26
        letra_cifrada = chr(ord('a') + indice_cifrado)
        if mayuscula:
            letra_cifrada = letra_cifrada.upper()
        return letra_cifrada
    else:
        return letra

# Cifrar el mensaje original
mensaje_cifrado = ''
for letra in mensaje_original:
    mensaje_cifrado += cifrar_letra(letra, desplazamiento)

print("Mensaje cifrado:", mensaje_cifrado)

"""# Descifrar el mensaje cifrado
mensaje_descifrado = ''
for letra in mensaje_cifrado:
    mensaje_descifrado += cifrar_letra(letra, -desplazamiento)

print("Mensaje descifrado:", mensaje_descifrado)"""





