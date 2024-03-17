
import tkinter as tk

class LabeledText(tk.Frame):
    def __init__(self, master, label_text, bg, font, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        
        self.label = tk.Label(self, text=label_text, bg=bg, font=font)
        self.label.pack(side="left")
        
        self.text = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.text, font=font)
        self.entry.pack(side="left")

    def get_text(self):
        return self.text.get()

# Ejemplo de uso
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Ejemplo de Clase LabeledText")

    l_bg = "lightgrey"
    l_font = ("Arial", 10)

    frame2 = tk.Frame(root)
    frame2.pack(padx=10, pady=10)

    lbl1 = LabeledText(frame2, "Nombre: ", l_bg, l_font)
    lbl1.pack(pady=5)

    lbl2 = LabeledText(frame2, "Edad: ", l_bg, l_font)
    lbl2.pack(pady=5)

    lbl3 = LabeledText(frame2, "Email: ", l_bg, l_font)
    lbl3.pack(pady=5)

    def print_values():
        print("Nombre:", lbl1.get_text())
        print("Edad:", lbl2.get_text())
        print("Email:", lbl3.get_text())

    btn_print = tk.Button(root, text="Imprimir valores", command=print_values)
    btn_print.pack(pady=5)

    root.mainloop()
