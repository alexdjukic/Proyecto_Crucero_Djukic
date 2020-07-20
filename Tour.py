class Tour():
    def __init__(self,tipo,precio,capacidad,hora):
        self.tipo = tipo 
        self.precio = precio
        self.capacidad = capacidad
        self.hora = hora
    
    def Nombre(self):
        return self.tipo
    
    def Precio(self,personas):
        return self.precio * personas


    def Cupos(self,clientes):
        if self.capacidad == 0:
            return "No hay cupos para este tour"
        else:
            self.capacidad -= clientes
            return str(self.precio * clientes)
           