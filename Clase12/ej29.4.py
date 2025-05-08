class Auto:
    """Inicializa los atributos para describir un auto."""
    def __init__(self, marca, modelo, año):
        """Inicializa los atributos para describir un auto."""
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.kilometraje = 0  

class AutoElectrico(Auto):
    """Representa aspectos de un auto, específicos de los vehículos eléctricos."""
    def __init__(self, marca, modelo, año):
        """Inicializa los atributos de la clase padre.
        Luego inicializa los atributos específicos de un auto eléctrico.
        """
        super().__init__(marca, modelo, año)
        self.bateria = Bateria()

    def obtener_autonomia(self):
        self.bateria.obtener_autonomia() 

    def actualizar_bateria(self):
        self.bateria.actualizar_bateria()  
        
class Bateria:
    def __init__(self, capacidad_bateria=40):
        self.capacidad_bateria = capacidad_bateria

    def describir_bateria(self):
        print(f"Este auto tiene una batería de {self.capacidad_bateria} kWh.")

    def obtener_autonomia(self):
        if self.capacidad_bateria == 40:
            rango = 150
        elif self.capacidad_bateria == 65:
            rango = 225
        print(f"Este auto tiene una autonomía de {rango} kilómetros.")

    def actualizar_bateria(self):
        if self.capacidad_bateria < 65:
            self.capacidad_bateria = 65  
            print("La batería ha sido actualizada a 65 kWh.")


MiAuto = AutoElectrico("Fiat", "Punto", 2021)

MiAuto.obtener_autonomia()
MiAuto.actualizar_bateria()
MiAuto.obtener_autonomia()
