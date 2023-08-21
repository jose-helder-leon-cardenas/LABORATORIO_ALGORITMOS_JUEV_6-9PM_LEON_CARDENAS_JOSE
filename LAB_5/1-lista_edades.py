edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")
# a. Ordena la lista y encuentra la edad mínima y máxima

"""lista_ordenada = sorted(edades)

edad_minima = lista_ordenada[0]  # lista_ordenada.min()
edad_maxima = lista_ordenada[len(lista_ordenada)-1] # lista_ordenada.max()

print("la edad minima encontrada es :", edad_minima)
print("la edad maxima encontrada es :", edad_maxima)

print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

# b. Añade de nuevo la edad mínima y máxima a la lista

def lista_agregada(lista_ordenada):

    lista_ordenada.insert(0,edad_minima)
    lista_ordenada.append(edad_maxima)

    return lista_ordenada

print(lista_agregada(lista_ordenada))"""

print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

# c. Encuentra la edad mediana (un elemento del medio o dos elementos del medio divididos por dos)

"""def encontrar_mediana(edades):
    edades_ordenadas = sorted(edades)
    cantidad_edades = len(edades_ordenadas)
    print("Edades ordenadas:", edades_ordenadas)

    if cantidad_edades % 2 == 1:  # Si es impar
        indice_medio = cantidad_edades // 2
        mediana = edades_ordenadas[indice_medio]
    else:  # Si es par
        indice_medio_1 = cantidad_edades // 2 - 1
        indice_medio_2 = cantidad_edades // 2
        mediana = (edades_ordenadas[indice_medio_1] + edades_ordenadas[indice_medio_2]) / 2
    
    return mediana

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
mediana = encontrar_mediana(edades)

print("Mediana:", mediana)

######################################

edades_ordenadas = sorted(edades)
cant_edades = len(edades)

if cant_edades%2 == 0:
    mediana1 = edades_ordenadas[cant_edades//2]
    mediana2 = edades_ordenadas[cant_edades//2 - 1]

    mediana = (mediana1 + mediana2)/2

    print("la cantidad de edades en la lista es par y la mediana es :", mediana )
else:
    mediana = edades_ordenadas[cant_edades//2]
    print("la cantidad de edades en la lista es impar y la mediana es :", mediana )"""


print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

# d. Encuentra la edad promedio (suma de todos los elementos divididos por su número)

"""def calcular_edad_promedio(edades):
    suma = 0
    for edad in edades :
        suma += edad
    
    promedio = suma/len(edades)
    return promedio

print("la edad promedio aclaculado es : ", calcular_edad_promedio(edades))

#############################
def calcular_edad_promedio(edades):
    suma_edades = sum(edades)
    total_edades = len(edades)
    promedio = suma_edades / total_edades
    
    return promedio

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
edad_promedio = calcular_edad_promedio(edades)

print("Edad promedio es: ", edad_promedio)"""

print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")

# e. Encuentra el rango de las edades (máximo menos mínimo)

"""edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
rango_edades = max(edades) - min(edades)

print("edades :",edades)
print("rango de edades calculado del max-min : ", rango_edades)

print("lllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllllll")"""

#f. Compara el valor de (mínimo - promedio) y (máximo - promedio), usa el método abs()

edades = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
minimo = min(edades)
maximo = max(edades)
promedio = sum(edades) / len(edades)

diferencia_min_promedio = abs(minimo - promedio)
diferencia_max_promedio = abs(maximo - promedio)

if diferencia_min_promedio > diferencia_max_promedio:
    print("El valor de (mínimo - promedio) es mayor que (máximo - promedio)")
elif diferencia_min_promedio < diferencia_max_promedio:
    print("El valor de (mínimo - promedio) es menor que (máximo - promedio)")
else:
    print("El valor de (mínimo - promedio) es igual a (máximo - promedio)")

