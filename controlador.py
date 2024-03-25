from tkinter import Tk
from vista import Ventana
import observador

from os import system
system("cls")


class Controlador:
    def __init__(self, root):
        self.controlador_root = root
        self.objeto_ventana = Ventana(self.controlador_root)
        self.observador_alta = observador.Observador_Alta(self.objeto_ventana.objeto_base)
        self.observador_mod = observador.Observador_Modif(self.objeto_ventana.objeto_base)
        self.observador_baja = observador.Observador_Baja(self.objeto_ventana.objeto_base)

if __name__ == '__main__':
    root = Tk()
    app = Controlador(root)
    root.wm_title("App POO + peewee + deco + pton observer -- RHC")
    root.mainloop()



"Cambiar el nombre de las clases por mi_class ---- ejemp mi_combobox, mi_boton"

#3
"Hacer personalizable la app (colores, idioma(?, fuente) Guardar esta nueva info en una nueva DDBB"
'Agregar la info de los frames(color, y cualquier cosa que puede ser util ) en "parametros_gui"'
"Hacer 3 variables de colores(jugar con la armonía de los colores) ver como seria el 'tema oscuro'"

#4
"Implementar un nuevo 'menu opciones' con 1.personalizacion, 2.idioma"

#5
"Opciones de graficos de barra segun la 'edad' y 'género' -(Agregar este apartado a todo el sistema)"

#1
'Crear un filtro de, fechas, edades, provincias e integrarlo a todo el sistema'
