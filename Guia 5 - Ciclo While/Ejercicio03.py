# Hacer un programa que solicite la edad de un grupo de personas. El programa
# deberá pedir edades hasta que se ingrese una edad menor a 18 años. Deberá
# mostrar por pantalla cuántas personas mayores se registraron.

contador = 0
edad = int(input("Ingrese una edad: "))
while edad > 18:
    if(edad > 18):
        contador += 1
        edad = int(input("Ingrese una edad: "))


print(f"Hay {contador} mayores de edad")
        