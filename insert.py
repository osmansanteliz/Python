import psycopg2

conexion = psycopg2.connect(database = 'Prueba', user='postgres', password='1234', host='127.0.0.1', port='5432')
print ('Conexion Exitosa')

cursor = conexion.cursor()

cursor.execute (''' INSERT INTO prueba (id, nombre, apellido) VALUES (123, 'Osman', 'Santeliz')); ''')

print('Datos Insertados exitosamente')

conexion.commit()
conexion.close()