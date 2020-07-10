from Tour import Tour
from Restaurante import Restaurante
class Crucero():
    def __init__(self,nombre,ruta,fecha,boletos,cantidad_sencilla,cantidad_premium,cantidad_vip):
        self.nombre = nombre
        self.ruta = ruta
        self.fecha = fecha
        self.boletos = boletos
        self.cantidad_sencilla = cantidad_sencilla
        self.cantidad_premium = cantidad_premium
        self.cantidad_vip = cantidad_vip
    
    def Cupos(self,clientes):
        if self.boletos == 0:
            return "No hay mas cupos en este barco"
        else:
            self.boletos -= clientes
            return "Se han registrado a los {} viajeros en el {}".format(clientes,self.nombre)

    def Info_Barco(self):
        return """   ------- Infromacion del Barco -------
        
                    Nombre : {}
                    Ruta: {}
                    Fecha de Salida: {}
                    Boletos Disponibles: {} 
                    Cantidad de habitaciones Sencillas: {}
                    Cantidad de habitaciones Premium: {}
                    Cantidad de habitaciones VIP: {}
                    
                    """.format(self.nombre,self.ruta,self.fecha,self.boletos,self.cantidad_sencilla,self.cantidad_premium,self.cantidad_vip)
    def Nombre(self):
        return self.nombre

    def Tours(self):
        tours = []
        puerto = Tour("Tour Puerto",30,10,"7 Am")
        tours.append(puerto)

        return tours
    
    def Restaurante(self):
        restaurante = Restaurante()
        return restaurante

    