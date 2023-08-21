"""diccionario = {"a":1,"b":2, "c":3, "b":2,"e":3, "f":4}
valores_unicos = set(diccionario.values())

for valores in valores_unicos:
    print(valores)
"""
#################
# Aquí está un ejemplo de un diccionario con algunos valores duplicados
diccionario = {'a': 1, 'b': 2, 'c': 2, 'd': 3, 'e': 4, 'f': 4}

valores_unicos = []

for valor in diccionario.values():
    if valor not in valores_unicos:
        valores_unicos.append(valor)
        print(valor)


mi_diccionario = {"a1": "maria", "b1": "pedro", "c1": "maria", "d1": "paul"}

valores_unicos = []
valores_repetidos = []

# Identificar valores únicos y repetidos
for valor in mi_diccionario.values():
    if valor in valores_unicos:
        valores_repetidos.append(valor)
    else:
        valores_unicos.append(valor)

# Remover de la lista valores_unicos aquellos que se repiten
for valor in valores_repetidos: 
    while valor in valores_unicos:
        valores_unicos.remove(valor)

# Imprimir los valores que solo aparecen una vez
for valor in valores_unicos:
    print(valor)

###########################################################################################

mi_diccionario = {"a1": "maria", "b1": "pedro", "c1": "maria", "d1": "paul"}

valores_unicos = []
valores_repetidos = []

# Identificar valores únicos y repetidos
for valor in mi_diccionario.values():
    if valor in valores_unicos:
        valores_repetidos.append(valor)
    else:
        valores_unicos.append(valor)

# Remover de la lista valores_unicos aquellos que se repiten
for valor in valores_repetidos: 
    while valor in valores_unicos:
        valores_unicos.remove(valor)

# Imprimir los valores que solo aparecen una vez
for valor in valores_unicos:
    print(valor)