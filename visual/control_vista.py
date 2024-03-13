
from random import sample


class ApartadoVisual:


    def limpiar_entradas(self, *variables):
        for variable in variables:
            variable.set("")


    def  insertar_encuesta_modificar(self, valores, nombre, edad, email, prov, int_voto ):

        nombre.insert(0, valores[0])
        edad.insert(0, valores[1])
        email.insert(0, valores[2])
        prov.configure(state="normal")
        prov.insert(0, valores[3])
        prov.configure(state="readonly")
        int_voto.configure(state="normal")
        int_voto.insert(0, valores[4])
        int_voto.configure(state="readonly")
        nombre.focus()



    def ord_aleatorio_candidatos(self, opciones_vot):

        candidatos = ["Voto en Blanco", "La libertad no avanza", "Por unión la patria", "La SINiestra", "Juntos sin el cambio"]

        # Seleccionar 5 candidatos de forma aleatoria
        values = sample(candidatos, 5)

        # Agregar un elemento vacío al principio de la lista
        values.insert(0, "")

        # Asignar la lista a las opciones_vot
        opciones_vot["values"] = values


    def help_mail(self, email, opcion):

        email.delete(0, "end")
        if opcion == 2:
            email.configure(disabledforeground="red")
            email.insert(0,"ej: pepe99@yahoo.com")
            email.configure(state="disabled")
            email.bind("<Button-1>", lambda limpiar:(email.configure(fg="black", state="normal"), email.delete(0, "end")))
        email.focus_set()



    def help_edad(self, edad, opcion):

        edad.delete(0, "end")
        if opcion == 4:
            edad.configure(disabledforeground="red")
            edad.insert(0,"ej: 26")
            edad.configure(state="disabled")
            edad.bind("<Button-1>", lambda despejar:(edad.configure(fg="black", state="normal"), edad.delete(0, "end")))
        edad.focus_set()


    def unbinded_btn_email_edad(self, edad, email):
        edad.unbind("<Button-1>")
        email.unbind("<Button-1>")

    def help_campos_vacios(self, opcion, nombre, edad, email, prov, int_voto):

        campos = {1: nombre, 2: edad, 3: email, 4: prov, 5: int_voto}
        campo = campos.get(opcion)

        if campo:
            campo.focus_set()
