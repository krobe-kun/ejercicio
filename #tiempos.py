#tiempos
hora=int(input("Ingrese la hora: "))
minutos= int(input("Ingrese el minuto: "))
duracion=int(input("Ingrese la aduracion del evento: "))

min_totales=minutos+duracion
hora_totales=hora+min_totales//60
min_totales=min_totales%60
hora_totales=hora_totales%24

print("la hora de finalizar sera: ", hora_totales,":",min_totales)
