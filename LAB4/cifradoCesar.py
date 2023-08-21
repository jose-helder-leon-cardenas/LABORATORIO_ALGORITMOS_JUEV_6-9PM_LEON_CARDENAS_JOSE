mensaje_original = input("ingrese el mensaje a cifrar : ") #"Hola, esto es un ejemplo de cifrado Cesar!"
desplazamiento = 3

# Cifrar el mensaje original
mensaje_cifrado = ''
for letra in mensaje_original:
    if letra.isalpha():
        mayuscula = letra.isupper()
        letra = letra.lower()
        indice = ord(letra) - ord('a')
        indice_cifrado = (indice + desplazamiento) % 26
        letra_cifrada = chr(ord('a') + indice_cifrado)
        if mayuscula:
            letra_cifrada = letra_cifrada.upper()
        mensaje_cifrado += letra_cifrada
    else:
        mensaje_cifrado += letra

print("Mensaje cifrado:", mensaje_cifrado)

"""# Descifrar el mensaje cifrado
mensaje_descifrado = ''
for letra in mensaje_cifrado:
    if letra.isalpha():
        mayuscula = letra.isupper()
        letra = letra.lower()
        indice = ord(letra) - ord('a')
        indice_descifrado = (indice - desplazamiento) % 26
        letra_descifrada = chr(ord('a') + indice_descifrado)
        if mayuscula:
            letra_descifrada = letra_descifrada.upper()
        mensaje_descifrado += letra_descifrada
    else:
        mensaje_descifrado += letra

print("Mensaje descifrado:", mensaje_descifrado)"""