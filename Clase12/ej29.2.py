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
    
class Administrador(Usuario):
    privilegios = ["puede agregar publciaciones","puede eliminar publciaciones", "puede bloquear usuarios"]
    
    def mostrar_privilegios(self):
        print(f"El usuario {self.nombre} {self.apellido} tiene los siguientes privilegios: {self.privilegios}")

Admin = Administrador("Agustin", "Quintela")

Admin.mostrar_privilegios()
