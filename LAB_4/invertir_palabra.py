palabra = "Aprendiendo Python con Edem"

list_palabr = palabra.split()
#print(len(list_palabr))  # imprmiendo la lista de palabras

invert_lista = list_palabr[::-1]
invert_lista =" ".join(invert_lista)

print(invert_lista)