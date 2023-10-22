# Hacer un programa para ingresar un número y luego se emita un cartel por
# pantalla “Positivo” si el número es mayor a cero, “Negativo” si el número es
# menor a cero o “Cero” si el número es igual a cero.

n1 = int(input("Ingrese un Número: "))

if(n1 > 0):
    print("Positivo")
elif(n1 == 0):
    print("Es igual a 0")
else:
    print("Negativo")