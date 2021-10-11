num = int(input('Ingrese un numero\n'))
x = 1

while(x <= num):
    print(f'El recorrido es {x}')
    x = x+1
print('************** FIN *************')

clave = int (input('Ingrese su contraseña:\n'))
while(clave != 123):
    clave = int(input(f'Contraseña Incorrecta, Intente de Nuevo'))
print('Contraseña Correcta')