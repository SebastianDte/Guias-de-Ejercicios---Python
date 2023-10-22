# Hacer un programa que solicite 10 números y luego mostrar por pantalla el
# máximo de ellos y la posición en la que fue ingresado.

bandera = True

for i in range (10):
    if(bandera):
        n1 = int(input("Ingrese un Número: "))
        maximo = n1
        posicion = i + 1
        bandera = False
    else:
        n1 = int(input("Ingrese un Número: "))
        if(n1 > maximo):
            maximo = n1
            posicion = i + 1

print(f"El mayor número ingresado fue {maximo} en la posicion {posicion}")