from tkinter import *
from tkinter import messagebox
import psycopg2

root=Tk()

barraMenu=Menu(root) #crearmos la barra del menu
root.config(menu=barraMenu, width=300, height=300) # asociamos la barra al root y el tamaño de la barra

menu_bd=Menu(barraMenu,tearoff=0)
menu_bd.add_command(label="conectar BD")
menu_bd.add_command(label="Salir")

menu_borrar=Menu(barraMenu,tearoff=0)
menu_borrar.add_command(label="Borrar")

menu_crud=Menu(barraMenu,tearoff=0)
menu_crud.add_command(label="Create")
menu_crud.add_command(label="Read")
menu_crud.add_command(label="Update")
menu_crud.add_command(label="Delete")

menu_ayuda=Menu(barraMenu,tearoff=0)
menu_ayuda.add_command(label="Ayuda")
menu_ayuda.add_command(label="Acverda de ...")

barraMenu.add_cascade(label="BBDD", menu=menu_bd)
barraMenu.add_cascade(label="Borrar", menu=menu_borrar)
barraMenu.add_cascade(label="CRUD", menu=menu_crud)
barraMenu.add_cascade(label="Ayuda", menu=menu_ayuda)

root.mainloop()
