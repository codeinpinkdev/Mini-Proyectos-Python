#Programa para poner en práctica el tema de funciones con retorno. 
#Calculadora básica, funcion para suma, resta, mult y div, y la misma calculadora es una función para que pueda ser llamada en el programa.

def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b

def calculadora():
    print("¿Qué operación deseas realizar?")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    
    opcion = int(input("Opción: "))

    numeroUno = float(input("Dame el primer número: "))
    numeroDos = float(input("Dame el segundo número: "))

    if opcion == 1:
        print(suma(numeroUno, numeroDos))
    elif opcion == 2:
        print(resta(numeroUno, numeroDos))
    elif opcion == 3:
        print(multiplicacion(numeroUno, numeroDos))
    elif opcion == 4:
        print(division(numeroUno, numeroDos))
    else:
        print("Opción inválida. Por favor, ingresa una opción válida (1/2/3/4).")

if __name__ == "__main__":
    calculadora()
