numero=int(input("Ingrese el numero: "))
factorial=1
for i in range(1, numero+1):
    factorial*=i
print("El factorial del numero ", numero, "es: ",factorial)
