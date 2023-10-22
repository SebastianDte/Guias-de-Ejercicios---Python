# Hacer un programa que solicite el ingreso de 10 números y que muestre el
# mayor de ellos por pantalla. Solo se debe emitir UN valor por pantalla.

bandera = True

for i in range(10):
    if(bandera):
        n = int(input("Ingrese un Número: "))
        mayor = n
        bandera = False
    else:
        n = int(input("Ingrese un Número: "))
        if(n > mayor):
            mayor = n
    
        
    
print(f"El número mayor ingresado fue {mayor}")