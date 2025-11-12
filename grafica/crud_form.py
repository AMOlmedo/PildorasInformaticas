from tkinter import *
from tkinter import messagebox
import psycopg2

root=Tk()

#-----Creacion de la Barra de Menu -------
barraMenu=Menu(root) # asociamos a barraMenu la propiedad Menu para este root
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

# ----  Comienzo de Campos-----

miFrame=Frame(root) #creamos el frame
miFrame.pack()  # empaquetamos el frame

campoNombre=Entry(miFrame)
campoNombre.grid(row=0, column=1, padx=10, pady=10)
campoNombre.config(fg="Green", justify= "right")

campoApellido=Entry(miFrame)
campoApellido.grid(row=1, column=1, padx=10, pady=10)
campoApellido.config(fg="Green", justify= "right")

campoTelefono=Entry(miFrame)
campoTelefono.grid(row=2, column=1, padx=10, pady=10)
campoTelefono.config(fg="Green", justify= "right")

campoMail=Entry(miFrame)
campoMail.grid(row=3, column=1, padx=10, pady=10)
campoMail.config(fg="Green", justify= "right")

campoTexto=Text(miFrame, width=16, height=5)
campoTexto.grid(row=4, column=1, padx=10, pady=10)
scrollVertical=Scrollbar(miFrame, command=campoTexto.yview) #creacion barra de desplazamiento del campo de texto
scrollVertical.grid(row=5, column=2, sticky="nsew")

campoTexto.config(yscrollcommand=scrollVertical.set)

# ----- Comienzo Label Campos ----

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

telefonoLabel=Label(miFrame, text="Telefono:")
telefonoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

mailLabel=Label(miFrame, text="E-Mail:")
mailLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

textoLabel=Label(miFrame, text="Mensaje:")
textoLabel.grid(row=4, column=0, sticky="n", padx=10, pady=10)

# ----botones CRUD----
miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="CREATE")
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="READ")
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="UPDATE")
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="DELETE")
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()
