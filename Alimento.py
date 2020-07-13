from Plato import Plato
class Alimento(Plato):
    def __init__(self,nombre,clasificacion,precio,metodo):
        self.metodo = metodo
        super().__init__(nombre,clasificacion,precio)
    
    def Nombre(self):
        return self.nombre
    
    def Metodo(self):
        return self.metodo
        
    def Info(self):
        return """------ Informacion del Platillo ------
                    Nombre: {}
                    Clasificacion: {}
                    Precio + IVA: {}$
                    Metodo de preparacion: {}
                    """.format(self.nombre,self.clasificacion,self.precio,self.metodo)
        