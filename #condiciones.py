#condiciones
numero1=int(input("ingrese el primer numero: "))
numero2=int(input("ingrese el segundo numero: "))
numero3=int(input("ingrese el tercer numero: "))
if numero1>numero2:
    numero_largo=numero1
elif numero2>numero3:
    numero_largo= numero2
else:
    numero_largo=numero3
print("el numero mayor es: ",numero_largo)

if numero3<numero2:
    numero_menor=numero3
elif numero2<numero1:
    numero_menor= numero2
else:
    numero_menor=numero1
print("el numero menor es: ",numero_menor)

if numero1==numero2==numero3:
    print("los tres numeros son iguales")
elif numero1==numero2:
    print("el primer numero y el segundo son iguales")
elif numero1==numero3:
    print("el primer numero y el tercero son iguales")
elif numero2==numero3:
    print("el segundo numero y el tercero son iguales")
else:
    print("los numeros son distintos")
