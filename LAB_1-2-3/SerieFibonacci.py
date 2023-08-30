cantidad=int(input("ingrese la cantidad de numeros a imprimir: "))
def fib(n):
    a = 0
    b = 1
    for k in range(n):
        c = b+a
        a = b
        b = c  
    return a
for x in range(cantidad):
    print(fib(x))
