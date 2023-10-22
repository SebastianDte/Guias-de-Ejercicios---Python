# Hacer un programa que solicite una lista de números que corta cuando se
# ingresa un cero y luego mostrar por pantalla el menor y el segundo menor.

bandera_primer_menor = True
bandera_segundo_menor = True
bandera = True


while bandera:
    n1 = int(input("Ingrese un Número: "))
    if(n1 != 0):
        if(bandera_primer_menor):
            primer_menor = n1
            bandera_primer_menor = False
        else:
            if(bandera_segundo_menor):
                bandera_segundo_menor = False
                if(n1 < primer_menor):
                    segundo_menor = primer_menor
                    primer_menor = n1
                else:
                    segundo_menor = n1
            else:
                if( n1 < primer_menor):
                    segundo_menor = primer_menor
                    primer_menor = n1
                else:
                    if(n1 < segundo_menor):
                        segundo_menor = n1
    else:
        bandera = False
            
print(f"El primer menor ingresado fue: {primer_menor} , el segundo menor fue { segundo_menor}")
                
        
            
                
    