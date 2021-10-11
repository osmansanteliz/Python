def cambioMoneda():
    print(' \n************ Bienvenido al Sistema de Cambio de Moneda ************\n')
    moneda = int(input('+++++++ Cordoba a Dolares elija 1, Dolares a Cordobas elija 2: +++++++\n'))
    dol = 35.25
    while(moneda == 1):
        if (moneda != 1 or 2):
            print('++ final de la aplicaciòn ++')
            exit()
        cor = float (input('Digite la cantidad en cordobas\n'))
        cambio = cor/dol
        print(f'El cambio es: {cambio} Dolares')
    else:
        dolar = float (input('Digite la cantidad en dolares que desea cambiar:\n'))
        cambio = dol * dolar
        print(f'EL cambio es: {cambio} Cordobas')
cambioMoneda()
