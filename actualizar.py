import psycopg2

conexion = psycopg2.connect(database = 'Prueba', user='postgres', password='1234', host='127.0.0.1', port='5432')
print ('Conexion Exitosa')

cursor = conexion.cursor()

cursor.execute (''' UPDATE prueba set nombre = 'Jose' where id = '123' ''')
conexion.commit()
print('Cantidad de filas modificadas: ', cursor.rowcount)

print('Cambio Exitoso')

conexion.close()