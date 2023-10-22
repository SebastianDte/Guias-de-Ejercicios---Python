# Hacer un programa para ingresar un valor que estará expresado en minutos. Si
# los minutos superan los 60, pasar el valor a horas, de lo contrario dejarlo en
# minutos. Mostrar el resultado en pantalla aclarando si se muestran minutos u
# horas.

minutos = float(input("Ingrese un valor expresado en minutos: "))

if(minutos > 60):
    horas = minutos / 60
    print(f"Valor en Horas: {horas} hs")
else:
    print(f"Valor expresado en Minutos: {minutos} min")