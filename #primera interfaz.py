#primera interfaz 
import tkinter as tk
root = tk.Tk ()

root.title("ejemplo boton")
root.geometry("600x400+500+200")
root.resizable(False, False)


boton_salir = tk.Button(root, text="Salir", command=lambda: root.quit())

boton_salir.pack(ipadx=20, ipady=10,expand=True)

root.mainloop()