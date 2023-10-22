# Hacer un programa para ingresar dos números distintos y luego se muestre por
# pantalla el menor de ellos.

n1 = int(input("Ingrese un Número: "))
n2 = int(input("Ingrese un Número: "))

if(n1 < n2):
    print(f"El número menor ingresado fue: {n1}")
else:
    print(f"El número menor ingresado fue: {n2}")