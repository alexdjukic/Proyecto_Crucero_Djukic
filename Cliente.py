from Tour import Tour
from Sencilla import Sencilla
from Premium import Premium
from Vip import Vip
class Cliente():
    '''Clase encargada de crear los objetos de tipo Cliente
        Parametros:
        ----------------------------------------------------
        nombre : string, nombre del cliente
        identidad: int, dni del cliente
        edad: int, edad del cliente
        crucero: string, nombre del crucero en el que viaja el cliente
        habitacion: obj, objeto de tipo habitacion del cliente
        monto: float, monto a pagar 
        descuento: float, descuento aplicado al cliente
        tour : bool, si el cliente compro o no un tour'''
    def __init__(self,nombre,identidad,edad,crucero,habitacion,monto,descuento,tour = False):
        self.nombre = nombre
        self.identidad = identidad
        self.edad = edad
        self.crucero = crucero
        self.habitacion = habitacion
        self.monto = monto 
        self.descuento = descuento
        self.tour = tour
    
    def Nombre(self):
        '''Funcion encargada de retornar el nombre del cliente'''
        return self.nombre

    def Factura(self):
        '''Funcion encargada de imprimir la factura del cliente'''
        # calculo del 16% de iva
        iva = self.monto * 0.16
        # calculo del total a pagar
        total = self.monto + iva - self.descuento
        # llamdo del metodo de Habitacion Type()
        habitacion = self.habitacion.Type()
        return """ ------ Factura del Cliente ------
                Nombre: {}
                Documento de Identidad : {}
                Edad: {}
                Habitacion: {}
                Monto a Pagar: {}$
                Descuento : {}$
                IVA: {}$
                Monto total a pagar: {}$
                """.format(self.nombre,self.identidad,self.edad,habitacion,self.monto,self.descuento,iva,total)

    def DNI(self):
        '''Funcion encargada de retornar el dni del cliente'''
        return self.identidad

    def Crucero(self):
        '''Funcion encargada de retornar el nombre del clucero en el que viaja el cliente'''
        return self.crucero
    
    def Habitacion(self):
        '''Metodo encargado de crear el objeto de tipo habitacion del cliente una vez es sacado del txt'''
        # se verifica el tipo de habitacion y se recorre la lsita para extraer la informacion necesaria
        if self.habitacion[0] == "simple":
            tipo = self.habitacion[0]
            capacidad = self.habitacion[1]
            costo = self.habitacion[2]
            pasillo = self.habitacion[3]
            numero = self.habitacion[4]
            #se crea el obejto de tipo sencilla
            simple = Sencilla(tipo,capacidad,costo,pasillo,numero,True)
            self.habitacion = simple
        elif self.habitacion[0] == "premium":
            tipo = self.habitacion[0]
            capacidad = self.habitacion[1]
            costo = self.habitacion[2]
            pasillo = self.habitacion[3]
            numero = self.habitacion[4]
            # se crea el objeto de tipo premium
            premium = Premium(tipo,capacidad,costo,pasillo,numero,True)
            self.habitacion = premium
        elif self.habitacion[0] == "vip":
            tipo = self.habitacion[0]
            capacidad = self.habitacion[1]
            costo = self.habitacion[2]
            pasillo = self.habitacion[3]
            numero = self.habitacion[4]
            # se crea el objeto de tipo vip
            vip = Vip(tipo,capacidad,costo,pasillo,numero,True)
            self.habitacion = vip

    def Ocupar(self):
        '''Metodo encargado de ocupar la habitacion del cliente'''
        info = []
        # se llama al metodo Request_room() para obtener los datos del cuarto
        habitacion = self.habitacion.Request_room()
        crucero = self.crucero
        info.append(crucero)
        tipo = habitacion[0]
        info.append(tipo)
        numero = habitacion[1]
        info.append(numero)
        return info

    def Stats(self):
        '''Metodo encargado de recopilar la informacion necesaria para el modulo de estadisticas
            Retorna una lista de estadisticas'''
        stats = []
        iva = self.monto * 0.16
        total = self.monto + iva - self.descuento
        stats.append(total)
        stats.append(self.nombre)
        stats.append(self.tour)
        stats.append(self.crucero)
        return stats
    
    def Info(self):
        '''Metodo encargado de imprimir la informacion del cliente para le metodo de estadisticas'''
        iva = self.monto * 0.16
        total = self.monto + iva - self.descuento
        habitacion = self.habitacion.Type()
        return """ ------ Informacion del Cliente ------
                Nombre: {}
                Documento de Identidad : {}
                Edad: {}
                Habitacion: {}
                Monto a Pagar: {}$
                Descuento : {}$
                IVA: {}$
                Monto total a pagar: {}$
                """.format(self.nombre,self.identidad,self.edad,habitacion,self.monto,self.descuento,iva,total)


    
    def Write_data(self):
        '''Metodo encargado de escribir la informacion del cliente en el archivo txt'''
        with open('cliente.txt','a') as c:
            c.write("cliente" + ";")
            c.write(self.nombre + ";")
            c.write(str(self.identidad) + ";")
            c.write(str(self.edad)+ ";")
            c.write(self.crucero + ";" )
            habitacion = self.habitacion
            hab = habitacion.Datos()
            c.write(hab[0] + ";")
            c.write(hab[1] + ";")
            c.write(hab[2] + ";")
            c.write(hab[3] + ";")
            c.write(hab[4] + ";")
            c.write(str(self.monto) + ";")
            c.write(str(self.descuento) + ";")
            c.write(str(self.tour))
            c.write("\n")
        

        
    
        
        



