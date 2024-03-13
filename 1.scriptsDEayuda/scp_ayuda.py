
from os import system
system("cls")

######################################################################
"""          Usando el mismo método en diferentes clases           """
######################################################################

class A:  # Clase padre 1
    def metodo_a(self):
        print("Método A")


class B:  # Clase padre 2
    def metodo_b(self):
        print("Método B")


class C(A, B):  # Clase hija que hereda de A y B
    def metodo_c(self):
        print("Método C")


c = C()  # Creamos una instancia de C
c.metodo_a()  # Podemos usar el método heredado de A
c.metodo_b()  # Y también el método heredado de B
c.metodo_c()  # Y también el método propio de C



######################################################################
"""                     """
######################################################################



import tkinter as tk

class MiEtiqueta:
    def __init__(self, master, text, x, y, bg, font):
        self.label = tk.Label(master, text=text, bg=bg, font=font)
        self.label.place(x=x, y=y)
        # Añadir la etiqueta al marco
        self.label.pack()

# Crear la ventana principal de Tkinter
root = tk.Tk()

# Definir el color de fondo común y la fuente común
l_bg = "white"
l_font = ("Arial", 12)

# Crear un frame dentro de la ventana principal
frame2 = tk.Frame(root)
frame2.pack()

# Crear instancias de la clase MiEtiqueta para cada etiqueta deseada
etiqueta1 = MiEtiqueta(frame2, text='Nombre: ', x=10, y=10, bg=l_bg, font=l_font)
etiqueta2 = MiEtiqueta(frame2, text='Edad: ', x=10, y=55, bg=l_bg, font=l_font)
etiqueta3 = MiEtiqueta(frame2, text='Email: ', x=10, y=105, bg=l_bg, font=l_font)

# Iniciar el bucle principal de Tkinter
root.mainloop()

