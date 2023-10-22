# Hacer un programa que solicite 20 edades y luego calcule el promedio de edad
# de aquellas personas mayores a 18 años.

contador = 0
acu = 0

for i in range(5):
    edad = int(input("Ingrese su edad: "))
    
    if(edad > 18):
        acu += edad
        contador += 1

promedio = acu / contador

print(f"El promedio de edades mayores a 18 es de: {promedio}")