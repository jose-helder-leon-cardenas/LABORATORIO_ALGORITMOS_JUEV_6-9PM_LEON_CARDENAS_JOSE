"""n = input("ingrese un numero : ")

contador = 1
numero = 2

while contador >= n:
    
    for i in range():

        if numero//numero==1 and numero%1==numero:
            print("este numero es primo")
        else :
            print("el numero no es primo")
"""

###################################

while True:
    try:
        numero = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Error: Ingrese un número válido.")

divisible = 0
primo = True

for divisor in range(2, numero):
    if numero % divisor == 0:
        divisible = divisor
        primo = False
        break

if primo:
    print("El número es primo")
else:
    print("El número no es primo")

