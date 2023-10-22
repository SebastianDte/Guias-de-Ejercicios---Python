# Hacer un programa para ingresar 4 números. Luego analizar e informar por
# pantalla si los mismos se encuentran ordenados de forma decreciente.

n1 = int(input("Ingrese un Número: "))
n2 = int(input("Ingrese un Número: "))
n3 = int(input("Ingrese un Número: "))
n4 = int(input("Ingrese un Número: "))

if(n1 > n2 and n2 > n3 and n3 > n4):
   print("Estan de forma decreciente")
else:
    print("No estan ordenados de forma Decreciente")