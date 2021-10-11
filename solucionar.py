class Mascota():
    def _init_(self, nombre, edad):
        self.nombre = str(input('Cual es el nombre de la mascota?\n'))
        self.edad = int(input('Cual es la edad de la mascota?\n'))

    def mostrarDatos(self):
        print(f'Nombre {self.nombre} \n Edad: {self.edad} \n')