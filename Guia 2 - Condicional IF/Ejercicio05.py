# Hacer un programa para ingresar un número y mostrar por pantalla un cartel
# aclaratorio si el mismo es PAR o IMPAR.

n1 = int(input("Ingrese un número: "))

if(n1 % 2 == 0):
    print("El número ingresado es par")
else:
    print("El número ingresado es impar")