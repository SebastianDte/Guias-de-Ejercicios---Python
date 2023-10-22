# Hacer un programa para ingresar una lista de números que corta cuando se
# ingresa un cero y luego mostrar: la cantidad de números primos, la cantidad de
# números pares, la cantidad de positivos y la cantidad de negativos.

badera = True
contador_primos = 0
contador_pares = 0
contador_negativos = 0
contador_positivos = 0


n1 = int(input("Ingrese un número: "))
while n1 != 0:
    contador_for = 0
    if(n1 > 0):
        contador_positivos += 1
    else:
        contador_negativos += 1
    if(n1 % 2 == 0):
        contador_pares += 1
    
    for i in range(1,n1 + 1):
        if(n1 % i == 0):
            contador_for += 1
    if(contador_for == 2):
        contador_primos += 1
        
    n1 = int(input("Ingrese un número: "))
    
        
print(f"Cant. Numeros positivos {contador_positivos},Cant. Negativos: {contador_negativos}")
print(f"Cantidad Pares: {contador_pares}, Cantidad Primos: {contador_primos}")
    
    
    