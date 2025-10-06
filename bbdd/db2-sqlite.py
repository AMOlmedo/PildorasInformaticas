import sqlite3
import os

# Obtiene la ruta del directorio del script actual
directorio_script = os.path.dirname(os.path.abspath(__file__))
# Une el directorio con el nombre del archivo de la base de datos
ruta_bd = os.path.join(directorio_script, "Produccion2.db")

miConexion = sqlite3.connect(ruta_bd)
miCursor = miConexion.cursor()

miCursor.execute("CREATE TABLE IF NOT EXISTS PRODUCTOS (NOMBRE VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miConexion.commit()
miConexion.close()

print(f"Base de datos creada en: {ruta_bd}")
