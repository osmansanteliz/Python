precio1 = float(input('Ingrese el valor de la manzaza en pali:\n'))
precio2 = float (input('Ingrese el precio de la manzana en super la colonia:\n'))

if (precio1 < precio2):
    ahorro = precio2 - precio1
    print (f'Las manzanas en el pali siempre son mas baratas, ({ahorro}) Cordobas de ahorro en el pali')
else :
    derroche = precio1 - precio2
    print (f'no se que pasa con los precios del pali ({derroche}) Cordobas mas en el pali')    