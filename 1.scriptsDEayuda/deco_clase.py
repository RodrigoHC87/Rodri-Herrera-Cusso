from os import system
system("cls")


######################################################################
"""            Decoradores y uso de *args y **kwargs              """
######################################################################

def mi_decorador(clase):
    # Define una nueva clase que extiende la original
    class NuevaClase(clase):
        def __init__(self, *args, **kwargs):
            # Puedes agregar código adicional antes de inicializar la clase original
            print("Antes de inicializar la clase")
            # Llama al constructor de la clase original
            super().__init__(*args, **kwargs)
            # Puedes agregar código adicional después de inicializar la clase original
            print(args, kwargs)
            print("Después de inicializar la clase")

    # Devuelve la nueva clase modificada
    return NuevaClase

# Uso del decorador
@mi_decorador
class MiClaseOriginal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.dato = 3.14
        self.edad = edad
        print(f"Clase original inicializada con nombre: {self.nombre}")

# Crear una instancia de la clase decorada
objeto = MiClaseOriginal("Ejemplo 2.0", 36)




print("\n###################################################\n")

def funcion_con_args_y_kwargs(arg1, *args, kwarg1="predeterminado", **kwargs):
    print(f"arg1: {arg1}")
    print(f"args: {args}")
    print(f"kwarg1: {kwarg1}")
    print(f"kwargs: {kwargs}")

# Llamada a la función con diferentes argumentos
funcion_con_args_y_kwargs("valor1", "valor2", "valor3", kwarg1="personalizado", clave1="valor1", clave2="valor2")


print("\n###################################################\n")


# Función que actuará como decorador
def mi_decorador(clase):
    # Define una nueva clase que extiende la original
    class NuevaClase(clase):
        def __init__(self, *args, **kwargs):
            print(f"Antes de inicializar la clase {clase.__name__}")
            super().__init__(*args, **kwargs)
            print(f"Después de inicializar la clase {clase.__name__}")

    # Devuelve la nueva clase modificada
    return NuevaClase

# Clase 1
@mi_decorador
class MiClase1:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Clase original 1 inicializada con nombre: {self.nombre}")

# Clase 2
@mi_decorador
class MiClase2:
    def __init__(self, nombre):
        self.nombre = nombre
        print(f"Clase original 2 inicializada con nombre: {self.nombre}")

# Crear instancias de las clases decoradas
objeto1 = MiClase1("Ejemplo1")
objeto2 = MiClase2("Ejemplo2")
