from Tour import Tour
class Cliente():
    def __init__(self,nombre,identidad,edad,crucero,habitacion,monto,descuento):
        self.nombre = nombre
        self.identidad = identidad
        self.edad = edad
        self.habitacion = habitacion
        self.crucero = crucero
        self.monto = monto 
        self.descuento = descuento
    
    def Factura(self):
        iva = self.monto * 0.16
        total = self.monto + iva - self.descuento
        return """ ------ Factura del Cliente ------
                Nombre: {}
                Documento de Identidad : {}
                Edad: {}
                Habitacion: {}
                Monto a Pagar: {}$
                Descuento : {}$
                IVA: {}$
                Monto total a pagar: {}$
                """.format(self.nombre,self.identidad,self.edad,self.habitacion,self.monto,self.descuento,iva,total)

    def DNI(self):
        return self.identidad

    def Crucero(self):
        return self.crucero
    
    def Monto(self,tour,personas):
        precio = tour.Precio(personas)
        self.monto += precio
        print(precio, self.monto)
        
    
        
        



