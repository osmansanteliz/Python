import psycopg2

conexion = psycopg2.connect(database = 'Prueba', user='postgres', password='1234', host='127.0.0.1', port='5432')
print ('Conexion Exitosa')

cursor = conexion.cursor()

cursor.execute (''' SELECT FROM prueba''')
rows = cursor.fetchall()

for row in rows:
    print('id =', row[0])
    print('nombre =', row[1])
    print('apellido =', row[2], '\n')

print('Consulta Exitosa')

conexion.commit()
conexion.close()