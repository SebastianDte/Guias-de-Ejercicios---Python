# Una importante marca de computadoras permite elegir cierta configuración
# del equipo a comprar. Para ello existe la siguiente escala de precios:
# i5 (1) i7 (2) i9 (3)
# 8 RAM (1) USD 800 USD 900 USD 1200
# 16 RAM (2) USD 900 USD 1000 USD 1400
# 32 RAM (3) USD 1000 USD 1400 USD 2000
# Además, el equipo viene con un disco que permite almacenar 500 GB de
# información y que se puede ampliar a 1 TB si así lo desea, lo cual tiene un costo
# adicional de USD 300.
# Hacer un programa que solicite la opción de procesador, la opción de memoria
# RAM, y si extiende el disco o no (ingresa 1 para extender y 0 para no extender)
# y calcule y emita por pantalla el monto de la máquina seleccionada.

op_procesador = int(input("Ingrese la opcion de Procesador: "))
op_ram = int(input("Ingrese la opcion de memoria RAM: "))

if(op_procesador == 1):
    if(op_ram == 1):
        importe = 800
    elif(op_ram == 2):
        importe = 900
    elif(op_ram == 3):
        importe = 1000
elif(op_procesador == 2):
    if(op_ram == 1):
        importe = 900
    elif(op_ram == 2):
        importe = 1000
    elif(op_ram == 3):
        importe = 1400
elif(op_procesador == 3):
    if(op_ram == 1):
        importe = 1200
    elif(op_ram == 2):
        importe = 1400
    elif(op_ram == 3):
        importe = 2000

print("Desea Extender la capacidad de Disco Duro ?")
op_disco = int(input( "Ingrese 1 para extender, 0 para no extender "))
if(op_disco == 1):
    importe += 300
    print(f"El total abonar es de: {importe}")
else:
    print(f"El total abonar es de: {importe}")
    
    