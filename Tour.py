class Tour():
    '''Clase encargada de crear los obejtos de tipo Tour
    Parametros:
    ---------------------------------------
    tipo: string, tipo de tour
    precio: float, precio del tour
    capacidad: int, capacidad del tour
    hora: string, hora del tour'''
    def __init__(self,tipo,precio,capacidad,hora):
        self.tipo = tipo 
        self.precio = precio
        self.capacidad = capacidad
        self.hora = hora
    
    def Nombre(self):
        '''Funcion encargada de retornar el nombre del tour'''
        return self.tipo
    
    def Precio(self,personas):
        '''Metodo encargado de calcular y retornar el precio del tour
        Recibe: personas: int, cantidad de personas que van al tour'''
        return self.precio * personas


    def Cupos(self,clientes):
        '''Metodo encargado de calcular los cupos del tour
        Recibe: clientes: int, cantidad de personas que van al tour'''
        if self.capacidad == 0:
            return "No hay cupos para este tour"
        else:
            self.capacidad -= clientes
            return str(self.precio * clientes)
           