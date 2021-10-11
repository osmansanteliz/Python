class Ataque:
    def _init_ (self, ip, puerto):
        self.ip = ip
        self.puerto = puerto
    def mostrar(self):
            while true:
                    print(f'\nAtaque al host {self.ip} en el puerto {self.puerto}')
                    print('Warning Infected')
A = Ataque('172.217.164.36', 5023)
A.mostrar() 