from Plato import Plato
class Bebida(Plato):
    def __init__(self,nombre,clasificacion,precio,size):
        self.size = size
        super().__init__(nombre,clasificacion,precio)

    def Info(self):
        return """------ Informacion del Platillo ------
                    Nombre: {}
                    Clasificacion: {}
                    Precio: {}
                    Tamaño: {}
                    """.format(self.nombre,self.clasificacion,self.precio,self.size)