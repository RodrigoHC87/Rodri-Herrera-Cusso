from tkinter import Button

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
        "geometria_t3": {'width': 95, 'height': 95}
    }


    def __init__(self, master=None, text="", command=None, config_type="tipo1", **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

        self.config(**self.config_comun)

        if config_type in self.config_esp:
            self.config(**self.config_esp[config_type])


    def place_button(self, x, y, config_geometria='geometria_t1', **kwargs):

        if config_geometria in self.geometria:
            self.place(x=x, y=y, **self.geometria[config_geometria])

