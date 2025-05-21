from ej29_3 import Usuario, Privilegios
class Administrador(Usuario):
    def __init__(self, nombre, apellido, privilegios):
        super().__init__(nombre, apellido)
        self.privilegios = Privilegios(privilegios)
