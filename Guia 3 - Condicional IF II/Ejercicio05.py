# Hacer un programa que solicite el ingreso de las notas del primer parcial y del
# segundo parcial de una alumna de programación. El programa deberá analizar
# las notas y emitir la situación de la alumna según la siguiente escala:
# a. Si tiene 8 o más en ambos parciales, emitir “aprobación directa”.
# b. Si tiene entre 4 y 7 en ambos parciales, emitir “rinde examen final”.
# c. Si tiene menos de 4 en alguno de los dos parciales, emitir “debe
# recuperar”.
# El programa debe emitir solo un cartel, el que corresponda.

n1 = int(input("Ingre la primer nota: "))
n2 = int(input("Ingre la segunda nota: "))

if(n1 >= 8 and n2 >= 8):
    print("Aprobación Directa ")
elif(n1 >= 4 and n2 >= 4):
    print("Rinde Examen Final")
else:
    print(" Debe Recuperar")