diccionario2 = {"Nombre": "Lesly", "Edad": 23, "Padres": ["Cesar", "Eveling"]}
print (f"Nombre: {diccionario2 ['Nombre']}")
print (f"Edad: {diccionario2 ['Edad']}")
print (f"Padres: {diccionario2 ['Padres']}")
#cambiar el nombre
diccionario2 ['Nombre'] = 'Keysell'
print (f'Nuevo Nombre: {(diccionario2)}')
#Metodo dict() recibe como parametro una representacion de un diccionario y si es factible devuelve un diccionario de datos
diccionario3 = dict(Nombre = 'Osman', edad = 32 , Padres = 'Cesar')
print (f'Metodo dict: {diccionario3}')
diccionario4 = dict(zip ('abcd', [1,2,3,4]))
print (f'Diccionario comprimido: {diccionario4}')
#item devuelve una lista de tuplas, cada tupla se compone de dos elementos, clave y valor en ese orden
print (f'metdo item: {diccionario3.items()}')
#copy() retorna una copia del diccionario original
dic = diccionario4.copy()
print (f'copiando el diccionario: {diccionario4.copy()}')
#fromkeys 
dic = dict.fromkeys(['a', 'b', 'c', 'd', 1])
print (f'metodo from keys: {dic}')
#values() retorna una lista de elementos que seran los valores de nuestro diccionario
print(f'Metodo Values: {dic.values()}')
#get() devuelve el valor de la clave si no lo encuentra devuelve none
print (f'Metodo get: {dic.get()}')
#update si se tienen claves iguales actualiza el valor d ela clave repetida, si no hay claves iguales el par clave valor es agregado
print(f'Metodo update: {dic.update()}')