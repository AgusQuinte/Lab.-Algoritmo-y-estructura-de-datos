class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.intentos_login = 0
    
    def describir_usuario(self):
        print(f"El usuario se llama {self.nombre} {self.apellido}")
    
    def saludar_usuario(self):
        print(f"Buenas tardes {self.nombre} {self.apellido}, ¿cómo estás el día de hoy?")
    
    def incrementar_intentos_login(self, intento):
        self.intentos_login += intento
        print(self.intentos_login)
    
    def reiniciar_intentos_login(self):
        self.intentos_login = 0
        print(self.intentos_login)

usuario1 = Usuario("Agustin", "Quintela")
usuario2 = Usuario("Julieta", "Rossney")

usuario1.describir_usuario()
usuario1.saludar_usuario()
print("")
usuario2.describir_usuario()
usuario2.saludar_usuario()

usuario1.incrementar_intentos_login(1)
usuario1.incrementar_intentos_login(1)
usuario1.incrementar_intentos_login(1)
usuario1.incrementar_intentos_login(1)
usuario1.reiniciar_intentos_login()  
