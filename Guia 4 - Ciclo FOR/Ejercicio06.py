# Hacer un programa que solicite UN número y luego calcule y emita un cartel
# aclaratorio si el mismo es primo o no es primo.
# Nota: un numero es primo cuando es divisible únicamente por 1 y por sí
# mismo.
contador = 0
n1 = int(input("Ingrese un Número: "))

for i in range (1,n1 + 1):
    if(n1 % i == 0):
        contador += 1

if(contador == 2):
    print("El número ingresado es Primo")
else:
    print("El número ingresado no es primo")