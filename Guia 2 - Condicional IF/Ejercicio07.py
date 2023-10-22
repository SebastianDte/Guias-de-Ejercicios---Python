# Hacer un programa para ingresar cuatro números distintos y luego mostrar por
# pantalla el mayor de ellos.

n1 = int(input("Ingrese un Número: "))
n2 = int(input("Ingrese un Número: "))
n3 = int(input("Ingrese un Número: "))
n4 = int(input("Ingrese un Número: "))


if(n1 > n2 and n1 > n3 and n1 > n4):
    print(f"Mayor: {n1}")
elif(n2 > n1 and n2 > n3 and n2 > n4):
    print(f"Mayor: {n2}")
elif(n3 > n1 and n3 > n2 and n3 > n4):
    print(f"Mayor: {n3}")
elif(n4 > n1 and n4 > n2 and n4 > n3):
    print(f"Mayor: {n4}")

    