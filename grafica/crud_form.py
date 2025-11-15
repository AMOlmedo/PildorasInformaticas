from tkinter import *
from tkinter import messagebox
import psycopg2


# ----- Funciones ---------------

def conexionDDBB():  
    try: 
        conexion_db = psycopg2.connect(
            host='localhost',
            port=5432, 
            database="formulario_db",
            user='postgres',
            password='postgres1234'
        )
        miCursor = conexion_db.cursor()    
        print("Conexión exitosa")
        messagebox.showinfo("DDBB", "Conexión exitosa a la DB")
        return conexion_db, miCursor
    except Exception as e:
        messagebox.showwarning("Atención", f"No se pudo conectar:ESTE MENSAJE ES DE LA EXECPCION !!!: {e} ") #captura el error
        return None, None


def salirAPP():
    valor=messagebox.askquestion("Salir", "Deseas salir de la App?")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    miNombre.set("")    # da una cadena vacia para limpiar el campo
    miApellido.set("")
    miTelefono.set("")
    miMail.set("")
    campoTexto.delete(1.0, END) # desde la posicion 1 hasta el final

def crear():
    conexion, cursor = conexionDDBB()
    if conexion and cursor:
        try:
            cursor.execute(
            "INSERT INTO user_table (nombre, apellido, telefono, email, mensaje) VALUES (%s, %s, %s, %s, %s)",
            (miNombre.get(), miApellido.get(), miTelefono.get(), miMail.get(), campoTexto.get("1.0", END).strip())
            )

            conexion.commit()
            messagebox.showinfo("BBDD", "Registro insertado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo insertar: {e}")
            print(e)
        finally:
            cursor.close()
            conexion.close()
def leer():
    conexion, cursor=conexionDDBB()
    if conexion and cursor:
        try:
            cursor.execute("SELECT * FROM user_table WHERE id=%s", (miId.get(),))
            registro=cursor.fetchall()
            if registro:
                miNombre.set(registro[1])
                miApellido.set(registro[2])
                miTelefono.set(registro[3])
                miMail.set(registro[4])
                campoTexto.delete(1.0, END)
                campoTexto.insert(END, registro[5])
            else:
                messagebox.showinfo("BBDD", "No se encontró el registro")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo leer: {e}")
            print(e)
        finally:
            cursor.close()
            conexion.close()

root=Tk()

#-----Creacion de la Barra de Menu -------
barraMenu=Menu(root) # asociamos a barraMenu la propiedad Menu para este root
root.config(menu=barraMenu, width=300, height=300) # asociamos la barra al root y el tamaño de la barra

menu_bd=Menu(barraMenu,tearoff=0)
menu_bd.add_command(label="conectar BD", command=conexionDDBB)
menu_bd.add_command(label="Salir", command=salirAPP)

menu_borrar=Menu(barraMenu,tearoff=0)
menu_borrar.add_command(label="Borrar", command=limpiarCampos)

menu_crud=Menu(barraMenu,tearoff=0)
menu_crud.add_command(label="Create", command=crear)
menu_crud.add_command(label="Read", command=leer)
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

miId=StringVar()
miNombre=StringVar()  #para poder manipular los datos de los entry
miApellido=StringVar()
miTelefono=StringVar()
miMail=StringVar()

campoId=Entry(miFrame, textvariable=miId)
campoId.grid(row=0, column=1, padx=10, pady=10)


campoNombre=Entry(miFrame, textvariable=miNombre)
campoNombre.grid(row=1, column=1, padx=10, pady=10)
campoNombre.config(fg="Green", justify= "right")

campoApellido=Entry(miFrame, textvariable=miApellido)
campoApellido.grid(row=2, column=1, padx=10, pady=10)
campoApellido.config(fg="Green", justify= "right")

campoTelefono=Entry(miFrame, textvariable=miTelefono)
campoTelefono.grid(row=3, column=1, padx=10, pady=10)
campoTelefono.config(fg="Green", justify= "right")

campoMail=Entry(miFrame, textvariable=miMail)
campoMail.grid(row=4, column=1, padx=10, pady=10)
campoMail.config(fg="Green", justify= "right")

campoTexto=Text(miFrame, width=16, height=5) # 16 caracteres  por 5 linas es el tamaño del campo Texto
campoTexto.grid(row=5, column=1, padx=10, pady=10)
scrollVertical=Scrollbar(miFrame, command=campoTexto.yview) #creacion barra de desplazamiento del campo de texto
scrollVertical.grid(row=5, column=2, sticky="ns")  # de north a south ( de arriba hasta abajo)
# sticky: Es una opción dentro del método grid() que determina cómo se comporta el widget si es más pequeño que la celda que se le ha asignado.
campoTexto.config(yscrollcommand=scrollVertical.set)

# ----- Comienzo Label de Campos ----

idLabel=Label(miFrame, text="ID:")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

telefonoLabel=Label(miFrame, text="Telefono:")
telefonoLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

mailLabel=Label(miFrame, text="E-Mail:")
mailLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

textoLabel=Label(miFrame, text="Mensaje:")
textoLabel.grid(row=5, column=0, sticky="n", padx=10, pady=10)

# ----botones CRUD----
miFrame2=Frame(root)    # Creamos un segundo Frame 
miFrame2.pack()

botonCrear=Button(miFrame2, text="CREATE",command=crear)
botonCrear.grid(row=0, column=0, sticky="e", padx=10, pady=10)

botonLeer=Button(miFrame2, text="READ", command=leer)
botonLeer.grid(row=0, column=1, sticky="e", padx=10, pady=10)

botonActualizar=Button(miFrame2, text="UPDATE")
botonActualizar.grid(row=0, column=2, sticky="e", padx=10, pady=10)

botonBorrar=Button(miFrame2, text="DELETE")
botonBorrar.grid(row=0, column=3, sticky="e", padx=10, pady=10)

root.mainloop()