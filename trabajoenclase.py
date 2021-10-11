nombre1 = str(input('Ingrese el nombre del primer estudiante: \n') )
nombre2 = str(input('Ingrese el nombre del segundo estudiante: \n'))
nombre3 = str(input('Ingrese el nombre del tercer alumno: \n'))
nota1 = int(input(f'Ingrese la nota de {nombre1}\n'))
nota2 = int(input(f'Ingrese la nota de {nombre2}\n'))
nota3 = int(input(f'Ingrese la nota de {nombre3}\n'))

if (nota1 > nota2):
    print (f'{nombre1} Tiene la calificacion mas alta {nota1}')
elif (nota1 > nota3):
    print(f'{nombre2} Tiene la calificacion mas alta {nota2}')      
else:
    print(f'{nombre3} Tiene la Nota mas alta {nota3}')
if (nota1 < nota2 and nota1 < nota3):
    print (f'{nombre1} Tiene la calificacion mas baja {nota1}')
elif (nota2 < nota1 and nota2 < nota3):
    print (f'{nombre2} Tiene la calificacion mas baja {nota2}') 
else :
    print (f'{nombre3} Tiene la calificacion mas baja {nota3}')
if (nota1 == nota2):
    print (f'{nombre1} , {nombre2} Tienen la misma calificacion {nota1}')
elif (nota2 == nota3):
    print (f'{nombre2} Y {nombre1} Tienen la misma calificacion {nota2}')     
else :
    print (f'{nombre3} y {nombre1} Tienen la misma calificacion {nota3}')                