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
    
class Privilegios:
    def __init__(self, privilegios):
        self.privilegios = privilegios
    
    def mostrar_privilegios(self):
        print(f"Este usuario tiene los siguientes privilegios:")
        for privilegio in self.privilegios:
            print(privilegio)
    
class Administrador(Usuario):
    def __init__(self, nombre, apellido, privilegios):
        super().__init__(nombre, apellido)
        self.privilegios = Privilegios(privilegios)


admin = Administrador("Agustin", "Quintela", ["puede agregar publciaciones","puede eliminar publciaciones", "puede bloquear usuarios"])
admin.describir_usuario()
admin.privilegios.mostrar_privilegios()