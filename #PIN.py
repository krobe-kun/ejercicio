#PIN
contrasena=int(input("ingrese su pin: "))

digito1=contrasena//10000000
digito2=contrasena%10000000
digito2=digito2//1000000
digito3=contrasena%1000000
digito3=digito3//1000000
digito4=contrasena%100000
digito4=digito4//100000
digito5=contrasena%10000
digito5=digito5//10000
digito6=contrasena%1000
digito6=digito6//1000
digito7=contrasena%100
digito7=digito7//100
digito8=contrasena%10
digito8=digito8//10

if 10000000<=contrasena<=99999999:
   print("djfkhñdk")
   if digito1==0:
        print("error")
        if (digito1 or digito2 or digito3 or digito4 or digito5 or digito6 or digito7 or digito8)==1:
            print("correcto")
        elif (digito1 or digito2 or digito3 or digito4 or digito5 or digito6 or digito7 or digito8)==2:
            print("correcto")
        elif (digito1 or digito2 or digito3 or digito4 or digito5 or digito6 or digito7 or digito8)==3:
            print("correcto")
        elif (digito1 or digito2 or digito3 or digito4 or digito5 or digito6 or digito7 or digito8)==5:
            print("correcto")
        elif (digito1 or digito2 or digito3 or digito4 or digito5 or digito6 or digito7 or digito8)==7:
            print("correcto")
        else:
            print("error")
else:
    print("error")
    