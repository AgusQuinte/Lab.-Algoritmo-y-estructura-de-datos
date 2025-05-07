class Restaurante:
    def __init__(self, nombre, cocina):
        self.nombre = nombre
        self.cocina = cocina
        
    def describir_resto(self):
        print(f"El nombre del restaurante es {self.nombre} y tiene un tipo de cocina {self.cocina}")
        
    def abrir_resto(self):
        print("¡El restaurante está abierto!")

# Crear una instancia de Restaurante
Resto = Restaurante("Siga la vaca", "Tenedor libre")

# Imprimir el nombre del restaurante
print(f"El restaurante se llama {Resto.nombre}")

# Llamar y ejecutar los métodos correctamente
Resto.abrir_resto()
Resto.describir_resto()
