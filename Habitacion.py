class Habitacion():
    def __init__(self,tipo,capacidad,costo,pasillo,numero):
        '''Clase abstracta y padre de los objetos de tipo habitacion
        Parametros:
        --------------------------
        tipo: string, tipo de habitacion
        capacidad: int, capacidad de la habitacion
        costo: float, costo de la habitacion
        pasillo: string, pasillo de la habitacion
        numero, string, numero de la habitacion
        '''
        self.tipo = tipo 
        self.capacidad = capacidad
        self.costo = costo
        self.pasillo = pasillo 
        self.numero = numero
    
    def Type(self):
        '''Metodo encargado de retornar los datos de la habitacion'''
        info = []
        h = []
        info.append(self.tipo)
        h.append(self.pasillo)
        h.append(self.numero)
        hab = ".".join(h)
        info.append(hab)
        return info
        