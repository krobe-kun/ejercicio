#impuestos
ingreso=float(input("Ingrese su ingreso: "))
if ingreso <85528.0:
    impuesto= ingreso*0.18-556.2
else:
    impuesto2=ingreso%85528
    impuesto=impuesto2*0.32+14839.2
print("su impuesto es: ",impuesto)
    
print("su impuesto es 0, no debe pagar nada")