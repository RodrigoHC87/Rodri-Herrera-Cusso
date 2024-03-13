from peewee import SqliteDatabase, Model, AutoField, CharField, IntegrityError
from pathlib import Path


ruta_db_acc_obs = Path('bases_de_datos/db_pton_obs.db')

db_acc_obs = SqliteDatabase(ruta_db_acc_obs)
db_acc_obs.connect()


class BaseModel(Model):

    class Meta:
        database = db_acc_obs


class Modif_Observer(BaseModel):

    id = AutoField()
    observador = CharField()
    accion = CharField()
    email = CharField()
    nombre = CharField()
    fecha = CharField()
    hora = CharField()


db_acc_obs.create_tables([Modif_Observer], safe=True)


class Subject:

    observadores = []

    def agregar(self, obj):
        self.observadores.append(obj)

    def quitar(self, obj):
        pass

    def notificar(self, *args):
        self.argumentos = args

        if self.argumentos[0] == "Alta":
            Observador_Alta.update(self, args)

        elif self.argumentos[0] == "Modificar":
            Observador_Modif.update(self, args)

        elif self.argumentos[0] == "Baja":
            Observador_Baja.update(self, args)

        else:
            return "ERROR!"

        with db_acc_obs.atomic():
            try:
                #mod_obs = Modif_Observer.create(
                Modif_Observer.create(
                    observador = f"OBS - {args[0]}",
                    accion = args[0],
                    nombre = args[1],
                    email = args[2],
                    fecha = args[3],
                    hora = args[4],
                )

                #mod_obs.save()
            except Exception as e:
                print(e)


class Observador:

    def update(self,):
        raise NotImplementedError("Delegación de actualización")


class Observador_Alta(Observador):

    def __init__(self, objeto):
        self.observado_alta = objeto
        self.observado_alta.agregar(self)

    def update(self, *args):
        print(f"Actualización dentro de Observador - Obs > {args[0][0]} <")
        print(f"Datos >>> {args[0][0]} / {args[0][1]} /"
              f" {args[0][2]} <> {args[0][3]} -- {args[0][4]}")

        """mod_obs = Modif_Observer()
        mod_obs.observador = "OBS - ALTA"
        mod_obs.accion = self.argumentos[0]
        mod_obs.nombre = self.argumentos[1]
        mod_obs.email = self.argumentos[2]
        mod_obs.fecha = self.argumentos[3]
        mod_obs.hora = self.argumentos[4]
        mod_obs.save()"""


class Observador_Modif(Observador):

    def __init__(self, objeto):
        self.observado_modif = objeto
        self.observado_modif.agregar(self)

    def update(self, *args):
        print(f"Actualización dentro de Observador - Obs > {args[0][0]} <")
        print(f"Datos >>> {args[0][0]} / {args[0][1]} /"
              f" {args[0][2]} <> {args[0][3]} -- {args[0][4]}")

        """mod_obs = Modif_Observer()
        mod_obs.observador = "OBS - MODIFICAR"
        mod_obs.accion = args[0][0]
        mod_obs.nombre = args[0][1]
        mod_obs.email = args[0][2]
        mod_obs.fecha = args[0][3]
        mod_obs.hora = args[0][4]
        mod_obs.save()"""


class Observador_Baja(Observador):

    def __init__(self, objeto):
        self.observado_baja = objeto
        self.observado_baja.agregar(self)

    def update(self, *args):
        print(f"Actualización dentro de Observador - Obs > {args[0][0]} <")
        print(f"Datos >>> {args[0][0]} / {args[0][1]} /"
              f" {args[0][2]} <> {args[0][3]} -- {args[0][4]}")

        """mod_obs = Modif_Observer()
        mod_obs.observador = "OBS - BAJA"
        mod_obs.accion = self.argumentos[0]
        mod_obs.nombre = self.argumentos[1]
        mod_obs.email = self.argumentos[2]
        mod_obs.fecha = self.argumentos[3]
        mod_obs.hora = self.argumentos[4]
        mod_obs.save()"""

