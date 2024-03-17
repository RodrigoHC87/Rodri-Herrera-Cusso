from tkinter import Frame, Entry, Scrollbar, PhotoImage, messagebox
from tkinter.ttk import Combobox, Treeview, Style
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import StringVar
from pathlib import Path

from visual.clases_vista import *

from modelo import *
from visual.parametros_gui  import *
from visual.control_vista import ApartadoVisual



class Ventana(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1090, height=320)
        self.master = master
        self.pack()

        self.nombre = StringVar()
        self.edad = StringVar()
        self.email = StringVar()
        self.provincia = StringVar()
        self.int_voto = StringVar()
        self.id = -1

        self.objeto_base = Abmc()
        self.apartado_visual_v = ApartadoVisual()
        self.crear_widgets()
        self.objeto_base.actualizar_treeview(self.my_tree)
        self.habilitar_entrys("disabled")
        self.habilitar_btn_operaciones("normal")
        self.habilitar_btn_guardar_cancelar("disabled")


    #--------------------- WIDGETS ------------------------
    def crear_widgets(self):

        #--------------->     1er Frame     <---------------------------------
        frame1 = FrameGenerico(0, 0, 95, 299, '#bfdaff')


        self.btn_nuevo = BotonGenerico(8, 65, frame1, text="Nuevo", command=lambda:self.fun_nuevo(),
                                       config_type='tipo1', config_geo="geometria_t1")

        self.btn_modificar = BotonGenerico(8, 105, frame1, text="Modificar", command=lambda:self.fun_modificar(),
                                           config_type='tipo1', config_geo="geometria_t1")

        self.btn_eliminar = BotonGenerico(8, 145, frame1, text="Eliminar", command=lambda:self.fun_eliminar(),
                                            config_type='tipo1', config_geo="geometria_t1")


        #--------------->     2do Frame     <---------------------------------
        frame2 = FrameGenerico(98, 0, 169, 299, '#ADBACC')


        LabelGenerico(10, 5, frame2, "Nombre: ")

        LabelGenerico(10, 55, frame2, "Edad: ")

        LabelGenerico(10, 105, frame2, "Email: ")

        LabelGenerico(10, 155, frame2, "Provincia: ")

        LabelGenerico(10,205, frame2, "Intención de voto: ")


        #self.txt_nombre = Entry(frame2, textvariable=self.nombre, font= e_font)
        #self.txt_nombre.place(x=10, y=26, width=150, height=20)
        self.txt_nombre = EntryGenerico(10, 26, 150, 20, self.nombre, frame2)


        #self.txt_edad = Entry(frame2, textvariable=self.edad, font=e_font)
        #self.txt_edad.place(x=10, y=76, width=65, height=20)
        self.txt_edad = EntryGenerico(10, 76, 65, 20, self.edad, frame2)



        #self.txt_email = Entry(frame2, textvariable=self.email, font= e_font)
        #self.txt_email.place(x=10, y=126, width=150, height=20)
        self.txt_email = EntryGenerico(10, 126, 150, 20, self.email, frame2)



        #self.provincias = list_provincias
        #self.txt_provincia = Combobox(frame2, textvariable=self.provincia, width=18, values=self.provincias, state="readonly", font= e_font)
        #self.txt_provincia.current(0)
        #self.txt_provincia.place(x=10, y=176, width=135, height=20)
        self.txt_provincia = ComboBoxGenerico(10, 176, 135, 20, self.provincia, frame2, "lista_provincias")


        #self.opciones_votos = list_candidatos
        #self.txt_int_voto = Combobox(frame2, textvariable=self.int_voto, width=18, values=self.opciones_votos, state="readonly", font= e_font)
        #self.txt_int_voto.current(0)
        #self.txt_int_voto.place(x=10, y=226, width=135, height=20)
        self.txt_int_voto= ComboBoxGenerico(10, 226, 135, 20, self.int_voto, frame2, "lista_candidatos")



        self.btn_guardar = BotonGenerico(13, 260, frame2, text="Guardar", command=lambda:self.fun_guardar(),
                                         config_type='tipo2', config_geo="geometria_t2", bg='green')

        self.btn_cancelar = BotonGenerico(92, 260, frame2, text="Cancelar", command=lambda:self.fun_cancelar(),
                                          config_type='tipo2', config_geo="geometria_t2", bg='red')


        #--------------->     3er Frame     <---------------------------------
        frame3 = FrameGenerico(388, 0, 700, 299, 'yellow')


        #--------------->     TREEVIEW     <---------------------------------
        self.my_tree = Treeview(frame3, columns=('col1', 'col2', 'col3', 'col4', 'col5'))

        # Agregarle 'estilo' al Treeview
        self.estilo = Style()
        self.estilo.configure("Treeview", font=("MONOSPACE",10))
        # Personalizar el estilo al heading:
        self.estilo.configure("Treeview.Heading", font=("MONOSPACE", 11))

        self.my_tree.heading('#0', text='ID', anchor="center")
        self.my_tree.heading('col1', text='Nombre', anchor="center")
        self.my_tree.heading('col2', text='Edad', anchor="center")
        self.my_tree.heading('col3', text='Email', anchor="center")
        self.my_tree.heading('col4', text='Provincia', anchor="center")
        self.my_tree.heading('col5', text='Int. de voto', anchor="center")

        self.my_tree.column('#0', width=50)
        self.my_tree.column('col1', width=140, anchor="center")
        self.my_tree.column('col2', width=65, anchor="center")
        self.my_tree.column('col3', width=175, anchor="center")
        self.my_tree.column('col4', width=115, anchor="center")
        self.my_tree.column('col5', width=125, anchor="center")


        self.my_tree.place(x=0, y=0, width=683, height=299)


        #----------------------------------------- Scrollbar
        sb = Scrollbar(frame3, orient="vertical")
        sb.pack(side="right", fill="y")
        self.my_tree.config(yscrollcommand=sb.set)
        sb.config(command=self.my_tree.yview)
        self.my_tree['selectmode'] = 'browse'


        #--------------->     4th Frame     <---------------------------------
        frame4 = FrameGenerico(270, 0, 115, 299, "#637A99")


        self.ruta_img_enc = Path("visual/1.encuestar_img.png")
        self.img_btn_enc = PhotoImage(file=self.ruta_img_enc)

        self.ruta_img_graf = Path("visual/2.img_graficar.png")
        self.img_btn_graficar = PhotoImage(file=self.ruta_img_graf)

        self.btn_encuestar = BotonGenerico(11, 45, frame4, command=lambda:self.fun_btn_encuestar(),
                                           config_type='tipo3', config_geo="geometria_t3", image= self.img_btn_enc)

        self.btn_graficar = BotonGenerico(11, 170, frame4, command=lambda:self.fun_btn_graficar(frame3),
                                          config_type='tipo3', config_geo="geometria_t3", image= self.img_btn_graficar)



    # ---------FUNCIONES PRINCIPALES!------------------
    def fun_nuevo(self,):

        self.habilitar_entrys("normal")
        self.habilitar_btn_operaciones("disabled")
        self.habilitar_btn_guardar_cancelar("normal")
        self.apartado_visual_v.ord_aleatorio_candidatos(self.txt_int_voto)
        self.apartado_visual_v.limpiar_entradas(self.nombre, self.edad, self.email, self.provincia, self.int_voto)
        self.txt_nombre.focus()


    def fun_modificar(self,):

        self.apartado_visual_v.ord_aleatorio_candidatos(self.txt_int_voto)
        seleccionado = self.my_tree.focus()
        # Para conocer el valor del ID (en este caso)
        clave = self.my_tree.item(seleccionado, 'text')

        if clave == "":
            messagebox.showwarning("Modificar", "Debes seleccionar un elemento de la tabla")
        else:
            self.id = clave
            self.habilitar_entrys("normal")
            # Para conocer los valores del item seleccionado
            valores = self.my_tree.item(seleccionado, 'values')
            self.apartado_visual_v.insertar_encuesta_modificar(valores, self.txt_nombre, self.txt_edad,
                                                               self.txt_email, self.txt_provincia, self.txt_int_voto)
            self.habilitar_btn_operaciones("disabled")
            self.habilitar_btn_guardar_cancelar("normal")


    def fun_eliminar(self,):

        self.objeto_base.baja(self.my_tree)


    def fun_guardar(self,):

        if self.id == -1:
            code = self.objeto_base.alta(self.nombre, self.edad, self.email, self.provincia, self.int_voto, self.my_tree)
        else:
            code = self.objeto_base.modificar(self.nombre, self.edad, self.email, self.provincia, self.int_voto, self.my_tree)
            if code != 0:
                self.id = 0
            else:
                self.id = -1

        if code == 0:
            self.apartado_visual_v.limpiar_entradas(self.nombre, self.edad, self.email, self.provincia, self.int_voto)
            self.habilitar_btn_guardar_cancelar("disabled")
            self.habilitar_entrys("disabled")
            self.habilitar_btn_operaciones("normal")
            self.apartado_visual_v.unbinded_btn_email_edad(self.txt_email, self.txt_edad)

        else:
            self.validacion_gral(code)


    def fun_cancelar(self,):

        respuesta = messagebox.askquestion("Cancelar", "Esta seguro que desea cancelar la operación actual?")
        if respuesta == messagebox.YES:
            self.apartado_visual_v.limpiar_entradas(self.nombre, self.edad, self.email, self.provincia, self.int_voto)
            self.habilitar_btn_guardar_cancelar("disabled")
            self.habilitar_entrys("disabled")
            self.habilitar_btn_operaciones("normal")
            self.apartado_visual_v.unbinded_btn_email_edad(self.txt_email, self.txt_edad)


    # --------------- Botones Gráfico y Encuesta ---------------------------------------
    def fun_btn_encuestar(self,):

        self.my_tree.place(x=0, y=0, width=683, height=299)
        plt.close("all")
        try:
            self.canvas.get_tk_widget().place(x=0, y=0,width=0, height=0)
        except AttributeError:
            messagebox.showinfo(message='Usted se encuentra en "Encuestar"!', title="Aviso")
        self.habilitar_btn_operaciones("normal")
        self.btn_graficar.configure(state="normal")


    def fun_btn_graficar(self, frame3):

        votos_grafico = self.objeto_base.conteo_de_votos()
        plt.close("all")
        self.my_tree.place_forget()
        self.habilitar_btn_operaciones("disabled")
        self.btn_graficar.configure(state="disabled")

        # GRAFICO-----------------------------------------------------------------------------
        candidatos = list_candidatos_graf
        colores = list_colores_graf

        fig, axs1 = plt.subplots(1, dpi=80, figsize=(13, 4), sharey=True, facecolor="lightblue")
        axs1.bar(candidatos, votos_grafico, color=colores)
        axs1.set_ylabel('Cantidad de votos')
        self.canvas = FigureCanvasTkAgg(fig, master=frame3)
        self.canvas.draw()
        self.canvas.get_tk_widget().place(x=0, y=0, width=685, height=299)


    # ---------FUNCIONES SECUNDARIAS!------------------

    #-------------- Funciones tkinter ----------------------------------------
    def habilitar_entrys(self, estado):

        self.txt_nombre.configure(state=estado)
        self.txt_edad.configure(state=estado)
        self.txt_email.configure(state=estado)
        if estado == "normal":
            self.txt_int_voto.configure(state="readonly")
            self.txt_provincia.configure(state="readonly")
        else:
            self.txt_int_voto.configure(state=estado)
            self.txt_provincia.configure(state=estado)


    def habilitar_btn_operaciones(self, estado):

        self.btn_nuevo.configure(state=estado)
        self.btn_modificar.configure(state=estado)
        self.btn_eliminar.configure(state=estado)


    def habilitar_btn_guardar_cancelar(self, estado):

        self.btn_guardar.configure(state=estado)
        self.btn_cancelar.configure(state=estado)


# -------------------Fun. SECUNDARIA posibles errores validación:
    def validacion_gral(self, opcion):

        if opcion == 2 or opcion == 3:
            self.apartado_visual_v.help_mail(self.txt_email, opcion)
            return
        elif opcion == 4 or opcion == 5 or opcion == 6:
            self.apartado_visual_v.help_edad(self.txt_edad, opcion)
            return
        else:
            self.apartado_visual_v.help_campos_vacios(opcion[1], self.txt_nombre, self.txt_edad,
                                                      self.txt_email, self.txt_provincia, self.txt_int_voto)

