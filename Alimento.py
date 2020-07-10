from Plato import Plato
class Alimento(Plato):
    def __init__(self,nombre,clasificacion,precio,metodo):
        self.metodo = metodo
        super().__init__(nombre,clasificacion,precio)
        
    def Info(self):
        return """------ Informacion del Platillo ------
                    Nombre: {}
                    Clasificacion: {}
                    Precio: {}
                    Metodo de preparacion: {}
                    """.format(self.nombre,self.clasificacion,self.precio,self.metodo)
        