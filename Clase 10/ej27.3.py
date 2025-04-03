class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    def describir_usuario(self):
        print(f"El usuario se llama {self.nombre} {self.apellido}"
              )
    def saludar_usuario(self):
        print(f"Buenas tardes {self.nombre} {self.apellido}, como estas el dia de hoy?")

usuario1 = Usuario("Agustin", "Quintela")
usuario2 = Usuario("Julieta", "Rossney")

usuario1.describir_usuario()
usuario1.saludar_usuario()
print("")
usuario2.describir_usuario()
usuario2.saludar_usuario()