
try:

    num1 = float(input("ingrese un PRIMER numero para realizar una operacion : "))
    num2 = float(input("ingrese el SEGUNDO numero para realizar la operacion : "))
    print("LA OPERACION PUEDE SER COMO : \npruducto : * \tadicion o suma : + \tsustraccion o resta : - \tdivision /")
    operador = input("ingrese el OPERADOR : ")

    if operador=="+":
        suma = num1 + num2
        print("la suma es : ",suma)
    elif operador=="-":
        sustraccion = num1 - num2
        print("la diferencia es : ",sustraccion)
    if operador=="*":
        producto = num1 * num2
        print("el producto es : ",producto)
    if operador=="/":
        division = num1 / num2
        print("la division es : ",division)  

except ValueError:
    print("debes ingresar un numero")
except ZeroDivisionError:
    print("no se puede dividir por cero")
finally:
    print("sin ingresate bien los numeros, entonces al parecer NO INGRESASTE CORRECTAMENTE el operador ")

#######################################################

"""def resta(a, b):
    return a - b

def suma(a,b):
    return a+b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def main():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        operacion = input("Ingrese la operación (+, -, *, /): ")

        if operacion == "+":
            resultado = suma(num1, num2)
        elif operacion == "-":
            resultado = resta(num1, num2)
        elif operacion == "*":
            resultado = multiplicacion(num1, num2)
        elif operacion == "/":
            resultado = division(num1, num2)
        else:
            print("Operación no válida. Por favor ingrese +, -, *, o /.")
            return

        print(f"El resultado es: {resultado:.2f}")

    except ValueError:
        print("Entrada incorrecta. Por favor ingrese números válidos.")

    except ZeroDivisionError as e:
        print(e)

if __name__ == "__main__":
    main()
"""