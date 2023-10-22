# Hacer un programa que permita ingresar por teclado dos números y que luego
# muestre por pantalla la suma, la resta, la multiplicación y la división de dichos
# números. Se deben mostrar cuatro resultados en pantalla. Los números deben
# ser solicitados una única vez.

n1 = float(input("Ingrese un número: "))
n2 = float(input("Ingrese un número: "))

suma = n1 + n2
resta = n1 - n2
multiplicación = n1 * n2
division = n1 / n2

print(f"Suma: {suma} \n Resta: {resta} \n Multiplicación: {multiplicación} \n Division: {division}")