# Hacer un programa que permita ingresar los kilómetros existentes entre dos
# ciudades y la velocidad promedio de un vehículo. Calcular y emitir por pantalla
# el tiempo aproximado que demandará llegar de un punto a otro teniendo en
# cuenta los datos ingresados.

km_existentes = int(input("Ingrese los km a recorrer de un punto a otro: "))
velocidad_promedio = int(input("Ingrese la velocidad promedio: "))

tiempo = km_existentes / velocidad_promedio

print(f"El tiempo aproximado para llegar a su destino es de: {tiempo:.2f}hs ")