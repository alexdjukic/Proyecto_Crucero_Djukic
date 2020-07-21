class Plato():
    def __init__(self,nombre,precio,cantidad,ventas = 0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.ventas = ventas
    
    def Info(self):
        return f"""------Informacio del Platillo ------
                    Nombre: {self.nombre}
                    Precio: {self.precio}
                    Cantidad: {self.cantidad}
                    """
    def Nombre(self):
        return self.nombre
    
    def Buy(self,cantidad):
        self.ventas += cantidad
        producto = []
        self.cantidad -= cantidad
        precio = self.precio * cantidad
        iva = precio*0.16
        precio += iva
        producto.append(self.nombre)
        producto.append(precio)
        return producto
    
    def Modify(self,modifier,mod):
        if modifier == "nombre":
            self.nombre = mod
            return "Se ha cambiado el nombre del platillo o combo"
        elif modifier == "precio":
            self.precio = mod
            return "Se ha cambiado el precio del platillo o combo"
        elif modifier == "cantidad":
            self.cantidad = mod
            return "se ha cambiado la cantidad del platillo o combo"
    
    def Write_data(self,barco):
        with open('menu.txt','a') as m:
            m.write("comida" + ";")
            m.write(barco + ";")
            m.write(self.nombre + ";")
            m.write(str(self.precio) + ";")
            m.write(str(self.cantidad) + ";")
            m.write(str(self.ventas) + ";")
            m.write("\n")
        