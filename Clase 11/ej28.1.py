class Restaurante:
    def __init__(self, nombre, cocina,):
        self.nombre = nombre
        self.cocina = cocina
        self.clientes = 0
    def establecer_clientes_atendidos(self, clientes):
        self.clientes = clientes
        print(clientes, "clientes atendidos")
    def incrementar_clientes(self, cliente,):
        self.clientes += cliente
        print(self.clientes)
    def describir_resto(self):
        print(f"El nombre del restaurante es {self.nombre} y tiene un tipo de cocina {self.cocina}. Clienes atendidos del dia de hoy: {self.clientes}")
        
    def abrir_resto(self):
        print("¡El restaurante está abierto!")

# Crear una instancia de Restaurante
Resto = Restaurante("Siga la vaca", "Tenedor libre")

# Imprimir el nombre del restaurante
print(f"El restaurante se llama {Resto.nombre}")

# Llamar y ejecutar los métodos correctamente
Resto.abrir_resto()
Resto.describir_resto()
Resto.establecer_clientes_atendidos(2)
Resto.incrementar_clientes(1)