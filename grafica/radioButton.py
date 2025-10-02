from tkinter import *
root=Tk()  

opcion=IntVar()   #fnc q define en Entry es un int

Radiobutton(root, text="Masculino", variable=opcion, value=(1)).pack()
Radiobutton(root, text="Femenino", variable=opcion, value=(2)).pack()


root.mainloop()


