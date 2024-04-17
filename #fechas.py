#fechas
def comparar_fechas(fecha1,fecha2):
        
    if fecha1<fecha2:
        print("la persona2 ees mayor que la persona1")
    elif fecha2 <  fecha1:
            print("la persona2 ees mayor que la persona1")
    
    else:
        print("las 2 personas tienen la misma edad")

fecha_n1=int(input("ingrese la fecha de nacimiento de la persona 1 (ddmmaa):"))
fecha_n2=int(input("ingrese la fecha de nacimiento de la persona 2 (ddmmaa):"))
comparar_fechas(fecha_n1,fecha_n2)

