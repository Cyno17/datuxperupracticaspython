# Escribe un programa que pida un numero entero y determine si es par o impar

# Pedir que se ingrese un número entero
Numero = int(input("Introduce un número entero: "))

# Determinar si el número es par o impar
if Numero % 2 == 0:
    print(f"El número {Numero} es par")
else:
    print(f"El número {Numero} es impar")
    