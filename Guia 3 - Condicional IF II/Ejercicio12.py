# Hacer un programa para ingresar tres números y emitir un cartel aclaratorio si
# la suma de los dos primeros es mayor al producto del segundo con el tercero.

n1 = int(input("Ingrese un Número"))
n2 = int(input("Ingrese un Número"))
n3 = int(input("Ingrese un Número"))

resultado_suma = n1 + n2
resultado_producto = n2 * n3

if(resultado_suma > resultado_producto):
    print("Es mayor la suma del primero por el segundo Número")
else:
    print("Es mayor el producto del segundo por el tercero")