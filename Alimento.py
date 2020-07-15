from Plato import Plato
class Alimento(Plato):
    def __init__(self,nombre,precio,cantidad,metodo,clasificacion = "alimento"):
        self.metodo = metodo
        super().__init__(nombre,precio,cantidad,clasificacion)
    
    def Nombre(self):
        return self.nombre.lower()
    
    def Metodo(self):
        return self.metodo.lower()
        
    def Info(self):
        return """------ Informacion del Platillo ------
                    Nombre: {}
                    Precio + IVA: {}$
                    Cantidad: {}
                    Metodo de preparacion: {}
                    """.format(self.nombre,self.precio,self.cantidad,self.metodo)
        