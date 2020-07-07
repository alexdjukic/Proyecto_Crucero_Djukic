class Crucero():
    def __init__(self,nombre,ruta,fecha,capacidad,cantidad_sencilla,cantidad_premium,cantidad_vip):
        self.nombre = nombre
        self.ruta = ruta
        self.fecha = fecha
        self.capacidad = capacidad
        self.cantidad_sencilla = cantidad_sencilla
        self.cantidad_premium = cantidad_premium
        self.cantidad_vip = cantidad_vip

    def Info_Barco(self):
        return """   ------- Infromacion del Barco -------
        
                    Nombre : {}
                    Ruta: {}
                    Fecha de Salida: {}
                    Capacidad: {} Personas
                    Cantidad de habitaciones Sencillas: {}
                    Cantidad de habitaciones Premium: {}
                    Cantidad de habitaciones VIP: {}
                    
                    """.format(self.nombre,self.ruta,self.fecha,self.capacidad,self.cantidad_sencilla,self.cantidad_premium,self.cantidad_vip)