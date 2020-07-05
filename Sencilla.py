from Habitacion import Habitacion
class Sencilla(Habitacion):
    def __init__(self,ocupante,ocupada,pasillo,tipo = "Sencilla",capacidad = 0,costo = 0):
        self.pasillo = pasillo
        self.tipo = tipo
        self.capacidad = capacidad
        self.costo = costo
        super().__init__(ocupante,ocupada)