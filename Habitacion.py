class Habitacion():
    def __init__(self,tipo,capacidad,costo,pasillo,numero):
        self.tipo = tipo 
        self.capacidad = capacidad
        self.costo = costo
        self.pasillo = pasillo 
        self.numero = numero
    
    def Type(self):
        info = []
        h = []
        info.append(self.tipo)
        h.append(self.pasillo)
        h.append(self.numero)
        hab = ".".join(h)
        info.append(hab)
        return info
        