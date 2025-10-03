# RadioButtom seleccion excluyente, solo 1  opcion a seleccionar

from tkinter import *
root=Tk()  

opcion=IntVar()   #fnc q define en Entry es un int

Label(root, text="Genero").pack()
def imprimir():
    if opcion.get() ==1:
        mensaje.config(text="Has seleccionado Masculino")
    elif opcion.get()==2:
        mensaje.config(text="Has seleccionado Femenino")
    else:
        mensaje.config(text="Has seleccionado OTROS")

Radiobutton(root, text="Masculino", variable=opcion, value=(1), command=imprimir).pack()
Radiobutton(root, text="Femenino", variable=opcion, value=(2), command=imprimir).pack()
Radiobutton(root, text="Otras", variable=opcion, value=(3), command=imprimir).pack()

mensaje=Label(root)
mensaje.pack()

root.mainloop()


