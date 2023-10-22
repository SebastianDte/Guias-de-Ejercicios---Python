# Hacer un programa que permita ingresar el año actual y el año de la fecha de
# nacimiento de una persona y luego calcule y emita por pantalla su edad.
# Nota: no hay que tener en cuenta si la persona cumplió años o no,
# simplemente calcular.

anio_actual = int(input("Ingrese el año actual: "))
anio_nacimiento = int(input("Ingrese el año en que nacio: "))

edad = anio_actual - anio_nacimiento

print(f"Su edad es {edad}")