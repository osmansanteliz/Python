print ('\n++++ Bienvenidos al banco industrial python ++++\n')
datosAprobados = []
datosNoAprobados = []
continuar = str (input('Deseas registrar un nuevo prestamo S/N?\n'))
while (continuar == 's'):
    if (continuar != 's'):
            print('++ final de la aplicaciòn ++')
            exit()
    nombre = str (input('Digite el Nombre del Solicitante del Prestamo:\n'))
    cedula = str (input(f'Digite Numero de Cedula del Solicitante {nombre}\n'))
    ingreso = int (input('\nDigite los Ingresos Mensuales:\n'))
    if (ingreso > 5000):
        datosAprobados.append(nombre)
        datosAprobados.append(cedula)
        datosAprobados.append(ingreso)
        print (f'\n+++++++++++ Bienvenidos a nuestro sistema de prestamos,{nombre} es elegible para aplicar al puesto +++++++++++\n')
        print ('+++++++++++++ Prestamos Aprobados +++++++++++++\n')
        print(datosAprobados)
        print('\n')
    else:
        print('+++++++++++++ Prestamos Rechazados +++++++++++++\n')
        datosNoAprobados.append(nombre)
        datosNoAprobados.append(cedula)
        datosNoAprobados.append(ingreso)
        print(datosNoAprobados)
        print('\n++++ No aplica al prestamo, gracias por su interes en nuestro banco ++++\n')
print('++++++++ Has salido de aplicaciòn ++++++++')
