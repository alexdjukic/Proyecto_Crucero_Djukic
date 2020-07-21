from Tour import Tour
from Sencilla import Sencilla
from Premium import Premium
from Vip import Vip
class Cliente():
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
        return self.nombre

    def Factura(self):
        iva = self.monto * 0.16
        total = self.monto + iva - self.descuento
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
        return self.identidad

    def Crucero(self):
        return self.crucero
    
    def Habitacion(self):
        if self.habitacion[0] == "simple":
            tipo = self.habitacion[0]
            capacidad = self.habitacion[1]
            costo = self.habitacion[2]
            pasillo = self.habitacion[3]
            numero = self.habitacion[4]
            simple = Sencilla(tipo,capacidad,costo,pasillo,numero,True)
            self.habitacion = simple
        elif self.habitacion[0] == "premium":
            tipo = self.habitacion[0]
            capacidad = self.habitacion[1]
            costo = self.habitacion[2]
            pasillo = self.habitacion[3]
            numero = self.habitacion[4]
            premium = Premium(tipo,capacidad,costo,pasillo,numero,True)
            self.habitacion = premium
        elif self.habitacion[0] == "vip":
            tipo = self.habitacion[0]
            capacidad = self.habitacion[1]
            costo = self.habitacion[2]
            pasillo = self.habitacion[3]
            numero = self.habitacion[4]
            vip = Vip(tipo,capacidad,costo,pasillo,numero,True)
            self.habitacion = vip

    def Ocupar(self):
        info = []
        habitacion = self.habitacion.Request_room()
        crucero = self.crucero
        info.append(crucero)
        tipo = habitacion[0]
        info.append(tipo)
        numero = habitacion[1]
        info.append(numero)
        return info

    def Stats(self):
        stats = []
        iva = self.monto * 0.16
        total = self.monto + iva - self.descuento
        stats.append(total)
        stats.append(self.nombre)
        stats.append(self.tour)
        stats.append(self.crucero)
        return stats
    
    def Info(self):
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
        

        
    
        
        



