import sqlite3
import os

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_bd = os.path.join(directorio_script, "gestionPersMascotas.db")

miConexion=sqlite3.connect(ruta_bd)
miCursor=miConexion.cursor()
#C.R.U.D  (Create. Read. Update. Delete) 
#CREATE en este caso ya esta creada en db3-sqlite.py

#READ
miCursor.execute("SELECT * FROM miembros WHERE NOMBRE='marti'")
name=miCursor.fetchall()    
print(name)

#UPDATE
#cambiamo el nombre de miti por moco  en la tabla miembros
miCursor.execute("UPDATE miembros SET NOMBRE='moco' WHERE NOMBRE='miti'") #cuidado con las comillas!!

#DELETE
# borramos el registo con el NOMBRE='moco'
miCursor.execute("DELETE FROM miembros WHERE NOMBRE='moco' ")
tabla_miembros=miCursor.fetchall()
print(tabla_miembros)

miConexion.commit()
miConexion.close()