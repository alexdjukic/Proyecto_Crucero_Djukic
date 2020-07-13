class Tour():
    def __init__(self,tipo,precio,capacidad,hora):
        self.tipo = tipo 
        self.precio = precio
        self.capacidad = capacidad
        self.hora = hora
    
    def Nombre(self):
        return self.tipo

    def Cupos(self,clientes):
        if self.capacidad == 0:
            return "No hay cupos para este tour"
        else:
            self.capacidad -= clientes
            return "Se ha registrado a los {} viajeros al tour".format(clientes)
           