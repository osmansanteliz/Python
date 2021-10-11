lista = ["Osman", ["Santeliz"], ["Rivera"] , 32 , 88.9]
print (lista)
print "Nombre:", lista[0]
print "Primer Apellido:", lista[1]
print "Primer Apellido:", lista[1][0] 
print "Segundo Apellido:", lista [2]
print "Edad:", lista[3]
#append, metodo que agrega un valor de ultimo a nuestra lista
lista.append(3)
print "Agregado numero 3 a la lista:", lista
#Metodo len cuenta el numero de elementos en la lista
print "Contando el numero de elementos de la lista:", len(lista)
#count recibe un elemento como argumento y cuenta la cantidad de veces que aparece en la lista
print "Argumento indice 1:", lista.count(1)
#reverse() incompleto
#sort() ordena los elementos de una lista
lista.sort()
print "Ordenando la lista:", lista
#remove() elimina un elemento
print "eliminado el elemento en el indice 3:", lista.remove(3)
print lista
#pop, muestra el ultimo elemento de la lista
print "Mostrando el ultimo elemento de la lista:", lista.pop()
#insert() inserta el elemento x en la lista en el indice i (posicion, nuevo valor)
print "insertando elementos:", lista.insert(0,'1')
#Index devuelve el numero del indice del elemento que le pasemos como parametro
print "Indice del elemento:", lista.index(32)
#extends extiende una lista agregando un iterable al final
print "Agregando a la lista:", lista.extend("Gerardo")
print "Elementos finales de la lista:", lista