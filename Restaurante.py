from Plato import Plato
class Restaurante():
    def __init__(self,menu = []):
        self.menu = menu

    def API_Platillos(self,sells):
        for i in range(len(sells)):
            nombre = sells[i]["name"].lower()
            precio = float(sells[i]["price"])
            cantidad = int(sells[i]["amount"])     
            platillo = Plato(nombre,precio,cantidad)
            self.menu.append(platillo)
      
    def Add_Platillo(self):
        aux = True
        while aux == True:
            aux2 = True
            while aux2 == True:
                nombre = input("Introduzca el nombre del platillo: ").lower()
                aux2 = False
            aux2 = True
            while aux2 == True:
                try:
                    precio = float(input("Introduzca el precio del platillo: "))
                    if precio > 0:
                        aux2 = False
                    else:
                        print("Introduzca un precio valido")
                except ValueError:
                    print("Introduzca un precio valido")
            aux2 = True
            while aux2 == True:
                try:
                    cantidad = int(input("Introduzca la cantidad del platillo que desea agregar: "))
                    if cantidad > 0:
                        aux2 = False
                    else:
                        print("Introduzca una cantidad valida")
                except ValueError:
                    print("Introduzca una cantidad valida")
            found = False
            for platillo in self.menu:
                if platillo.Nombre() == nombre:
                    found = True
                    print("El platillo ya esta en el menu")
            if found == False:
                platillo = Plato(nombre,precio,cantidad)
                self.menu.append(platillo)
                return "El platillo ha sido agregado"
    
    def Add_Combo(self):
        aux = True
        while aux == True:
            aux2 = True
            while aux2 == True:
                nombre = input("Introduzca el nombre del combo: ").lower()
                aux2 = False
            aux2 = True
            while aux2 == True:
                try:
                    precio = float(input("Introduzca el precio del combo: "))
                    if precio > 0:
                        aux2 = False
                    else:
                        print("Introduzca un precio valido")
                except ValueError:
                    print("Introduzca un precio valido")
            aux2 = True
            while aux2 == True:
                try:
                    cantidad = int(input("Introduzca la cantidad del combo que desea agregar: "))
                    if cantidad > 0:
                        aux2 = False
                    else:
                        print("Introduzca una cantidad valida")
                except ValueError:
                    print("Introduzca una cantidad valida")
            found = False
            for platillo in self.menu:
                if platillo.Nombre() == nombre:
                    found = True
                    print("El combo ya esta en el menu")
            if found == False:
                platillo = Plato(nombre,precio,cantidad)
                self.menu.append(platillo)
                return "El combo ha sido agregado"

    def Buy(self):
        for i,platillo in enumerate(self.menu):
            print(f"{i+1} {platillo.Info()}")
        
        seleccion = int(input("Seleccione el platillo o combo a comprar: "))
        for i,platillo in enumerate(self.menu):
            if i+1 == seleccion:
                aux = True
                while aux == True:
                    try:
                        cantidad = int(input("Cuantos de este platillo desea comprar: "))
                        if cantidad > 0:
                            aux = False
                    except ValueError:
                        print("Introduzca una cantidad valida")
                    info = platillo.Buy(cantidad)
        return f'''------ Factura del resturante ------
                    Nombre: {info[0]}
                    Precio: {info[1]}$
                    Cantidad comprada: {cantidad}
                    '''
                
        

    
    def Eliminar_Platillo(self):
        for platillo in self.menu:
            print(platillo.Info())
        aux = True
        while aux == True:
            nombre = input("Introduzca el nombre del platillo a eliminar: ").lower()
            aux = False
        found = False
        for platillo in self.menu:
            if platillo.Nombre() == nombre:
                found = True
                self.menu.remove(platillo)
        if found == False:
            return "Se ha eliminado el platillo"
        else:
            return "El platillo no se encuentra en el menu"
    
    
    
    def Modificar(self):
        for platillo in self.menu:
            print(platillo.Info())
        aux = True
        while aux == True:
            nombre = input("Introduzca el nombre del platillo o combo que desea modificar: ").lower()
            aux = False
        found = False
        for platillo in self.menu:
            if platillo.Nombre() == nombre:
                found = True
        if found == True:
            aux = True
            while aux == True:
                print("Que desea modificar?")
                modifier = input("Presione (1) para modificar el nombre, (2) para modificar el precio o (3) para modificar la cantidad")
                if modifier == "1":
                    modifier = "nombre"
                    mod = input("Introduzca el nuevo nombre del platillo o combo: ").lower()
                    for platillo in self.menu:
                        if platillo.Nombre() == nombre:
                            print(platillo.Modify(modifier,mod))
                    return "Todo listo"
                elif modifier == "2":
                    modifier = "precio"
                    mod = float(input("Introduzca el nuevo precio del platillo o combo: "))
                    for platillo in self.menu:
                        if platillo.Nombre() == nombre:
                            print(platillo.Modify(modifier,mod))
                    return "Todo listo"
                elif modifier == "3":
                    modifier = "cantidad"
                    mod = int(input("Introduzca el nueva cantidad del platillo o combo: "))
                    for platillo in self.menu:
                        if platillo.Nombre() == nombre:
                            print(platillo.Modify(modifier,mod))
                    return "Todo listo"
                else:
                    print("introduzca una opcion valida")
                        





        
        
    

    




                        




                    

            
                    
