from Tour import Tour
from Restaurante import Restaurante
class Crucero():
    def __init__(self,nombre,ruta,fecha,n_habitacion,cantidad_sencilla,costo_simple,cantidad_premium,costo_premium,cantidad_vip,costo_vip,tours = [],restaurante = False):
        self.nombre = nombre
        self.ruta = ruta
        self.fecha = fecha
        self.n_habitacion = n_habitacion
        self.cantidad_sencilla = cantidad_sencilla
        self.costo_simple = costo_simple
        self.cantidad_premium = cantidad_premium
        self.costo_premium = costo_premium
        self.cantidad_vip = cantidad_vip
        self.costo_vip = costo_vip
        self.tours = tours
        self.restaurante = restaurante

    
    
    def Info_Barco(self):
        return f"""   ------- Infromacion del Barco -------
        
                    Nombre : {self.nombre}
                    Ruta: {self.ruta}
                    Fecha de Salida: {self.fecha}
                    Rooms: {self.n_habitacion}
                    Capacidad de habitaciones Sencillas: {self.cantidad_sencilla} personas
                    Costo habitaciones Sencillas: {self.costo_simple}$
                    Capacidad de habitaciones Premium: {self.cantidad_premium} personas
                    Costo habitaciones Premium: {self.costo_premium}$
                    Capacidad de habitaciones VIP: {self.cantidad_vip} personas
                    Costo habitaciones VIP: {self.costo_vip}$
                    
                    """
    def Nombre(self):
        return self.nombre.lower()
    
    def Ruta(self):
        return self.ruta
    
    def Type_Room(self,habitacion):
        if habitacion == "simple":
            return self.n_habitacion["simple"]
        elif habitacion == "premium":
            return self.n_habitacion["premium"]
        elif habitacion == "vip":
            return self.n_habitacion["vip"]

    def Tours(self):
        if len(self.tours) == 0:
            puerto = Tour("Tour Puerto",30,10,"7 Am")
            self.tours.append(puerto)
            comida = Tour("Degustacion",100,100,"12 Pm")
            self.tours.append(comida)
            trote = Tour("Trote",0,1000,"6 Am")
            self.tours.append(trote)
            historia = Tour("Lugares Historicos",40,15,"10 Am")
            self.tours.append(historia)
            return self.tours
        else:
            return self.tours
    
    def Restaurante(self):
        if self.restaurante == False:
            self.restaurante = Restaurante()
            return self.restaurante
        else:
            return self.restaurante

    