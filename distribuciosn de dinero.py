cantidad= float(input("ingrese la cantidad: "))

if 0<cantidad<0.05:
    moneda= cantidad *100
    print("distribucion en centavos : ", moneda, "monedas de 1 c")
elif 0.04<cantidad<0.1:
    moneda=cantidad//0.05
    moneda2=cantidad%0.05
    print("ocupa ",moneda,"monedas de 5 c y ",(moneda2*100), "monedas de 1c.")

elif 0.09<cantidad<0.25:
    moneda=cantidad//0.1
    moneda1=cantidad%0.1
    moneda1=moneda1//0.05
    moneda2=cantidad%0.05 
    print("ocupa ", moneda,"de 10 c , ", moneda1," de 5 c y ", moneda2," de 1c.")

elif 0.24<cantidad<0.50:
    moneda=cantidad//0.25
    moneda1=cantidad%0.25
    moneda1=moneda1//0.1
    moneda2=cantidad%0.1
    moneda2=moneda2//0.05
    moneda3=cantidad%0.05
    print(moneda, "de 25 c ", moneda1, "moneda de 10 ", moneda2, "moneda de 5c ", moneda3, "moneda de 1c")

elif 0<cantidad<5:
    print("Su cantidad es de: ",cantidad," monedas de Q.1")
elif 4<cantidad<10:
    cambio1=cantidad//5
    cambio2=cantidad%5
    print("cantidad de ",cambio1,"billetes de Q.5 y ",cambio2,"monedas de Q.1")
elif 9<cantidad<20:
    cambio1=cantidad//10
    cambio2=cantidad%10
    cambio2=cambio2//5
    cambio3=cantidad%5
    print(cambio1,"billetes de Q.10")
    print(cambio2,"billetes de Q.5")
    print(cambio3,"monedas de Q.1")
elif 19<cantidad<50:
    cambio1=cantidad//20
    cambio2=cantidad%20
    cambio2=cambio2//10
    cambio3=cantidad%10
    cambio3=cambio3//5
    cambio4=cantidad%5
    print(cambio1,"billetes de Q.20")
    print(cambio2,"billetes de Q.10")
    print(cambio3,"billetes de Q.5")
    print(cambio4,"monedas de Q.1")
elif 49<cantidad<100:
    cambio1=cantidad//50
    cambio2=cantidad%50
    cambio2=cambio2//20
    cambio3=cantidad%20
    cambio3=cambio3//10
    cambio4=cantidad%10
    cambio4=cambio4//5
    cambio5=cantidad%5
    print(cambio1,"billetes de Q.50")
    print(cambio2,"billetes de Q.20")
    print(cambio3,"billetes de Q.10")
    print(cambio4,"billetes de Q.5")
    print(cambio5,"monedas de Q.1")

else:
    print("error")