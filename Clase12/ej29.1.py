class Restaurante:
    def __init__(self, nombre, cocina):
        self.nombre = nombre
        self.cocina = cocina
        
    def describir_resto(self):
        print(f"El nombre del restaurante es {self.nombre} y tiene un tipo de cocina {self.cocina}")
        
    def abrir_resto(self):
        print("¡El restaurante está abierto!")

class PuestoDeHelados(Restaurante):

    def mostrar_sabores():