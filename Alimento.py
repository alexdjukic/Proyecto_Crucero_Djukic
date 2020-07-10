from Plato import Plato
class Alimento(Plato):
    def __init__(self,nombre,clasificacion,precio,empaque):
        self.empaque = empaque
        super().__init__(nombre,clasificacion,precio)
        
        