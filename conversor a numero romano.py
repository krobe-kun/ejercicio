numero=int(input("ingrese unnumero entre 1 y 100: "))

i=0
v=0
x=0
l=0

if numero<101:
    if numero == 100:
        print("C")
    elif 100<numero<91:
        num=numero-90
        v=num//5
        i=numero-5
        print("XC",v*"V",i*"I")
    elif 90>numero>50:
            l=l+1
            num=numero-50
            x=num//10
            num2=num-x*10
            v=num2//5
            i=num2%5
            print(l*"L",x*"x",v*"v",i*"I")
    elif 0<numero<40:
        x=numero//10
        num2=numero-x*10
        v=num2//5
        i=num2%5
        if num2==9:
             print("I ",x*"x")
        elif num2==4:
            print(x*"x","I V",)
        else:
            print(x*"x",v*"v",i*"I") 


else:
    print("el numero es mayor a 100")
    
