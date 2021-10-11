class Producto():
  def ingresar(self):
    print('\n** Ingrese los datos del Producto')
    self.nombre = str(input('Nombre del producto'))
    self.marca = str(input('Marca del Producto'))
    self.estado = str(input('Estado del Producto: *'))

  def Mostrar(self):
      print('\n** Los datos del producto son: **')
      print(f'Nombre del producto: {self.nombre}')
      print(f'Marca del Producto: {self.marca}')
      print(f'Estado del Producto: {self.estado}')

  def Actualizar(self):
    print('\n** Actualizar datos: **')    
    self.nom = str(input('Nombre del Producto: '))
    self.mrc = str(input('Marca del Producto: '))
    self.est = str(input('Estado del Producto: '))
    self.nombre = self.nom
    self.marca = self.mrc
    self.estado = self.est
    print('\n** Actualizacion realizada **')
    self.Mostrar()
Objeto = Producto()
Objeto.ingresar()
Objeto.Mostrar()
Objeto.Actualizar()    