# Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego emitir por pantalla el máximo de los números
# negativos y el mínimo de los números positivos.

n1 = int(input("Ingrese un Número: "))
bandera_max = True
bandera_min = True
minimo_positivo = None
maximo_negativo = None

while n1 != 0:
    
    if(n1 > 0):
        if(bandera_max):
            minimo_positivo = n1
            bandera_max = False
        else:
            if(n1 < minimo_positivo):
                minimo_positivo = n1
    else:
        if(bandera_min):
            maximo_negativo = n1
            bandera_min = False
        else:
            if(n1 > maximo_negativo):
                maximo_negativo = n1

    n1 = int(input("Ingrese un Número: "))

if(minimo_positivo == None and maximo_negativo == None):
    print("No se ingreso ningun Número")
elif(minimo_positivo == None and maximo_negativo != None):
        print("No se ingresaron números positivos")
        print(f"El maximo negativo fue {maximo_negativo}")
elif(maximo_negativo == None and minimo_positivo != None):
            print("No se ingresaron numeros negativos") 
            print(f"El minimo positivo ingresado fue: {minimo_positivo}")
else:
    print(f"El minimo positivo ingresado fue: {minimo_positivo}, El maximo negativo fue {maximo_negativo}")
    
    

    
    
                
    
        
    
    