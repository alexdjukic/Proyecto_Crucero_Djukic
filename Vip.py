from Habitacion import Habitacion
class Vip(Habitacion):
    '''Clase hija de Habitacion encargada de crear los objetos de tipo Vip
        Parametros:
        ---------------------------
        Hereda los atributos de la clase Habitacion
        ocupada: bool, indica si la habitacion esta ocupada o no'''
    def __init__(self,tipo,capacidad,costo,pasillo,numero,ocupada = False):
        self.ocupada = ocupada
        super().__init__(tipo,capacidad,costo,pasillo,numero)
    
    def Info(self):
        '''Metodo encargado de retornar la informacion de la habitacion'''
        return f'''------ Informacion de la Habitacion ------
                    Tipo: {self.tipo}
                    Capacidad: {self.capacidad} personas
                    Costo: {self.costo}$
                    Pasillo: {self.pasillo}
                    Numero Habitacion: {self.numero}'''
    
    def Request_room(self):
        '''Metodo encargado de recopilar los datos de la habitacion para ser utilizadps para ocupar la habitacion'''
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
        '''Metodo encargado de recopilar los datos de la habitacion para escribirlos en el txt'''
        data = []
        data.append(self.tipo)
        data.append(str(self.capacidad))
        data.append(str(self.costo))
        data.append(self.pasillo)
        data.append(self.numero)
        return data