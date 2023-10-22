# Hacer un programa para ingresar por teclado la longitud de los tres lados de un
# triángulo y que luego determine e informe con un cartel aclaratorio a qué tipo
# de triángulo corresponde:
# a. Equilátero: cuando los tres lados sean iguales.
# b. Isósceles: cuando dos de los tres lados sean iguales.
# c. Escaleno: cuando todos los lados sean distintos.

l1 = int(input("Ingre el primer lado del triangulo: "))
l2 = int(input("Ingre el segundo lado del triangulo: "))
l3 = int(input("Ingre el tercer lado del triangulo: "))

if(l1 == l2 and l2 == l3):
    print("Equilátero")
elif(l1 != l2 and l2 != l3 and l1 != l3):
    print("Escaleno")
else:
    print("Isoceles")