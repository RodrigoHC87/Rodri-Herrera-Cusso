import tkinter as tk

from tkinter import Button



class BotonPersonalizado(Button):
    CONFIG_COMUN = {
        'bg': '#bfdaff',
        'cursor': 'hand2'
    }

    CONFIG_COMUN1 = {
        'bg': '#bfdaff',
        'cursor': 'hand2'
    }

    def __init__(self, master=None, text="", command=None, config_type='default', **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

        if config_type == 'default':
            self.config(**self.CONFIG_COMUN)
            self.config(fg='#000000', font=('Arial', 12))
        elif config_type == 'special':
            self.config(**self.CONFIG_COMUN1)
            self.config(fg='#0000FF', font=('Arial', 14))

    def place_button(self, x, y, width, height):
        self.place(x=x, y=y, width=width, height=height)

if __name__ == "__main__":
    from tkinter import Tk, Frame

    class MiVentana(Tk):
        def __init__(self):
            super().__init__()
            self.frame1 = Frame(self, bg='#bfdaff')
            self.frame1.place(x=0, y=0, width=95, height=299)

            self.btn_nuevo = BotonPersonalizado(self.frame1, text="Nuevo")
            self.btn_nuevo.place_button(x=8, y=65, width=80, height=30)

            self.btn_modificar = BotonPersonalizado(self.frame1, text="Modificar")
            self.btn_modificar.place_button(x=8, y=105, width=80, height=30)

            self.btn_eliminar = BotonPersonalizado(self.frame1, text="Eliminar")
            self.btn_eliminar.place_button(x=8, y=145, width=80, height=30)

            self.frame2 = Frame(self, bg='#bfdaff')
            self.frame2.place(x=0, y=0, width=95, height=299)

            self.btn_guardar = BotonPersonalizado(self.frame2, text="Guardar", command=self.fun_guardar,
                                                    config_type='special')
            self.btn_guardar.place_button(x=13, y=260, width=80, height=30)

        def fun_nuevo(self):
            print("Nuevo")

        def fun_modificar(self):
            print("Modificar")

        def fun_eliminar(self):
            print("Eliminar")

        def fun_guardar(self):
            print("Guardar")

    ventana = MiVentana()
    ventana.mainloop()



################################################################################################################




class BotonPersonalizado(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(
            relief=tk.RAISED,
            padx=10,
            pady=5,
            font=('Helvetica', 12)
        )

# Crear una ventana
ventana = tk.Tk()
ventana.title("Ejemplo de Clase de Botones")

# Crear instancias de la clase BotonPersonalizado
boton1 = BotonPersonalizado(ventana, text="Botón 1", command=lambda: print("Botón 1 presionado"))
boton1.pack(pady=25)

boton2 = BotonPersonalizado(ventana, text="Botón 2", command=lambda: print("Botón 2 presionado"))
boton2.pack(pady=5)

boton3 = BotonPersonalizado(ventana, text="Botón 3", command=lambda: print("Botón 3 presionado"))
boton3.pack(pady=5)

# Ejecutar el bucle principal de la interfaz gráfica
ventana.mainloop()

################################################################################################################

from tkinter import Tk, Frame, Button

class BotonPersonalizado(Button):
    def __init__(self, master=None, text="", command=None, **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)
        self.config(
            bg='#bfdaff',
            fg='#000000',
            cursor='hand2',
            font=('Arial', 12)
        )

class MiVentana(Tk):
    def __init__(self):
        super().__init__()

        self.frame1 = Frame(self, bg='#bfdaff')
        self.frame1.place(x=0, y=0, width=95, height=299)

        self.btn_nuevo = BotonPersonalizado(self.frame1, text="Nuevo", command=self.fun_nuevo)
        self.btn_nuevo.place(x=8, y=65, width=80, height=30)

        self.btn_modificar = BotonPersonalizado(self.frame1, text="Modificar", command=self.fun_modificar)
        self.btn_modificar.place(x=8, y=105, width=80, height=30)

        self.btn_eliminar = BotonPersonalizado(self.frame1, text="Eliminar", command=self.fun_eliminar)
        self.btn_eliminar.place(x=8, y=145, width=80, height=30)

    def fun_nuevo(self):
        print("Nuevo")

    def fun_modificar(self):
        print("Modificar")

    def fun_eliminar(self):
        print("Eliminar")

if __name__ == "__main__":
    ventana = MiVentana()
    ventana.mainloop()