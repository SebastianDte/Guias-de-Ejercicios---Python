# Realizar el nuevamente el ejercicio 8 pero ahora debe devolver además la
# posición en la que fue encontrado cada uno de los mínimos.

posicion_primero = None
posicion_Segundo = None
posicion = 1
bandera_primer_menor = True
bandera_segundo_menor = True
bandera = True


while bandera:
    n1 = int(input("Ingrese un Número: "))
    if(n1 != 0):
        if(bandera_primer_menor):
            primer_menor = n1
            posicion_primero = posicion
            bandera_primer_menor = False
        else:
            if(bandera_segundo_menor):
                bandera_segundo_menor = False
                if(n1 < primer_menor):
                    segundo_menor = primer_menor
                    posicion_Segundo = posicion_primero
                    primer_menor = n1
                    posicion_primero = posicion
                else:
                    segundo_menor = n1
                    posicion_Segundo = posicion
            else:
                if( n1 < primer_menor):
                    segundo_menor = primer_menor
                    posicion_Segundo = posicion_primero
                    primer_menor = n1
                    posicion_primero = posicion
                else:
                    if(n1 < segundo_menor):
                        segundo_menor = n1
                        posicion_Segundo = posicion
    else:
        bandera = False
        
    posicion += 1
            
print(f"Primer menor ingresado : {primer_menor} En la posicion: {posicion_primero}. Segundo menor ingresado: { segundo_menor}. En laPosicion: {posicion_Segundo}")
                
        
            
                
    