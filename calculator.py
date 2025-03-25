def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."

def calculator():
    print("Bienvenido a la calculadora básica")
    print("Opciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    while True:
        choice = input("Selecciona una opción (1/2/3/4/5): ")

        if choice == '5':
            print("¡Gracias por usar la calculadora! Adiós.")
            break

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))

                if choice == '1':
                    print(f"Resultado: {add(num1, num2)}")
                elif choice == '2':
                    print(f"Resultado: {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"Resultado: {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"Resultado: {divide(num1, num2)}")
            except ValueError:
                print("Error: Por favor ingresa números válidos.")
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar la calculadora
if __name__ == "__main__":
    calculator()