# Una importante cadena de delivery cuenta con una promoción por tiempo
# limitado en la que otorga un 15% de descuento sobre el total del valor de la
# compra realizada. Hacer un programa para solicitar el monto total y el mismo
# calcule y emita por pantalla el total a cobrar con el descuento aplicado.

monto_total = float(input("Ingrese el monto total: "))

total_cobrar = monto_total * 0.85

print(f"El total a cobrar con el descuento aplicado es de: ${total_cobrar}")