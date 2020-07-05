from Habitacion import Habitacion
class Premium(Habitacion):
    def __init__(self,ocupante,ocupada,pasillo,tipo = "Premium",capacidad = 0,costo = 0):
        self.pasillo = pasillo 
        self.tipo = tipo 
        self.capacidad = capacidad
        self.costo = costo
        super().__init__(ocupante,ocupada)