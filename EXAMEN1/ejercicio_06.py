""" un programa que tome una lista de números y devuelva una tupla con dos listas, la primera contiene
solo los números pares y la segunda los números impares.

Entrada Salida
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
salida
([2, 4, 6, 8], [1, 3, 5, 7, 9])"""


def separar_numeros(numbers):
    pares = [num for num in numbers if num % 2 == 0]
    impares = [num for num in numbers if num % 2 == 1]
    return (pares, impares)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = separar_numeros(numbers)
print(resultado)
