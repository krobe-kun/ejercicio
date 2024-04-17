frase=input("ingrese una frase: ")
letra=input("ingrese una letra: ")
veces=0

for i  in frase:
    if i == letra:
        veces = veces + 1
print(veces)