# Hacer un programa para ingresar por teclado las tres notas de exámenes de un
# alumno y luego calcule y emita por pantalla el promedio final.

nota_uno = int(input("Ingrese la nota del examen uno: "))
nota_dos = int(input("Ingrese la nota del examen dos: "))
nota_tres = int(input("Ingrese la nota del examen tres: "))

promedio_notas = (nota_uno + nota_dos + nota_tres) / 3

print(f"El promedio de las notas es: {promedio_notas}")