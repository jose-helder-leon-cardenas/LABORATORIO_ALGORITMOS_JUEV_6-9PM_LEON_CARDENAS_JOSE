"""str1 = "PYTHON"
output = [chr(ord(char)-5) for char in str1]
print("" .join(output))"""

####################

"""cad = " Hola, cómo estás?"

print("hola" in cad)  # FALSE
print("como" not in cad) # TRUE
"""

################

objetivo_secreto = "manzana", "pera", "platano"
  # Este es el objeto que el jugador debe adivinar
max_intentos = 3  # El jugador tiene 3 intentos para adivinar el objeto

def adivinar():

    for i in range(max_intentos):
        
        adivinanza = input("Introduce tu adivinanza: ")
        if adivinanza == objetivo_secreto[0]:
            print("¡Has ganado!")
        if adivinanza == objetivo_secreto[1]:
            print("¡Has ganado!")
        if adivinanza == objetivo_secreto[2]:
            print("¡Has ganado!")
            break
    else:
        print("Has perdido. El objeto secreto era: ", objetivo_secreto)

print(adivinar())

#######################

def procesar_frase(frase):
    palabras = frase.lower().split()
    palabras_unicas = []
    palabras_repetidas = set()

    for palabra in palabras:
        if palabras.count(palabra) > 1:
            palabras_repetidas.add(palabra)
        if palabra not in palabras_unicas:
            palabras_unicas.append(palabra)
    return (palabras_unicas, palabras_repetidas)

frase = "the cat is the hat IS in the"
print(procesar_frase(frase))









objetivo_secreto = ["manzana", "pera", "platano"]
intentos = 3

for i in range(intentos):
    entrada = input("Por favor, ingresa una palabra clave: ")
    if entrada.lower() in objetivo_secreto:
        print("¡Has acertado!")
        break
    else:
        print("Esa no es la palabra clave. Te quedan", intentos - i - 1, "intentos.")
else:
    print("Lo siento, has agotado tus intentos.")



























