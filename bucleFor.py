semana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
for dia in semana:
    print(dia)

cantidad = int(input('Digite la Cantidad de Personas:\n'))
nombre = []
salario = []
for x in range(cantidad):
    nom = str(input('Ingrese su Nombre:\n'))
    nombre.append(nom)
    sueldo = float(input('Ingrese su Salario:\n'))
    salario.append(sueldo)
print(nombre)