
def nuevo_libro(titulo,autor,categoria):
    libro={"titulo":titulo,"autor": autor,"categoria": categoria}
    libros.append(libro)
    print("libro agregado exitosamente.")

def buscar_por_titulo(titulo):
    resultados=[]
    for libro in libros:
        if libro["titulo"].lower() == titulo.lower():
            resultados.append(libros)
    return resultados
    

libros=[]
titulos=[]
autores=[]
categorias=[]

usuario= "Jose"
pasword= "python"
usu=str(input("ingrese usuario: "))
cont=str(input("ingrese contraseña: "))

if cont!= pasword:
    cont=str(input("ingrese contraseña: "))
    if cont!= pasword:
        cont=str(input("ingrese contraseña: "))
        if cont!= pasword:
            print("limite de intentos alcanzado")
else:
    while True:
        print("1. Agregar libro")
        print("2. Buscar libro por titulo")
        print("3. Buscar libro por autor")
        print("4. Buscar libro por categoria")
        print("5. Eliminar libro")
        print("6. Mostrar todos los libros")
        print("7. Salir")

        accion=int(input("Seleccione un apocion "))
    
        if accion==1:
            titulo1=str(input("ingrese el titulo del libro: "))
            autor1=str(input("ingrese el nombre del autor: "))
            categoria1=str(input("ingrese la categoria del libro: "))
            nuevo_libro(titulo1,autor1,categoria1)