# Considera dos listas, l1 y l2, que contienen tuplas. 
# Cada tupla consta de una cadena de texto y un número entero. 
# La lista l1 tiene 5 elementos y la lista l2 tiene 3 elementos.

l1 = [("one", 1), ("two", 2), ("three", 3), ("four", 4), ("five", 5)]
l2 = [("one", 1), ("two", 2), ("six", 6)]

#a. Crear conjuntos a partir de estas listas, s1 y s2.

print("\n=======================================================================")

print("convertido a tuplas de l1")
tuplas_l1 = tuple(l1)
print(tuplas_l1)

print("\n=======================================================================")

print("convertido a tuplas de l2")
tuplas_l2 = tuple(l2)
print(tuplas_l2)

print("\n=======================================================================")

print("convertido a conjunto") 
conjunto_creado_s1 = set(l1)  # {('two', 2), ('one', 1), ('five', 5), ('three', 3), ('four', 4)}
conjunto_creado_s2 = set(l2)  # {('one', 1), ('six', 6), ('two', 2)}

print(conjunto_creado_s1, ".......... \t", conjunto_creado_s2)


# b Encontrar los elementos que son comunes a s1 y s2 y almacenarlos en un conjunto s3.

s3 = conjunto_creado_s1.intersection(conjunto_creado_s2)

print("esto es s3 : ",s3)   # {('one', 1), ('two', 2)}

# c Encontrar los elementos que son únicos para s1 y s2 y almacenarlos en un conjunto s4.

s1 = {('two', 2), ('one', 1), ('five', 5), ('three', 3), ('four', 4)}
s2 = {('one', 1), ('six', 6), ('two', 2)}

# primer metodo
s4 = s1 - s2 | s2 - s1
print("esto es s4 : ", s4)
# segundo metodo
s4 = s1 ^ s2
print(s4)
#tercer metodo
s4 = s1.symmetric_difference(s2)
print(s4)

print("\n=======================================================================")

# d Crear una nueva lista l3 que contenga los elementos de s3 y s4 ordenados por el número entero de cada tupla.

# PRIMER METODO ===============

s3 = {('one', 1), ('two', 2)}
s4 = {('five', 5), ('four', 4), ('six', 6), ('three', 3)}

# Combinar los elementos de s3 y s4 en una sola lista
combined_list = list(s3) + list(s4)

# Ordenar la lista combinada por el número entero de cada tupla
l3 = sorted(combined_list, key=lambda x: x[1])

print("ESTO ES L3", l3)

# SEGUNDO METODO ============

# Encontrar los elementos únicos en s3 y s4
unique_elements = []
for tupla in s3:
    if tupla not in s4:
        unique_elements.append(tupla)

for tupla in s4:
    if tupla not in s3:
        unique_elements.append(tupla)


# Ordenar la lista de elementos únicos por el número entero de cada tupla
l3 = sorted(unique_elements, key=lambda x: x[1])

print("ESTO ES L3", l3)

# TERCER METODO

# Encontrar los elementos únicos en s3 y s4
unique_elements = []

for tupla_s3 in s3:
    encontrado = False
    for tupla_s4 in s4:
        if tupla_s3[1] == tupla_s4[1]:
            encontrado = True
            break
    if not encontrado:
        unique_elements.append(tupla_s3)

for tupla_s4 in s4:
    encontrado = False
    for tupla_s3 in s3:
        if tupla_s4[1] == tupla_s3[1]:
            encontrado = True
            break
    if not encontrado:
        unique_elements.append(tupla_s4)

# Ordenar la lista de elementos únicos por el número entero de cada tupla
l3 = sorted(unique_elements, key=lambda x: x[1])

print("ESTO ES L3", l3)
