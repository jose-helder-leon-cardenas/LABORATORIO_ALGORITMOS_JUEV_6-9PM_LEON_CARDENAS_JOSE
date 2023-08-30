def celsius_a_fahrenheit(temperatura):
    return temperatura * 9/5 + 32

def fahrenheit_a_celsius(temperatura):
    return (temperatura - 32) * 5/9

def conversion_temperatura():
    try:
        temperatura = float(input("Ingrese la temperatura debe ser en numeros: "))
        unidad = input("Ingrese la unidad de temperatura (C o F): ").upper()
        
        if unidad == "C":
            temperatura_convertida = celsius_a_fahrenheit(temperatura)
            print(f"{temperatura} grados Celsius equivalen a {temperatura_convertida} grados Fahrenheit.")
        elif unidad == "F":
            temperatura_convertida = fahrenheit_a_celsius(temperatura)
            print(f"{temperatura} grados Fahrenheit equivalen a {temperatura_convertida} grados Celsius.")
        else:
            print("Unidad de temperatura no válida.")
            
    except ValueError:
        print("Entrada inválida. Debe ingresar un número para la temperatura.")

conversion_temperatura()

