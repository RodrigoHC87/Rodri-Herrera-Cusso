import re
from tkinter import messagebox

class ValidarDatos:
    # ---------------------------------Fun. validar campos:
    def validar_campos(self, nombre, edad, email, provincia, voto):
        error_validacion = 0
        campos = [nombre.get(), edad.get(), email.get(), provincia.get(), voto.get()]

        # Verificar campos vacíos
        if "" in campos:
            messagebox.showinfo("Validación", "Todos los campos son requeridos!")
            error_validacion = 1
            campo_faltante = campos.index("") + 1
            return error_validacion, campo_faltante

        # Verificar formato de correo electrónico
        patron_mail = r"^[a-zA-Z0-9._%+*#-]+@[a-zA-Z0-9.-]+\.com$"
        if not re.match(patron_mail, email.get()):
            error_validacion = 2
            messagebox.showerror("Validación", 'Formato de correo no valido!')
            return error_validacion

        # Verificar formato y rango de la edad
        patron_edad = r"^\d{1,3}$"
        if not re.match(patron_edad, edad.get()):
            messagebox.showerror("Validación", "         Edad incorrecta!         ")
            error_validacion = 4
            return error_validacion

        edad_int = int(edad.get())
        if edad_int > 105 or edad_int < 16:
            if edad_int < 16:
                messagebox.showerror("Validación", 'La persona encuestada debe ser mayor!')
                error_validacion = 5
            elif edad_int > 105:
                messagebox.showerror("Validación", 'La persona encuestada no puede\ntener más años qué Mirtha!')
                error_validacion = 6
        return error_validacion
