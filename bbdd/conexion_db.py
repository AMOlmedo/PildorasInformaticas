# modelo para la creacion de una Base de Datos
import sqlite3
import os
from tkinter import messagebox

ubicacion_db = os.path.dirname(os.path.abspath(__file__)) 
ruta_bd = os.path.join(ubicacion_db, "nombreBaseDatos.db")  # Asegurate de usar .db

def conexionBD():
    miConexion = sqlite3.connect(ruta_bd)
    miCursor = miConexion.cursor()
    try:
        miCursor.execute('''
        CREATE TABLE cliente(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE VARCHAR(50),
            APELLIDO VARCHAR(50),
            TELEFONO INTEGER,
            DIRECCION VARCHAR(100),
            COMENTARIOS VARCHAR(300)
        )
        ''')
        miConexion.commit()
        messagebox.showinfo("BBDD", "Base de Datos creada con éxito")
    except:
        messagebox.showwarning("Atención!", "La Base de Datos ya existe")
    finally:
        miConexion.close()

conexionBD()

print(f"Ruta de la base de datos: {ruta_bd}")
print("¿Existe la base de datos?", os.path.exists(ruta_bd))



               