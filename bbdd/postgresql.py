import psycopg2

try:
    conexion_db=psycopg2.connect(
        host='localhost',
        user='postgres',
        ##password='',
        database='prueba'
    )
    print("conexion exitosa")
except Exception as ex:
    print(ex)
finally:
    conexion_db.close()
    print("conexion finalizada")

    