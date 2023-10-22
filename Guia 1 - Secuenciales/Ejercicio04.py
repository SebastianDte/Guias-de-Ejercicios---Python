# Una casa de computación paga a sus empleados un sueldo fijo de ARS15000
# más una comisión del 5% sobre el total facturado por cada empleado. Hacer un
# programa para ingresar el total facturado por un empleado y que luego calcule
# y emita por pantalla el sueldo total a cobrar por el mismo.

sueldo_fijo = 15000
comision = 5

total_facturado = float(input("Ingrese el total facturado: "))
monto_total = (sueldo_fijo + total_facturado) * 1.05

print(f"El monto total a cobrar es de:${monto_total}")