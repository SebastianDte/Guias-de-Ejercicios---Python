# Hacer un programa que solicite cuatro números y emitir un cartel aclaratorio si
# son todos iguales entre sí, caso contrario, no emitir nada.

n1 = int(input("Ingrese un Número"))
n2 = int(input("Ingrese un Número"))
n3 = int(input("Ingrese un Número"))
n4 = int(input("Ingrese un Número"))

if(n1 == n2 and n2 == n3 and n3 == n4):
    print("Son iguales entre sí")