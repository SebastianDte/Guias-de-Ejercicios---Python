# Hacer un programa que solicite dos números y luego muestre los números
# entre el menor y el mayor de ellos. Acordate, usando While.

n1 = int(input("Ingrese un Número: "))
n2 = int(input("Ingrese un Número: "))
if(n1 < n2):
    menor = n1
    mayor = n2
else:
    menor = n2
    mayor = n1
while menor <= mayor:
    print(menor)
    menor+=1