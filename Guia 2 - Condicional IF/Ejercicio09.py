# Hacer un programa para ingresar cinco números distintos y luego mostrar por
# pantalla el mayor y el menor de ellos.

n1 = int(input("Ingrese un Número: "))
n2 = int(input("Ingrese un Número: "))
n3 = int(input("Ingrese un Número: "))
n4 = int(input("Ingrese un Número: "))
n5 = int(input("Ingrese un Número: "))

if(n1 > n2 and n1 > n3 and n1 > n4 and n1 > n5):
    mayor = n1
elif(n2 > n1 and n2 > n3 and n2 > n4 and n2 > n5):
    mayor = n2
elif(n3 > n1 and n3 > n2 and n3 > n4 and n3 > n5):
    mayor = n3
elif(n4 > n1 and n4 > n2 and n4 > n3 and n4 > n5):
    mayor = n4
elif(n5 > n1 and n5 > n2 and n5 > n3 and n5 > n4):
    mayor = n5
    
if(n1 < n2 and n1 < n3 and n1 < n4 and n1 < n5):
    menor = n1
elif(n2 < n1 and n2 < n3 and n2 < n4 and n2 < n5):
   menor = n2
elif(n3 < n1 and n3 < n2 and n3 < n4 and n3 < n5):
    menor = n3
elif(n4 < n1 and n4 < n2 and n4 < n3 and n4 < n5):
    menor = n4
elif(n5 < n1 and n5 < n2 and n5 < n3 and n5 < n4):
    menor = n5

#Forma dos de resolucion:
# mayor = max(n1,n2,n3,n4,n5)
# menor = min(n1,n2,n3,n4,n5)

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")