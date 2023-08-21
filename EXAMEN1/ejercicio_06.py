""" un programa que tome una lista de números y devuelva una tupla con dos listas, la primera contiene
solo los números pares y la segunda los números impares.

Entrada Salida
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
salida
([2, 4, 6, 8], [1, 3, 5, 7, 9])"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def numeros_pares(numbers):
    numeros_pares = []
    for numero in numbers:
        if numero % 2==0
