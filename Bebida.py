from Plato import Plato
class Bebida(Plato):
    def __init__(self,nombre,precio,cantidad,size,clasificacion = "bebida"):
        self.size = size
        super().__init__(nombre,precio,cantidad,clasificacion)
    
    def Nombre(self):
        return self.nombre.lower()
    
    def Size(self):
        return self.size.lower()

    def Info(self):
        return """------ Informacion del Platillo ------
                    Nombre: {}
                    Precio + IVA: {}$
                    Cantidad: {}
                    Tamaño: {}
                    """.format(self.nombre,self.precio,self.cantidad,self.size)