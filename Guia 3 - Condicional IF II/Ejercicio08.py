# El negocio de desinfectante antes mencionado vende además detergente
# suelto, y los precios se aplican según la siguiente escala:
# a. 25 ARS por litro los primeros 50 litros.
# b. 20 ARS por litro si la venta es de 101 a 200 litros.
# c. 15 ARS por litro si la venta es de 201 a 500 litros.
# d. 10 ARS por litro si la venta es de más de 500 litros.
# Además, si paga en efectivo, tiene un adicional del 10% sobre el importe final.
# Hacer un programa que solicite la cantidad de litros vendidos y el tipo de pago
# (ingresará 1 si paga en efectivo y 0 con cualquier otro medio de pago) y calcule
# y emita por pantalla el monto final a abonar por el cliente.

cantidad_litros = int(input("Ingrese la cantidad de litros vendidos: "))
metodo_pago = int(input("Ingrese 1 para pagar en efectivo o 0 cualquier otro metodo: "))

if(cantidad_litros > 500):
    importe_final = cantidad_litros * 10
elif(cantidad_litros > 200):
    importe_final = cantidad_litros * 15
elif(cantidad_litros > 100):
    importe_final = cantidad_litros * 20
else:
    importe_final = cantidad_litros * 25
    
if(metodo_pago == 1):
    importe_final = importe_final * 0.90
    print(f"Total abonar {importe_final}")
else:
    print(f"Total abonar {importe_final}")
