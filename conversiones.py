
medida=int(input("ingrese la medida: "))
unidad_medida=input("ingrese la unidad de medida basado en: f = pies, p = pulgadas, y = yardas, c = centimetros, m = metros:  ")

if unidad_medida=="f":
    pies_pulgadas=medida*12
    pies_yardas=medida*0.3333333333
    pies_cent=medida*30.48
    pies_metros=medida*0.3048
    print("pies a pulgadas: ",pies_pulgadas,
          ", pies a yardas: ", pies_yardas,
          ", pies a centimetros: ", pies_cent,
          ", pies a metros: ", pies_metros)

elif unidad_medida=="p":
    pulg_pies= medida* 0.0833333333
    pulg_yardas=medida*0.0277777778
    pulg_cent=medida*2.54
    pulg_metros=medida*0.0254
    print("pulgadas a pies: ",pulg_pies,
          ", pulgadas a yardas: ", pulg_yardas,
          ", pulgadas a centimetros: ", pulg_cent,
          ", pulgadas a metros: ", pulg_metros)

elif unidad_medida=="y":
    yardas_pies = medida * 3
    yardas_pulg = medida * 36
    yardas_cent = medida * 91.44
    yardas_metros = medida * 0.9144
    print("yardas a pies: ",yardas_pies,
          ", yardas a pulgadas: ", yardas_pulg,
          ", yardas a centimetros: ", yardas_cent,
          ", yardas a metros: ", yardas_metros)

elif unidad_medida=="c":
    cent_pies = medida * 0.032808399
    cent_pulgadas = medida * 0.3937007874
    cent_yardas = medida * 0.010936133
    cent_metros = medida * 0.01
    print("centimetros a pies = ", cent_pies,
          ", centimetros a pulgadas: ", cent_pulgadas,
          ", centimetros a yardas: ", cent_yardas,
          ", centimetros a metros: ", cent_metros)
    
elif unidad_medida == "m":
    metros_pies= medida * 3.280839895
    metros_pulgadas= medida * 39.3700787402
    metros_yardas= medida * 1.0936132983
    metros_cent= medida * 100
    print("metros a pies = ", metros_pies,
          ", metros a pulgadas: ", metros_pulgadas,
          ", metros a yardas: ", metros_yardas,
          ", metros a metros: ", metros_cent)
    
else: 
    print("la letra no es valida en el repertorio de unidades de medida")