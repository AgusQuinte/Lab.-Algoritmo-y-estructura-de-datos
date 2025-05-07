class Restaurante:
    def __init__(self, nombre, cocina):
        self.nombre = nombre
        self.cocina = cocina
        
    def describir_resto(self):
        print(f"El nombre del restaurante es {self.nombre} y tiene un tipo de cocina {self.cocina}")
        
    def abrir_resto(self):
        print("¡El restaurante está abierto!")
    
resto1 = Restaurante("La popular", "General")
resto2 = Restaurante("Parrila loca", "Parrilla")
resto3 = Restaurante("McDonalds", "Comida rapida")

resto1.describir_resto()
resto2.describir_resto()
resto3.describir_resto()