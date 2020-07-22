from Plato import Plato
class Restaurante():
    '''Clase encargadad de crear los objetos de tipo Restaurante
        Parametros:
        menu: list, lista de objetos de tipo Plato presentes en el restaurante
        '''
    def __init__(self,menu = []):
        self.menu = menu

    def API_Platillos(self,sells):
        '''Metodo encargado de agregar al menu los paltillos del api
        Recibe: sells: list, lista de ventas del crucero respectivo'''
        for i in range(len(sells)):
            # se recopilan los datos para crear los objetos de tipo plato
            nombre = sells[i]["name"].lower()
            precio = float(sells[i]["price"])
            cantidad = int(sells[i]["amount"])     
            platillo = Plato(nombre,precio,cantidad)
            self.menu.append(platillo)
      
    def Add_Platillo(self):
        '''Metodo encargado de agregar platillos al menu'''
        aux = True
        # se pregunta el nombre del platillo a agregar
        while aux == True:
            aux2 = True
            while aux2 == True:
                nombre = input("Introduzca el nombre del platillo: ").lower()
                aux2 = False
            aux2 = True
            # se pregunta el precio del platillo
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
            #se pregunta la cantidad a agregar
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
            # si el paltillo se encuentra en el menu no se agrega a este
            for platillo in self.menu:
                if platillo.Nombre() == nombre:
                    found = True
                    print("El platillo ya esta en el menu")
            # en caso contrario se crea el objeto y se agrega el menu
            if found == False:
                platillo = Plato(nombre,precio,cantidad)
                self.menu.append(platillo)
                return "El platillo ha sido agregado"
    
    def Add_Combo(self):
        '''Metodo encargado de agregar combos al menu'''
        aux = True
        while aux == True:
            aux2 = True
            #se pregunta el nombre del combo
            while aux2 == True:
                nombre = input("Introduzca el nombre del combo: ").lower()
                aux2 = False
            aux2 = True
            # se pregunta el precio del combo
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
            # se pregunta la cantidad de combos a agregar
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
            # se busca el combo en el menu
            for platillo in self.menu:
                # si se encuentra no se agrega el menu
                if platillo.Nombre() == nombre:
                    found = True
                    print("El combo ya esta en el menu")
            # en caso contrario se crea el objeto y se agrega al menu
            if found == False:
                platillo = Plato(nombre,precio,cantidad)
                self.menu.append(platillo)
                return "El combo ha sido agregado"

    def Buy(self):
        '''Metodo encargado de las compras de platillos del restaurante'''
        for i,platillo in enumerate(self.menu):
            # se recorre el menu y se imprime la informacion de cada platillo
            print(f"{i+1} {platillo.Info()}")
        # se pregunta que platillo desea comprar
        seleccion = int(input("Seleccione el platillo o combo a comprar: "))
        for i,platillo in enumerate(self.menu):
            # si el numero del platillo es igual a la seleccion
            if i+1 == seleccion:
                aux = True
                # se pregunta cuantos desea comprar
                while aux == True:
                    try:
                        cantidad = int(input("Cuantos de este platillo desea comprar: "))
                        if cantidad > 0:
                            aux = False
                    except ValueError:
                        print("Introduzca una cantidad valida")
                    # se llama al metodo de Plato Buy()
                    info = platillo.Buy(cantidad)
        # se retorna la informacion del platillo comprado 
        return f'''------ Factura del resturante ------
                    Nombre: {info[0]}
                    Precio: {info[1]}$
                    Cantidad comprada: {cantidad}
                    '''
                
    def Eliminar_Platillo(self):
        '''Metodo encargado de eliminar paltillos del menu'''
        # se recorre el menu
        for platillo in self.menu:
            print(platillo.Info())
        aux = True
        # se pregunta que platillo desea eliminar
        while aux == True:
            nombre = input("Introduzca el nombre del platillo a eliminar: ").lower()
            aux = False
        found = False
        for platillo in self.menu:
            # si se encuentra el platillo o combo en el menu se elimina el objeto
            if platillo.Nombre() == nombre:
                found = True
                self.menu.remove(platillo)
        if found == False:
            return "Se ha eliminado el platillo"
        else:
            return "El platillo no se encuentra en el menu"
    
    def Modificar(self):
        '''Metodo encargado de modificar platillos o combos en el menu'''
        #serecorre el menu
        for platillo in self.menu:
            print(platillo.Info())
        aux = True
        # se pregunta el nombre del paltillo a modificar
        while aux == True:
            nombre = input("Introduzca el nombre del platillo o combo que desea modificar: ").lower()
            aux = False
        found = False
        # se recorre el menu en busqueda del platillo
        for platillo in self.menu:
            if platillo.Nombre() == nombre:
                found = True
        # si es encontrado se pregunta que se desea modificar
        if found == True:
            aux = True
            while aux == True:
                print("Que desea modificar?")
                modifier = input("Presione (1) para modificar el nombre, (2) para modificar el precio o (3) para modificar la cantidad")
                # en caso del nombre
                if modifier == "1":
                    modifier = "nombre"
                    # se pregunta el nuevo nombre
                    mod = input("Introduzca el nuevo nombre del platillo o combo: ").lower()
                    for platillo in self.menu:
                        if platillo.Nombre() == nombre:
                            # se llama al metodo de Plato Modify()
                            print(platillo.Modify(modifier,mod))
                    return "Todo listo"
                    # en caso del precio
                elif modifier == "2":
                    modifier = "precio"
                    mod = float(input("Introduzca el nuevo precio del platillo o combo: "))
                    for platillo in self.menu:
                        if platillo.Nombre() == nombre:
                            print(platillo.Modify(modifier,mod))
                    return "Todo listo"
                    # en caso de la cantidad
                elif modifier == "3":
                    modifier = "cantidad"
                    mod = int(input("Introduzca el nueva cantidad del platillo o combo: "))
                    for platillo in self.menu:
                        if platillo.Nombre() == nombre:
                            print(platillo.Modify(modifier,mod))
                    return "Todo listo"
                else:
                    print("introduzca una opcion valida")
    
    def Txt_platillos(self,lista):
        '''Metodo encargado de crear los paltillos encontrados en el txt '''
        nombre = lista[0]
        precio = lista[1]
        cantidad = lista[2]
        ventas = lista[3]
        platillo = Plato(nombre,precio,cantidad,ventas)
        self.menu.append(platillo)

    def Data(self,barco):
        "Metodo encargado de llamar al metodo Write _Data() de Plato"
        for platillo in self.menu:
            platillo.Write_data(barco)





        
        
    

    




                        




                    

            
                    
