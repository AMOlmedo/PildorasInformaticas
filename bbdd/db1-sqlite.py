import sqlite3
import os

#==== para que se vea la db creada ========
# Obtiene la ruta del directorio del script actual
directorio_script = os.path.dirname(os.path.abspath(__file__))
# Une el directorio con el nombre del archivo de la base de datos
ruta_bd = os.path.join(directorio_script, "personas2.db")
#=========================

miConexion=sqlite3.connect(ruta_bd)
miCursor=miConexion.cursor()

#miCursor.execute("CREATE TABLE personas2 (NOMBRE VARCHAR(50), EDAD INTEGER, PAIS VARCHAR(50))")
#miCursor.execute("INSERT INTO personas2 VALUES('Martina', 16, 'Argentina')")

#Para agregar varios registros de una vez. Se crea una lista con tuplas x cada registro
# variosPersonas=[
#     ("Adri", 52, "Argentina"),               
#     ("kuka", 10, "Bolivia"),               
#     ("Rita", 16, "Narnia")               
# ]
# miCursor.executemany("INSERT INTO personas2 VALUES(?,?,?)", variosPersonas) # tantos ? como campos existan

miCursor.execute("SELECT * FROM personas2")
variasConsulas=miCursor.fetchall()  #devuelve la consulta hecha en la linea anterior
#print(variasConsulas)

#otra forma de mostrar es:
for personas2 in variasConsulas:  #personas2 es la tabla
    print(personas2)

print("===================")

for personas2 in variasConsulas:
    print(personas2[0])

for personas2 in variasConsulas:
    print(personas2[1])

for personas2 in variasConsulas:
    print(personas2[2])
print("===================")
for personas2 in variasConsulas:
    print("Nombre: ", personas2[0], "Edad: ", personas2[1], "Pais: ", personas2[2])

miConexion.commit()
miConexion.close()