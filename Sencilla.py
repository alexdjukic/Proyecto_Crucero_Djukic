from Habitacion import Habitacion
class Sencilla(Habitacion):
    def __init__(self,tipo,capacidad,costo,pasillo,numero,ocupada = False):
        self.ocupada = ocupada
        super().__init__(tipo,capacidad,costo,pasillo,numero)

    def Info(self):
        return f'''------ Informacion de la Habitacion ------
                    Tipo: {self.tipo}
                    Capacidad: {self.capacidad} personas
                    Costo: {self.costo}$
                    Pasillo: {self.pasillo}
                    Numero Habitacion: {self.numero}'''
    def Request_room(self):
        habitacion = []
        hab = []
        tipo = self.tipo
        habitacion.append(tipo)
        pasillo = self.pasillo
        hab.append(pasillo)
        numero = self.numero
        hab.append(numero)
        hab = ".".join(hab)
        habitacion.append(hab)
        return habitacion


    def Datos(self):
        data = []
        data.append(self.tipo)
        data.append(str(self.capacidad))
        data.append(str(self.costo))
        data.append(self.pasillo)
        data.append(self.numero)
        return data
    