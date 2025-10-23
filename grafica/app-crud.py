from tkinter import *
from tkinter import messagebox
import sqlite3
import os

directorio_script = os.path.dirname(os.path.abspath(__file__)) #esto es para q el SO pueda crear la DB
ruta_bd = os.path.join(directorio_script, "usuarios_db")

# ===== FUNCIONES ======
def conexionDB():
    miConexion=sqlite3.connect(ruta_bd)
    miCursor=miConexion.cursor()
    try:
        miCursor.execute('''
        CREATE TABLE USUARIOS(
                     ID INTEGER PRIMARY KEY AUTOINCREMENT,
                     NOMBRE VARCHAR(50),
                     APELLIDO VARCHAR(50),
                     PASSWORD VARCHAR (30),
                     DIRECCION VARCHAR (100),
                     COMENTARIOS VARCHAR (300))            
                     ''')
        messagebox.showinfo("BBDD", "Base de Datos creada con éxito")
    except:
        messagebox.showwarning("Atencion!", "La Base de Datos ya existe")
 

def salirAplicacion():
    valor=messagebox.askquestion("Salir", "Desea salir de la Aplicacion?")
    if valor =="yes":
        root.destroy()

root=Tk()
barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height=300)


bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionDB)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar Campos")

crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear")
crudMenu.add_command(label="Leer")
crudMenu.add_command(label="Actualizar")
crudMenu.add_command(label="Borrar")

ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Liciencia")
ayudaMenu.add_command(label="Acerca de ...")

#para q aparezcan en la barra de menu
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)


miFrame=Frame(root)
miFrame.pack()
# ==== label ============
idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(miFrame, text="Password:")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

comentarioLabel=Label(miFrame, text="Comentario:")
comentarioLabel.grid(row=5, column=0, sticky="en", padx=10, pady=10)

#====== Comienzo de campos=====


cuadroID=Entry(miFrame)
cuadroID.grid(row=0,column=1, padx=10,pady=10)

cuadroNombre=Entry(miFrame)
cuadroNombre.grid(row=1,column=1, padx=10,pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=2,column=1, padx=10,pady=10)
cuadroApellido.config(fg="red", justify="right")

cuadroPass=Entry(miFrame)
cuadroPass.grid(row=3,column=1, padx=10,pady=10)
cuadroPass.config(show="*", justify="right")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=4,column=1, padx=10,pady=10)
cuadroDireccion.config(fg="red", justify="right")

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=5,column=1, padx=10, pady=10)
scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=5, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)

miFrame2=Frame(root)
miFrame2.pack()

botonCrear=Button(miFrame2, text="CREATE")
botonCrear.grid(row=1, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="READ")
botonLeer.grid(row=1, column=1, sticky="e", padx=10, pady=10)

botonUpdate=Button(miFrame2, text="UPDATE")
botonUpdate.grid(row=1, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="DELETE")
botonBorrar.grid(row=1, column=3, sticky="e", padx=10, pady=10)
                 


root.mainloop()