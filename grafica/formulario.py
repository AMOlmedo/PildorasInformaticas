from tkinter import *

raiz=Tk()

formulario=Frame(raiz, width=500, height=600)
formulario.pack()

#===== Entry - entradas del formulario =====
nombre=Entry(formulario)
nombre.grid(row=0, column=1, padx=15, pady=15)
nombre.config(fg="green", justify="center")


raiz.mainloop()
