class Humano():
  def _init_(self, edad, nombre, ocupacion):
    self.edad = edad
    self.nombre = nombre
    self.ocupacion = ocupacion

def presentar(self):
  presentacion = ('Hola soy {self.nombre}, mi edad es {self.edad} y mi ocupacion es {self.ocupacion}')

def contratar(self, puesto):
    self.puesto = puesto
    print('{self.puesto} ha sido contratado como {self.ocupacion}'.format(self.nombre, self.puesto))
    self.ocupacion = puesto
Personal = Humano(32, 'Osman', 'Ingeniero en Sistemas')
Personal.presentar()
Personal.contratar('Obrero')
Personal.presentar()
