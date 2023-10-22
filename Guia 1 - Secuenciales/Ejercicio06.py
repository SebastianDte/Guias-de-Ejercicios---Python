# Hacer un programa para ingresar por teclado los metros cuadrados totales de
# un predio y los metros cuadrados cubiertos; luego calcular y mostrar por
# pantalla el porcentaje de metros cuadrados cubiertos y el porcentaje de
# metros cuadrados descubiertos.

m2_totales = int(input("Ingrese los m2 totales: "))
m2_cubiertos = int(input("Ingrese los m2 cubiertos: "))

m2_descubiertos = m2_totales - m2_cubiertos
pro_m2cubiertos = (m2_cubiertos / m2_totales) * 100
pro_m2descubiertos = (m2_descubiertos / m2_totales) * 100

print(f"El porcentaje de m2 cubiertos es {pro_m2cubiertos} y el Porcentaje de m2 descubiertos es {pro_m2descubiertos}")
