# Una universidad desea conocer los porcentajes de mujeres y hombres en las
# carreras de ciencias exactas. Se solicita un programa para cargar la cantidad de
# mujeres y la cantidad de hombres y que el mismo calcule y emita por pantalla
# los porcentajes correspondientes.

cantidad_mujeres = int(input("Ingrese la cantidad de mujeres: "))
cantidad_hombres = int(input("Ingrese la cantidad de Hombres: "))

total = cantidad_hombres + cantidad_mujeres
porcentaje_H = cantidad_hombres / total * 100
porcentaje_M = cantidad_mujeres / total * 100

print(f"Porcentaje Hombres{porcentaje_H} - Porcentaje Mujeres: {porcentaje_M}")