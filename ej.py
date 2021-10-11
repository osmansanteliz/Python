trabajadores = []
sal = []
print ('\n Bievenidos\n')
clave = str (input('Desea Continuar:? S/N\n'))
while (clave == 's' or 'S'):
    print('\n ++ Si desea salir la cantidad tiene que ser 0 ++\n')
    cantidad = int(input('Ingrese la cantidad de trabajadores:\n'))
    if (cantidad == 0):
            print('++ final de la aplicaciòn ++')
            exit()
    else:   
        for x in range(cantidad): 
            nombre = str (input('Digite el nombre del Trabajador:\n'))
            trabajadores.append(nombre)
            edad = int (input('Digite edad del trabajador:\n'))
            trabajadores.append(edad)
            salario = float (input('Digite el salario del trabajador:\n'))
            sal.append(salario)
            print(trabajadores)
        for y in (sal):
            sal.reverse
            print(sal)
print('++ Fin ++')            
