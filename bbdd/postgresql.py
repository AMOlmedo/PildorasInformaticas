import psycopg2

try:
    conexion_db=psycopg2.connect(
        host='localhost',
        port=5432, 
        database="clientes_db",
        user='postgres',
        password='12345',
        database='prueba'
    )
    print("conexion exitosa")
    
except Exception as ex:
    print(ex)
finally:
    conexion_db.close()
    print("conexion finalizada")

    