import sqlite3
import os

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_bd = os.path.join(directorio_script, "gestionPersMascotas.db")

miConexion=sqlite3.connect(ruta_bd)
miCursor=miConexion.cursor()

miCursor.execute('''    
    CREATE TABLE miembros (
                 ID INTEGER PRIMARY KEY AUTOINCREMENT,
                 NOMBRE VARCHAR(30),
                 EDAD INTEGER,
                 PAIS VARCHAR(50))
                 ''')
# la triple  ''' es para poder escribir en varias lineas las sentencia de sql
personajesLista=[
        ("adrian", 52, "arg"),
        ("marti", 16, "arg"),
        ("kuka", 10, "bol"),
        ("rita", 16, "usa"),
        ("miti", 10, "chi")

]
    
miCursor.executemany("INSERT INTO miembros VALUES(NULL,?,?,?)", personajesLista)

miConexion.commit()
miConexion.close()
