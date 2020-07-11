from Tour import Tour
from Restaurante import Restaurante
class Crucero():
    def __init__(self,nombre,ruta,fecha,boletos,cantidad_sencilla,cantidad_premium,cantidad_vip,tours = [],restaurante = False):
        self.nombre = nombre
        self.ruta = ruta
        self.fecha = fecha
        self.boletos = boletos
        self.cantidad_sencilla = cantidad_sencilla
        self.cantidad_premium = cantidad_premium
        self.cantidad_vip = cantidad_vip
        self.tours = tours
        self.restaurante = restaurante

    
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
        if len(self.tours) == 0:
            puerto = Tour("Tour Puerto",30,10,"7 Am")
            self.tours.append(puerto)
            return self.tours
        else:
            return self.tours
    
    def Restaurante(self):
        if self.restaurante == False:
            self.restaurante = Restaurante()
            return self.restaurante
        else:
            return self.restaurante

    