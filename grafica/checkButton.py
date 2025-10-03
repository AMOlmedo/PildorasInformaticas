# CheckButtum permite multiple selecciones

from tkinter import *

root=Tk()
root.title("Destinos")

playa=IntVar()
monte=IntVar()
campo=IntVar()

def seleccion():
    opcion=""
    if(playa.get()==1):
        opcion+="playa "
    if(monte.get()==1):
        opcion+="montaña "
    if(campo.get()==1):
        opcion+="campo "
    textoFinal.config(text=opcion)
foto=PhotoImage(file="avion.png")
Label(root, image=foto).pack()

frame=Frame(root)
frame.pack()

Label(root, text="Elije Destinos", width=50).pack()
Checkbutton(root, text="playa", variable=playa, onvalue=1, offvalue=0, command=seleccion).pack()
Checkbutton(root, text="montaña", variable=monte, onvalue=1, offvalue=0, command=seleccion).pack()
Checkbutton(root, text="campo", variable=campo, onvalue=1, offvalue=0, command=seleccion).pack()

textoFinal=Label(frame, text="Opciones: ")
textoFinal.pack()
root.mainloop()
