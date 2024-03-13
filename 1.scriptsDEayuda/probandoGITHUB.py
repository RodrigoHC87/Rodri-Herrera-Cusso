
"""   PROBANDO GITHUB! """

import tkinter as tk

class Aplicacion:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Ejemplo POO con Tkinter")

        # Etiqueta
        self.etiqueta = tk.Label(ventana, text="Bienvenido a la aplicación!")
        self.etiqueta.pack(pady=10)

        # Campo de entrada
        self.campo_entrada = tk.Entry(ventana)
        self.campo_entrada.pack(pady=5)

        # Botón
        self.boton = tk.Button(ventana, text="Haz clic", command=self.mostrar_mensaje)
        self.boton.pack(pady=5)

    def mostrar_mensaje(self):
        mensaje = "¡Hola, " + self.campo_entrada.get() + "!"
        self.etiqueta.config(text=mensaje)

# Crear la ventana principal
ventana_principal = tk.Tk()

# Crear una instancia de la aplicación
app = Aplicacion(ventana_principal)

# Ejecutar la aplicación
ventana_principal.mainloop()
