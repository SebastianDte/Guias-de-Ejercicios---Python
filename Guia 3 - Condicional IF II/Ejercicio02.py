# Hacer un programa que solicite el ingreso de dos números y luego calcular:
# a. La resta si el primero es mayor que el segundo.
# b. La suma si son iguales.
# c. El producto si el primero es menor.
# Se deberá emitir un cartel por pantalla con el resultado correspondiente.

n1 = int(input("Ingrese un Número: "))
n2 = int(input("Ingrese un Número: "))

if(n1 > n2):
    r = n1 - n2
elif(n1 < n2):
    r = n1 * n2
else:
    r = n1 + n2
print(f"El resultado obtenido es: {r}")