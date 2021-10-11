import psycopg2

conexion = psycopg2.connect(database = 'Prueba', user='postgres', password='1234', host='127.0.0.1', port='5432')
print ('Conexion Exitosa')

cursor = conexion.cursor()

cursor.execute ('''
                    create table prueba(
                    id int,
                    nombre varchar(50),
                    apellido varchar(50));
                ''')

print('Tabla creada exitosamente')

conexion.commit()
conexion.close()