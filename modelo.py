from tkinter import messagebox
from peewee import SqliteDatabase, Model, AutoField, CharField, IntegrityError
from datetime import datetime
from pathlib import Path


from validar_campos import ValidarDatos
from decorador import tipo_de_entrada
from observador import Subject


ruta_db = Path("bases_de_datos/data_base.db")

db = SqliteDatabase(ruta_db)
db.connect()

class BaseModel(Model):
    class Meta:
        database = db


class Encuestaa(BaseModel):
    id = AutoField()
    nombre = CharField()
    edad = CharField()
    email = CharField(unique=True)
    provincia = CharField()
    voto = CharField()


db.create_tables([Encuestaa], safe=True)


class Abmc(Subject):

    @tipo_de_entrada("ALTA")
    def alta(self, nombre, edad, email, provincia, voto, my_tree):

        code = ValidarDatos.validar_campos(self, nombre, edad, email, provincia, voto)

        if code == 0:

            with db.atomic():
                encuesta1 = Encuestaa(
                    nombre = nombre.get(),
                    edad = edad.get(),
                    email = email.get(),
                    provincia = provincia.get(),
                    voto = voto.get()
                )

                try:
                    encuesta1.save()
                    self.actualizar_treeview(my_tree)
                    messagebox.showinfo("Guardar", "Elemento insertado correctamente")
                    fecha_hora1 = fecha_hora()

                    self.notificar("Alta", nombre.get(), email.get(),
                                   fecha_hora1[0], fecha_hora1[1]
                                )
                    return code

                except IntegrityError:
                    messagebox.showerror("Error", f"El correo {email.get()} ya fue ingresado")
                    code = 3
                    return code

                except Exception as e:
                    print(e)
        else:
            return code


    @tipo_de_entrada("MODIFICAR")
    def modificar(self, nombre, edad, email, provincia, voto, my_tree):

        item_seleccionado = my_tree.focus()
        valor_id = my_tree.item(item_seleccionado)
        code = ValidarDatos.validar_campos(self, nombre, edad, email, provincia, voto)

        if code == 0:
            try:
                actualizar = Encuestaa.update(nombre=nombre.get(), edad=edad.get(), email=email.get(),
                                              provincia=provincia.get(), voto=voto.get()
                                              ).where(Encuestaa.id==valor_id["text"])

                actualizar.execute()

                self.actualizar_treeview(my_tree)
                messagebox.showinfo("Guardar", "Elemento modificado correctamente")

                fecha_hora1 = fecha_hora()

                self.notificar("Modificar", nombre.get(), email.get(),
                               fecha_hora1[0], fecha_hora1[1]
                               )
                return code

            except IntegrityError:
                messagebox.showerror("Error", f"El correo {email.get()} ya fue ingresado")
                code = 3
                return code

        else:
            return code


    @tipo_de_entrada("BAJA")
    def baja(self, my_tree):

        code = 1
        item_seleccionado = my_tree.focus()
        valor_id = my_tree.item(item_seleccionado)

        if valor_id["text"] == "":
            messagebox.showwarning("Eliminar", "Debes seleccionar un elemento de la tabla")
            return code

        else:
            data = f'{valor_id["values"][0]} - {valor_id["values"][1]} - {valor_id["values"][2]}'
            respuesta = messagebox.askquestion("Eliminar", "Deseas eliminar el registro seleccionado?\n   " + data)

            if respuesta == messagebox.YES:
                borrar = Encuestaa.get(Encuestaa.id==valor_id["text"])
                borrar.delete_instance()
                self.actualizar_treeview(my_tree)
                code = 0
                messagebox.showinfo("Eliminar", "Elemento eliminado correctamente")

                fecha_hora1 = fecha_hora()

                self.notificar("Baja", valor_id["values"][0], valor_id["values"][2],
                               fecha_hora1[0], fecha_hora1[1]
                               )
                return code

            else:
                messagebox.showinfo("Eliminar", "No fué posible eliminar el elemento")
                return code




# ----------------------------------Fun. actualizar treevieew
    def actualizar_treeview(self, my_tree):
        #limpieza de tabla
        records = my_tree.get_children()
        for element in records:
            my_tree.delete(element)
        #consiguiendo datos:
        for fila in Encuestaa.select():
            my_tree.insert("", 0, text=fila.id, values=(fila.nombre, fila.edad, fila.email, fila.provincia, fila.voto))


# ----------------------------------Fun. conteo_de_votos:
    """def conteo_de_votos(self):

        votos_grafico = []

        conteo_blancos = 0
        conteo_juntos = 0
        conteo_union = 0
        conteo_siniestra = 0
        conteo_libertad = 0

        for encuestas in Encuestaa.select():
            if encuestas.voto == "Voto en Blanco":
                conteo_blancos += 1
            elif encuestas.voto == "La libertad no avanza":
                conteo_libertad += 1
            elif encuestas.voto == "Por unión la patria":
                conteo_union += 1
            elif encuestas.voto == "La SINiestra":
                conteo_siniestra += 1
            elif encuestas.voto == "Juntos sin el cambio":
                conteo_juntos += 1

        votos_grafico.extend([conteo_blancos, conteo_juntos, conteo_siniestra,
                              conteo_libertad, conteo_union])
        print("votos: ", votos_grafico)
        return votos_grafico"""


    def conteo_de_votos(self):

        conteos = {
            "Voto en Blanco": 0,
            "Juntos sin el cambio": 0,
            "La SINiestra": 0,
            "La libertad no avanza": 0,
            "Por unión la patria": 0
        }

        for encuestas in Encuestaa.select():
            voto = encuestas.voto
            if voto in conteos:
                conteos[voto] += 1

        votos_grafico = list(conteos.values())
        print("votos: ", votos_grafico)
        return votos_grafico



# ----------------------------------Fun. fecha y hora
def fecha_hora():
    fecha = datetime.today().strftime("%d/%m/%y")
    hora = datetime.now().strftime("%H:%M:%S")
    return (fecha, hora)