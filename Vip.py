from Habitacion import Habitacion
class Vip(Habitacion):
    def __init__(self,ocupante,ocupada,pasillo,tipo = "Vip",capacidad = 0,costo = 0):
        self.pasillo = pasillo
        self.tipo = tipo 
        self.capacidad = capacidad
        self.costo = costo
        super().__init__(ocupante,ocupada)