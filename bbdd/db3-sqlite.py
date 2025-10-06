import sqlite3
import os

directorio_script = os.path.dirname(os.path.abspath(__file__))
ruta_bd = os.path.join(directorio_script, "gestionPersonas.db")

miConexion=sqlite3.connect(ruta_bd)
miCursor=miConexion.cursor()

miCursor.execute('''
    CREATE TABLE personajes (
                 CODIGO INTEGER PRIMARY KEY,
                 NOMBRE VARCHAR(30),
                 EDAD INTEGER,
                 PAIS VARCHAR(50))
                 ''')

personajesLista=[
        (1, "adrian", 52, "arg"),
        (2, "marti", 16, "arg"),
        (3, "kuka", 10, "bol"),
        (4, "rita", 16, "usa")
]
    
miCursor.executemany("INSERT INTO personajes VALUES(?,?,?,?)", personajesLista)

miConexion.commit()
miConexion.close()
