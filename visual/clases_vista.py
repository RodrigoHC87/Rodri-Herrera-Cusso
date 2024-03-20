from tkinter import Button, Label, Frame, Entry
from tkinter.ttk import Combobox

class BotonGenerico(Button):

    config_comun = {
        'cursor': "hand2",
        'fg': '#FFFFFF',
        'border': 2
    }

    config_esp = {
        'tipo1': {'bg':'#0761F7', 'font':'MONOSPACE 10 bold'},
        'tipo2': {'font':'MONOSPACE 9 bold'},
        'tipo3': {'border': 0}
    }

    geometria = {
        "geometria_t1": {'width': 80, 'height': 30},
        "geometria_t2": {'width': 65, 'height': 30},
        "geometria_t3": {'width': 95, 'height': 95},
        "geometria_t4": {'width': 55, 'height': 25},
    }


    def __init__(self, x, y, master=None, text="", command=None, config_type="", config_geo="",  **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

        self.config(**self.config_comun)

        if config_type in self.config_esp:
            self.config(**self.config_esp[config_type])

        if config_geo in self.geometria:
            self.place(x=x, y=y, **self.geometria[config_geo])


#------------------------------------------------------------------------------------------------------

class LabelGenerico(Label):

    config_esp ={
        'tipo1': {'bg': 'red', 'font': 'MONOSPACE 10 bold', 'fg':'white'},
        'tipo2': {'bg': '#ADBACC', 'font': 'MONOSPACE 11 bold', 'fg':'black'},
    }

    def __init__(self, x, y, master=None, text="", config="", **kwargs):
        super().__init__(master, text=text, **kwargs)

        if config in self.config_esp:
            self.config(**self.config_esp[config])

        self.place(x=x, y=y)


class FrameGenerico(Frame):

    config_comun = {
        #En caso de necesitar!!
    }

    def __init__(self, x, y, widht, heigth, bg, master=None, config=config_comun, **kwargs):
        super().__init__(master, bg=bg, **config)

        self.place(x=x, y=y, width=widht, height=heigth)



class EntryGenerico(Entry):

    config_comun = {
        'font': "MONOSPACE 10"
    }

    def __init__(self, x, y, widht, heigth, textvariable, master=None, config=config_comun, **kwargs):
        super().__init__(master, textvariable=textvariable, **config)

        self.place(x=x, y=y, width=widht, height=heigth)



class ComboBoxGenerico(Combobox):
    lista_candidatos = ["", "Voto en Blanco", "La libertad no avanza", "Por unión la patria",
                       "La SINiestra", "Juntos sin el cambio"]

    lista_provincias = ["","Buenos Aires", "CABA", "Catamarca", "Chaco", "Chubut", "Córdoba", "Corrientes", "Entre Ríos",
                        "Formosa", "Jujuy", "La Pampa", "La Rioja", "Mendoza", "Misiones", "Neuquén", "Río Negro", "Salta",
                        "San Juan", "San Luis", "Santa Cruz", "Santa Fe", "Santiago del Estero",
                        "Tierra del Fuego, Antártida e Islas del Atlántico Sur",
                        "Tucumán"]

    opc_lista = {
        'lista_candidatos': lista_candidatos,
        'lista_provincias': lista_provincias
    }

    config_comun = {
        'width': 18,
        'state': 'reandonly',
        'font': 'MONOSPACE 10',
    }


    def __init__(self, x, y, widht, heigth, textvariable, master=None, config_lista="", **kwargs):
        super().__init__(master, textvariable=textvariable, **kwargs)

        self.configure(**self.config_comun)


        if config_lista in self.opc_lista:
            self.config(values = self.opc_lista[config_lista])

        self.current(0)

        self.place(x=x, y=y, width=widht, height=heigth)


    pass