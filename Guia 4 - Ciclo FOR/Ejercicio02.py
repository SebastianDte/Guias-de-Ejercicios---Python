# Hacer un programa que solicite 20 números y calcule y emita por pantalla
# cuántos son positivos (mayores a cero). Se debe mostrar un solo valor: el
# conteo final.

contador = 0

for i in range(20):
    n1 = int(input("Ingrese un Número: "))
    if(n1 > 0):
        contador+=1

print(f"EL total de números positivos ingresados {contador}")
    