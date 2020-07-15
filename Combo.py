from Plato import Plato
class Combo(Plato):
    def __init__(self,nombre,precio,cantidad,platillos = [],clasificacion = "combo"):
        self.platillos = platillos
        super().__init__(nombre,precio,cantidad,clasificacion)
    
    def Nombre(self):
        return self.nombre
    
    def Info(self):
        return f""" ------ Informacion del Combo ------
                    Nombre: {self.nombre} 
                    Precio: {self.precio}
                    Cantidad: {self.cantidad}
                    Platillos: {self.platillos} """
    