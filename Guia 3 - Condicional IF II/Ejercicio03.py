# Hacer un programa para ingresar dos números. Si el segundo es distinto de
# cero, calcular la división del primero por el segundo y mostrar el resultado por
# pantalla; caso contrario, emitir un cartel aclarando que no se puede dividir por
# cero.

n1 = float(input("Ingrese un Número: "))
n2 = float(input("Ingrese un Número: "))

if(n2 != 0):
    r = n1 / n2
    print(f"El resultado de la division es: {r}")
else:
    print("No se puede dividir por 0")
    