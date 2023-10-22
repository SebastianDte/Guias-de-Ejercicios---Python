# Hacer un programa para ingresar tres números y luego mostrarlos ordenados
# de menor a mayor.

n1 = int(input("Ingrese un Número:"))
n2 = int(input("Ingrese un Número:"))
n3 = int(input("Ingrese un Número: "))


if(n1 < n2 and n1 < n3):
    menor1 = n1
    if(n2 < n3):
        menor2 = n2
        menor3 = n3
    else:
        menor2 = n3
        menor3 = n2
elif(n2 < n3 and n2 < n1):
    menor1 = n2
    if(n1 < n3):
        menor2 = n1
        menor3 = n3
    else:
        menor2 = n3
        menor3 = n1   
elif(n3 < n1 and n3 < n2):
    menor1 = n3
    if(n1 < n2):
        menor2 = n1
        menor3 = n2
    else:
        menor2 = n2
        menor3 = n1

print(f"Los números ingresados fueron {n1,n2,n3}")
print(f"Los números ordenados de menor a mayor: {menor1,menor2,menor3}")
