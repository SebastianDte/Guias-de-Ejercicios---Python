# Una casa de video juegos otorga un descuento dependiendo del importe de la
# compra realizada según los siguientes valores:
# • Si el importe es menor a ARS 1000, no hay descuento.
# • Si el importe es ARS 1000 o más pero menor a ARS 5000, aplica un
# descuento del 10%.
# • Si el importe es ARS 5000 o más, aplica un descuento del 18%.
# Hacer un programa para ingresar un importe de venta y luego muestre por
# pantalla el importe final con el descuento que corresponda.

importe_final = float(input("Ingrese el importe final: "))

if(importe_final >= 5000):
    importe_final = importe_final * 0.82
elif(importe_final >= 1000):
    importe_final = importe_final * 0.90
    
print(f"El monto total es de: {importe_final}")