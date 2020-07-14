from Plato import Plato
class Bebida(Plato):
    def __init__(self,nombre,clasificacion,precio,cantidad,size):
        self.size = size
        super().__init__(nombre,clasificacion,precio,cantidad)
    
    def Nombre(self):
        return self.nombre
    
    def Size(self):
        return self.size

    def Info(self):
        return """------ Informacion del Platillo ------
                    Nombre: {}
                    Clasificacion: {}
                    Precio + IVA: {}$
                    Tamaño: {}
                    """.format(self.nombre,self.clasificacion,self.precio,self.size)