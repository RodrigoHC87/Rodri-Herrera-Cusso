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



# ------------------------------------------------------------NUEVO!!
    def conteo_por_filtro(self, prov, regiones, edad):

        conteos1 = {
            "Voto en Blanco": 0,
            "Juntos sin el cambio": 0,
            "La SINiestra": 0,
            "La libertad no avanza": 0,
            "Por unión la patria": 0
        }

        conj_de_prov = {
            'Noroeste': {"Jujuy", "Salta", "Tucumán", "Santiago del Estero", "Catamarca", "La Rioja"},
            'Nordeste': {"Corrientes", "Misiones", "Chaco", "Formosa"},
            'Cuyo': {"San Luis", "Mendoza", "San Juan"},
            'Pampeana': {"Córdoba", "La Pampa", "Buenos Aires", "CABA", "Santa Fe", "Entre Ríos"},
            'Patagonia': {"Neuquén", "Río Negro", "Chubut", "Santa Cruz", "Tierra del Fuego, Antártida e Islas del Atlántico Sur"},
        }


        query = Encuestaa.select().where(Encuestaa.provincia == prov.get())
        for encuesta in query:
            voto = encuesta.voto
            if voto in conteos1:
                conteos1[voto] += 1
        votos_grafico_1 = list(conteos1.values())
        print("votos // _prov --->", votos_grafico_1)

        #---------------------------------------------------------

        lista_prov = list(conj_de_prov[regiones.get()])
        query_reg = Encuestaa.select().where(Encuestaa.provincia << lista_prov)
        for encuesta in query_reg:
            voto = encuesta.voto
            if voto in conteos1:
                conteos1[voto] += 1
        votos_grafico_reg = list(conteos1.values())
        print("votos // _region --->", votos_grafico_reg)

        #---------------------------------------------------------

        rango_etario = edad.get()
        print(rango_etario)
        edades=rango_etario.split("-")
        print(f"edad1-  {edades[0]} // edad2- {edades[1]}")
        query_edad = Encuestaa.select().where((Encuestaa.edad >= edades[0]) & (Encuestaa.edad <= edades[1]) )
        for encuesta in query_edad:
            voto = encuesta.voto
            if voto in conteos1:
                conteos1[voto] += 1
        votos_grafico_edad = list(conteos1.values())
        print("votos // _rango edad --->", votos_grafico_edad)




        return votos_grafico_1

# ------------------------------------------------------------


# ----------------------------------Fun. fecha y hora
def fecha_hora():
    fecha = datetime.today().strftime("%d/%m/%y")
    hora = datetime.now().strftime("%H:%M:%S")
    return (fecha, hora)