class Gestor_gastos:
    def __init__(self):
        self.ingresos = 0
        self.gastos = 0
    
    def ingreso(self, cantidad):
        self.ingresos + cantidad
    
    def gasto(self, cantidad):
        self.gastos += cantidad
    
    def balance(self):
        return self.ingresos - self.gastos



while True: 
    print("\n1. Agregar Ingreso")
    print("2. Agregar gasto")
    print("3. Ver Balance")
    print("4. Ver Registro")
    print("5. Sali")
    opcion = int(input("seleccione una opcion: "))
    
    registro = Gestor_gastos()
    
    if opcion == 1:
        ingreso1=float(input("agregue ingreso: "))
        registro.ingreso(ingreso1)
    elif opcion == 2:
        egreso=int(input("ingrese el valor de su gasto: "))
        registro.gasto(egreso)
    elif opcion == 3:
        print("le queda un saldo de: ",registro.balance())
    elif opcion == 4:
        break
    else:
        print("opcion no valida")







