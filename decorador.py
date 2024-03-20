from peewee import SqliteDatabase, Model, AutoField, CharField
from datetime import datetime
from pathlib import Path



ruta_db_acc = Path("bases_de_datos/db_reg_deco.db")

db_acc = SqliteDatabase(ruta_db_acc)
db_acc.connect()


class BaseModel(Model):

    class Meta:
        database = db_acc


class Modificaciones(BaseModel):

    id = AutoField()
    accion = CharField()
    fecha = CharField()
    hora = CharField()


db_acc.create_tables([Modificaciones], safe=True)


def tipo_de_entrada(name):
    def wrapper (funcion):
        def wrapper_2(*args, **kwargs):
            resultado_fun = funcion(*args, **kwargs)

            if resultado_fun == 0 or resultado_fun == "ok":

                fecha_hora1 = [datetime.today().strftime("%d/%m/%y"), datetime.now().strftime("%H:%M:%S")]

                print("Acción del decorador.-")
                print(f"La acción '{name}' fue registrada en la fecha - {fecha_hora1[0]} a la hora: {fecha_hora1[1]}")
                print("---------------------------------------------------------------------\n")

                with db_acc.atomic():
                    try:
                        #mod1 = Modificaciones(
                        Modificaciones.create(
                            accion = name,
                            fecha = fecha_hora1[0],
                            hora = fecha_hora1[1],
                        )
                    except Exception as e:
                        print(e)
            return resultado_fun
        return wrapper_2
    return wrapper




# MIRAR ESTAS MEJORAS!
"""
from functools import wraps
from datetime import datetime

def tipo_de_entrada(name):
    def wrapper(funcion):
        @wraps(funcion)
        def wrapper_2(*args, **kwargs):
            resultado_fun = funcion(*args, **kwargs)

            if resultado_fun == 0 or resultado_fun == "ok":
                fecha_hora = datetime.now().strftime("%d/%m/%y %H:%M:%S")

                print("Acción del decorador.-")
                print(f"La acción '{name}' fue registrada en la fecha - {fecha_hora}")
                print("---------------------------------------------------------------------\n")

                with db_acc.atomic():
                    try:
                        Modificaciones.create(
                            accion=name,
                            fecha=fecha_hora.split()[0],
                            hora=fecha_hora.split()[1],
                        )
                    except Exception as e:
                        print(e)

            return resultado_fun

        return wrapper_2

    return wrapper"""