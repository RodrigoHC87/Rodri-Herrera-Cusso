import re
from tkinter import messagebox

class ValidarDatos:
    # ---------------------------------Fun. validar campos:
    def validar_campos(self, nombre, edad, email, provincia, voto):
        error_validacion = 0
        patron_edad = r"^[0-9]{1,3}$"
        patron_mail = r"^[a-zA-Z0-9._%+*#-]+@[a-zA-Z0-9.-]+\.com$"

        if nombre.get() == "" or email.get() == "" or edad.get() == "" or provincia.get() == "" or voto.get() == "":
            messagebox.showinfo("Validación", "Todos los campos son requeridos!")
            error_validacion = 1
            lista = [nombre.get(), edad.get(), email.get(), provincia.get(), voto.get()]
            ind_entry_faltante = 0
            for entry in lista:
                ind_entry_faltante += 1
                if entry == "":
                    return (error_validacion, ind_entry_faltante)

        if re.match(patron_mail, email.get()) == None:
            error_validacion = 2
            messagebox.showerror("Validación", 'Formato de correo no valido!')
            return error_validacion

        if re.match(patron_edad, edad.get()) == None:
            messagebox.showerror("Validación", "         Edad incorrecta!         ")
            error_validacion = 4
            return error_validacion

        if re.match(patron_edad, edad.get()):
            edad_int = int(edad.get())
            if edad_int > 105 or edad_int < 16:
                if edad_int < 16:
                    messagebox.showerror("Validación", 'La persona encuestada debe ser mayor!')
                    error_validacion = 5
                elif edad_int > 105:
                    messagebox.showerror("Validación", 'No podés tener más años qué Mirtha!')
                    error_validacion = 6
            return error_validacion

        else:
            return error_validacion

