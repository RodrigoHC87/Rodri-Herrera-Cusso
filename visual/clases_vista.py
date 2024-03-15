from tkinter import Button, PhotoImage
from pathlib import Path



# Parametros generales de los Botones:
b_csor = "hand2"
b_fg = '#FFFFFF'


    # botones del 1er frame
b_font = "MONOSPACE 10 bold"
b1_bg = '#0761F7'
b1_width = 80
b1_height = 30

    # botones del 2do frame
b2_font = "MONOSPACE 9 bold"
b2_width = 65
b2_height = 30

    # botones del 4to frame
bder = 0
"""ruta_img_enc = Path("visual/1.encuestar_img.png")
img_btn_enc = PhotoImage(file=ruta_img_enc)

ruta_img_graf = Path("visual/2.img_graficar.png")
img_btn_graficar = PhotoImage(file=ruta_img_graf)"""



class BotonGenerico(Button):

    config_comun = {
        'cursor': "hand2",
        'fg': '#FFFFFF'
    }

    def __init__(self, master=None, text="", command=None, config_type="tipo1", **kwargs):
        super().__init__(master, text=text, command=command, **kwargs)

        if config_type == "tipo1":
            self.config(**self.config_comun)
            self.config(bg='#0761F7', font='MONOSPACE 10 bold')
        elif config_type == "tipo2":
            self.config(**self.config_comun)
            self.config(font="MONOSPACE 9 bold")
        elif config_type == "tipo3":
            self.config(**self.config_comun)
            self.config_comun(border=bder)


    def place_button(self, x, y, width, height):
        self.place(x=x, y=y, width=width, height=height)
