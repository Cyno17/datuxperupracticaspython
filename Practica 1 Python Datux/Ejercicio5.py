# Escribe un programa que que pida un numero entero y calcule la suma de 1 hasta el numero ingresado
# Usar formula de suma de numeros enteros

# Pedir un número entero
print("Ingrese el valor final (N)")

# Asignar variables
a = int(input())
b=0

# Usar funcion for in para calcular
for i in range(1, a+1):
    print(i)
    b=b+i
print("La suma es: ",b)
    
