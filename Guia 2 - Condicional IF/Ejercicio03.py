# Hacer un programa para ingresar dos números y que luego emita por pantalla
# el mayor de ellos o un cartel aclaratorio “Son iguales” en el caso de que así sea.

n1 = int(input("Ingrese un número: "))
n2 = int(input("Ingrese un número: "))

if(n1 > n2):
    print(f"El número mayor es: {n1}")
elif(n2 > n1):
    print(f"El número mayor es {n2}")
else:
    print("Los números ingresados son iguales.")