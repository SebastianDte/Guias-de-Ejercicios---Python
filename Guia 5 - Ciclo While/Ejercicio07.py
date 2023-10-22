# Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego mostrar por pantalla el máximo de ellos y la posición
# en la que fue ingresado.

maximo = 0
bandera = True
banderab = True
posicion = 0
posicionmax = 0

while bandera:
    n1 = int(input("Ingrese un Número: "))
    if (n1 != 0):
        if(banderab):
            maximo = n1
            posicionmax = posicion + 1
            banderab = False
        else:
            if(n1 > maximo):
                maximo = n1
                posicionmax = posicion + 1
    else:
        bandera = False
    posicion += 1
            
    
if(maximo == 0):
     print("No se ingresaron numeros")
else:
    print(f"El maximo ingresado fue {maximo} en la posicion {posicionmax}")
    
    
        
