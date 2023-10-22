# Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.

n1 = int(input("Ingrese un número: "))
contador = 0
i = 1

while i <= n1:
    if n1 % i == 0:
        contador += 1
    i += 1

if contador == 2:
    print("Es primo")
else:
    print("No es primo")
