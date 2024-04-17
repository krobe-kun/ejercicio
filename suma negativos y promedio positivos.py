positivo=0
negativo=0
promedio=0

for i in range(0,6):
    num=int(input("ingrese un numero peitivo o negativo: "))
    if num >= 1:
        positivo = positivo + num
        promedio = promedio + 1
    else: 
        negativo = negativo + num

if positivo==0 and promedio==0:
    print("No hay numeros positivos")
else:
    print("positivo: ", (positivo//promedio))
print("negativo: ", negativo)