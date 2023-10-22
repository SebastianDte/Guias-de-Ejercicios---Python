# Hacer un programa que solicite el ingreso de un número y que luego emita un
# cartel por pantalla aclarando si el mismo es múltiplo de 5.

n1 = int(input("Ingrese un Número: "))

if(n1 % 5 == 0):
    print("Es múltiplo de 5")
else:
    print("No es multiplo de 5")