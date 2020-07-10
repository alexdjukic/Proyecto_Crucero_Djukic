from Plato import Plato
class Bebida(Plato):
    def __init__(self,nombre,clasificacion,precio,size):
        self.precio = precio
        super().__init__(nombre,clasificacion,precio)