class Plato():
    '''Clase encargada de crear los obejtos de tipo Plato
        Parametros:
        --------------------------------------
        nombre: string, nombre del paltillo o combo
        precio: float, precio del platillo o combo
        cantidad: int, cantidad del platillo o combo
        ventas: int, cantidad de platillos o combos vendidos'''
    def __init__(self,nombre,precio,cantidad,ventas = 0):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.ventas = ventas
    
    def Info(self):
        '''Metodo encargado de retornar la informacion del platillo'''
        return f"""------Informacio del Platillo ------
                    Nombre: {self.nombre}
                    Precio: {self.precio}
                    Cantidad: {self.cantidad}
                    """
    def Nombre(self):
        '''Metodo encargado de retornar el nombre del platillo'''
        return self.nombre
    
    def Buy(self,cantidad):
        '''Metodo encargado de las ventas del producto
        Recibe: cantidad: cantidad del producto comprada'''
        # se suma la cantidad al atributo ventas
        self.ventas += cantidad
        producto = []
        # se resta la cantidad al atributo cantidad
        self.cantidad -= cantidad
        # se calcula el precio
        precio = self.precio * cantidad
        # se calcula el iva
        iva = precio*0.16
        # se calcula el total
        precio += iva
        # se retorna el nombre y el precio del producto
        producto.append(self.nombre)
        producto.append(precio)
        return producto
    
    def Modify(self,modifier,mod):
        '''Metodo encargado de la modificacion del producto
        Recibe: 
        ----------------------------
        modifier: categoria a modificar
        mod: nuevo cambio que s eaplicara al producto'''
        # en caso de modificar el nombre
        if modifier == "nombre":
            # se cambia el atributo nombre por mod
            self.nombre = mod
            return "Se ha cambiado el nombre del platillo o combo"
        # en caso de modificar el precio
        elif modifier == "precio":
            self.precio = mod
            return "Se ha cambiado el precio del platillo o combo"
        # en caso de modificar la cantidad
        elif modifier == "cantidad":
            self.cantidad = mod
            return "se ha cambiado la cantidad del platillo o combo"
    
    def Write_Data(self,barco):
        '''Metodo encargado de escribir los datos del producto en el txt'''
        with open('menu.txt','a') as m:
            m.write("comida" + ";")
            m.write(barco + ";")
            m.write(self.nombre + ";")
            m.write(str(self.precio) + ";")
            m.write(str(self.cantidad) + ";")
            m.write(str(self.ventas) + ";")
            m.write("\n")
        