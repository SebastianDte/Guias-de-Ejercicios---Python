# Hacer un programa que solicite 20 números y luego mostrar por pantalla el
# menor de ellos y la posición en la que fue encontrado.

bandera = True

for i in range (10):
    if(bandera):
        n1 = int(input("Ingrese un Número: "))
        menor = n1
        posicion = i + 1
        bandera = False
    else:
        n1 = int(input("Ingrese un Número: "))
        if(n1 < menor):
            menor = n1
            posicion = i + 1

print(f"El mayor número ingresado fue {menor} en la posicion {posicion}")