# Hacer un programa que solicite 20 números y luego emitir por pantalla el
# máximo de los números pares y el mínimo de los números impares.

bandera_maxpar = True
bandera_minimpar = True

for i in range(20):
    n1 = int(input("Ingrese un Número: "))
    if(n1 % 2 == 0):
        if(bandera_maxpar):
            max_par = n1
            bandera_maxpar = False
        else:
            if(n1 > max_par):
                max_par = n1
    else:
        if(bandera_minimpar):
            min_impar = n1
            bandera_minimpar = False
        else:
            if(n1 < min_impar):
                min_impar = n1

print(f"El maximo número par ingresado fue: {max_par}. Y el menor impar fue: {min_impar}")
            