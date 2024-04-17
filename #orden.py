#orden
a=float(input("ingrese el primer numero "))
b=float(input("ingrese el segundo numero "))
c=float(input("ingrese el tercer numero "))

if a>b>c:
    print("mayor: ",a,"medio: ",b,"menor: ",c)
    print("menor: ",c,"medio: ",b,"mayor: ",a)
elif a>c>b:
    print("mayor: ",a,"medio: ",c,"menor: ",b)
    print("menor: ",b,"medio: ",c,"mayor: ",a)
elif b>a>c:
    print("mayor: ",b,"medio: ",a,"menor: ",c)
    print("menor: ",c,"medio: ",a,"mayor: ",b)
elif b>c>a:
    print("mayor: ",b,"medio: ",c,"menor: ",a)
    print("menor: ",a,"medio: ",c,"mayor: ",b)
elif c>b>a:
    print("mayor: ",c,"medio: ",b,"menor: ",a)
    print("menor: ",a,"medio: ",b,"mayor: ",c)
elif c>a>b:
    print("mayor: ",c,"medio: ",a,"menor: ",b)
    print("menor: ",b,"medio: ",a,"mayor: ",c,)  