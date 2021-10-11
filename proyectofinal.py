print ('''\n
    #####################################################################
    #                                                                   #
    #          Bievenido al Sistema de inventario Computo Plus          #
    #                                                                   #
    #####################################################################''')
inventario = {}
continuar = True
while continuar:
    menu = int(input('''\n
    ===============================================
                    Menu Principal
    ===============================================

    1.- ** Listar Existencia del Inventario **
    2.- ** Agregar Un nuevo elemento al Inventario **
    3.- ** Actualizar Un elemento del Inventario **
    4.- ** Modificar Un elemento del Inventario **
    5.- ** Salir de la Aplicación **

    Seleccione la opcion que desea: '''))

    if(menu == 1):
        print('\n******* Lista de Productos *******')
        print(f'''
        ==================================================================
        {inventario}
        ==================================================================''')
        if (menu != 5):
            menuPrincipal = str(input('\nRegresar al menu Principal? S/N\n'))
            if (menuPrincipal == 'S' or menuPrincipal == 's'):
                pass
            else:
                continuar = False
                print('''
                    =======================================================
                    xxx   Saliendo.... Has Salido de la Aplicación      xxx
                    =======================================================''')
    elif(menu == 2):
        print('******* Digite los nuevos registros *******')
        id = int(input('Ingrese el id: '))
        inventario['ID'] = id
        nombre = str (input('Digite el Nombre del Producto: '))
        inventario['Producto'] = nombre
        proveedor = str (input('Digite proveedor: '))
        inventario['Proveedor'] = proveedor
        existencia = int (input('Digite Existencia del Producto: '))
        inventario['Cantidad'] = existencia
        print('''\n
         ================
         Datos Ingresados
         ================''')
        if (menu != 5):
            menuPrincipal = str(input('\nRegresar al menu Principal? S/N\n'))
            if (menuPrincipal == 'S' or menuPrincipal == 's'):
                pass
            else:
                continuar = False
                print('''
                    =======================================================
                    xxx   Saliendo.... Has Salido de la Aplicación      xxx
                    =======================================================''')
    elif(menu == 3):
        print('\n******* Actualizar los registros *******\n')
        act = int(input('Seleccione los datos a Actualizar: 1- Producto, 2- Proveedor, 3- cantidad\n'))
        if (act == 1):
            nombreproducto = str (input('Digite el Nombre del Producto: '))
            inventario.update(({'Producto': nombreproducto}))
        elif(act == 2):
            proveedores = str (input('Digite proveedor: '))
            inventario.update(({'Proveedor': proveedores}))
        elif (act == 3):
            existencias = int (input('Digite Existencia del Producto: '))
            inventario.update(({'Cantidad': existencias}))
        print('''\n
         ===================
         Datos Actualizados.
         ===================''')
        if (menu != 5):
            menuPrincipal = str(input('\nRegresar al menu Principal? S/N\n'))
            if (menuPrincipal == 'S' or menuPrincipal == 's'):
                pass
            else:
                continuar = False
                print('''
                    =======================================================
                    xxx   Saliendo.... Has Salido de la Aplicación      xxx
                    =======================================================''')
    elif (menu == 4):
        print('******* Modificar los Registros *******')
        nombre = str (input('Digite el Nombre del Producto: '))
        inventario['Producto'] = nombre
        proveedor = str (input('Digite proveedor: '))
        inventario['Proveedor'] = proveedor
        existencia = int (input('Digite Existencia del Producto: '))
        inventario['Cantidad'] = existencia
        print('''\n
         =================
         Datos Modificados
         =================''')
        if (menu != 5):
            menuPrincipal = str(input('\nRegresar al menu Principal? S/N\n'))
            if (menuPrincipal == 'S' or menuPrincipal == 's'):
                pass
            else:
                continuar = False
                print('''
                    =======================================================
                    xxx   Saliendo.... Has Salido de la Aplicación      xxx
                    =======================================================''')
    else:
        (menu == 5)
        print('''\n
            =======================================================
            xxx   Saliendo.... Has Salido de la Aplicación      xxx
            =======================================================''')
        exit()
