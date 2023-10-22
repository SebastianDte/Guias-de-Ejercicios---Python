# Un importante negocio de desinfectante líquido realiza descuentos
# dependiendo de la cantidad de litros vendidos según la siguiente escala:
# a. Si vende menos de 100 litros, no hay descuento.
# b. Si vende entre 101 y 300 litros, el descuento es del 10%.
# c. Si vende entre 301 y 500 litros, el descuento es del 15%.
# d. Finalmente, si la venta es de más de 500 litros, el descuento es del 25%.
# Hacer un programa que solicite el ingreso del importe total de la venta y la
# cantidad de litros vendidos y calcule y emita el importe con el descuento
# aplicado.

importe_total = float(input("Ingrese el Importe Total: "))
cant_litros = float(input("Ingrese la cantidad de Litros Vendidos: "))

if(cant_litros > 500):
    importe_total = importe_total * 0.75
elif(cant_litros > 300):
    importe_total = importe_total * 0.85
elif(cant_litros > 100):
    importe_total = importe_total * 0.90

print(f"El importe abonar es de:{importe_total}")