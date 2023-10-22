# Hacer un programa para ingresar 10 números y luego calcule y emita el mayor
# de los primos de la lista. En caso de no haber ningún número primo, deberá
# aclararlo con un cartel.

bandera = True
bandera_primos = False

for i in range(5):
    contador = 0
    n1 = int(input("Ingrese un Número: "))
    
    for x in range(1,n1 + 1):
        if(n1 % x == 0):
            contador += 1
            
    if(bandera):
        if(contador == 2):
            mayor_primo = n1
            bandera_primos = True
            bandera = False
    else:
        if(contador == 2):
            if(n1 > mayor_primo):
                mayor_primo = n1
    
            
if(bandera_primos != 0):
    print(f"El mayor numero primo ingresado fue: {mayor_primo}")
else:
    print("No se ingresaron Números primos")