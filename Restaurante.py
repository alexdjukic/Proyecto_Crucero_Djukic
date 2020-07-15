from Plato import Plato
from Alimento import Alimento
from Bebida import Bebida
from Combo import Combo
class Restaurante():
    def __init__(self,menu = []):
        self.menu = menu

    def Add_Platillo(self):
        platillo = False
        while platillo == False:
            aux = True
            while aux == True:
                nombre = input("introduzca el nombre del platillo: ").lower()
                aux = False
            aux = True
            while aux == True:
                try:
                    precio = int(input("Introduzca el precio del platillo: "))
                    if precio > 0:
                        precio += precio *0.16
                        aux = False
                    else:
                        print("Introduzca un precio valido")
                except ValueError:
                    print("Introduzca un precio valido")
            aux = True
            while aux == True:
                clasificacion = input("Es un alimento o una bebida?: ").lower()
                if clasificacion == "alimento":
                    aux1 = True
                    while aux1 == True:
                        try:
                            cantidad = int(input("Cuantos desea agregar?: "))
                            if cantidad > 0:
                                aux1 = False
                            else:
                                print("Introduzca una cantidad valida")
                        except ValueError:
                            print("introduzca una cantidad valida")
                    aux1 = True
                    while aux1 == True:
                        metodo = input(" El aliemento es de (1) Empaque o (2) Preparacion: ")
                        if metodo == "1":
                            metodo = "empaque"
                            item = False
                            for platillo in self.menu:
                                if platillo.Nombre() == nombre and platillo.Metodo() == metodo:
                                    item = True
                            if item == False:
                                platillo = Alimento(nombre,precio,cantidad,metodo)
                                self.menu.append(platillo)
                                aux = False
                                aux1 = False
                                platillo = True
                            else:
                                return "El platillo ya esta en el Menu"
                        elif metodo == "2":
                            metodo = "preparacion"
                            item = False
                            for platillo in self.menu:
                                if platillo.Nombre() == nombre and platillo.Metodo() == metodo:
                                    item = True
                            if item == False:
                                platillo = Alimento(nombre,precio,cantidad,metodo)
                                self.menu.append(platillo)
                                aux = False
                                aux1 = False
                                platillo = True
                            else:
                                return "El platillo ya esta en el Menu"
                        else:
                            print("Introduzca un metodo valido")
                elif clasificacion == "bebida":
                    aux1 = True
                    while aux1 == True:
                        try:
                            cantidad = int(input("Cuantos desea agregar?: "))
                            if cantidad > 0:
                                aux1 = False
                            else:
                                print("Introduzca una cantidad valida")
                        except ValueError:
                            print("introduzca una cantidad valida")
                    aux1 = True
                    while aux1 == True:
                        size = input("Indique el tamaño de la bebida: ").lower()
                        if size == "pequeño":
                            item = False
                            for platillo in self.menu:
                                if platillo.Nombre() == nombre and platillo.Size() == size:
                                    item = True
                            if item == False:
                                platillo = Bebida(nombre,precio,cantidad,size)
                                self.menu.append(platillo)
                                aux1 = False
                                aux = False
                                platillo = True
                            else:
                                return "La bebida ya esta en el Menu"
                        elif size == "mediano":
                            item = False
                            for platillo in self.menu:
                                if platillo.Nombre() == nombre and platillo.Size() == size:
                                    item = True
                            if item == False:
                                platillo = Bebida(nombre,precio,cantidad,size)
                                self.menu.append(platillo)
                                aux1 = False
                                aux = False
                                platillo = True
                            else:
                                return "la bebida ya esta en el Menu"
                        elif size == "grande":
                            item = False
                            for platillo in self.menu:
                                if platillo.Nombre() == nombre and platillo.Size() == size:
                                    item = True
                            if item == False:
                                platillo = Bebida(nombre,precio,cantidad,size)
                                self.menu.append(platillo)
                                aux1 = False
                                aux = False
                                platillo = True
                            else:
                                return "La bebida ya esta en el Menu"
                        else:
                            print("Introduzca un tamaño valido")
                else:
                    print("Introduzca una clasificacion valida")
        if platillo == True:
            return "El platillo ha sido agregado"
    
    def Add_Combo(self):
        aux = True
        while aux == True:
            nombre = input("Introduzca el nombre del combo: ").lower()
            aux = False
        aux = True
        while aux == True:
            try:
                precio = float(input("introduzca el precio del combo: "))
                if precio > 0:
                    aux = False
                else:
                    print("Introduzca un precio valido")
            except ValueError:
                print("Introduzca un precio valido")
        aux = True
        while aux == True:
            try:
                cantidad = int(input("Cuantos de estos combos desea agregar: "))
                if cantidad > 0:
                    aux = False
                else:
                    print("Introduzca una cantidad valida")
            except ValueError:
               print("Introduzca una cantidad valida")
        aux = True
        platillos = []
        i = 0
        while aux == True:
            if i == 2:
                combo = Combo(nombre,precio,cantidad,platillos)
                self.menu.append(combo)
                aux = False
            else:
                print(self.Check_Menu())
                aux1 =  True
                while aux1 == True:
                    item = input("Introduzca el nombre de un platillo que desee agregar al combo: ").lower()
                    if item in platillos:
                        print("El platillo ya esta agregado al combo")
                    else:
                        clasificacion = int(input("Presiona (1) si es un alimento o (2) si es una bebida: "))
                        if clasificacion == 1:
                            metodo = int(input("Presione (1) si es de empaque o (2) si es preparado"))
                            if metodo == 1:
                                metodo = "empaque"
                                for platillo in self.menu:
                                    if platillo.Nombre() == nombre and platillo.Metodo() == metodo:
                                        platillos.append(platillo)
                                        i += 1
                                        aux1 = False
                            elif metodo == 2:
                                metodo = "preparacion"
                                for platillo in self.menu:
                                    if platillo.Nombre() == nombre and platillo.Metodo() == metodo:
                                        platillos.append(platillo)
                                        i += 1
                                        aux1 = False
                            else:
                                print("Introduzca un metodo de preparaciuon valido")
                        
                        elif clasificacion == 2:
                            size = int(input("Presione (1) si es de tamaño pequeño, (2) si es mediano o (3) si es grande: "))
                            if size == 1:
                                size = "pequeño"
                                for platillo in self.menu:
                                    if platillo.Nombre() == nombre and platillo.Size() == size:
                                        platillos.append(platillo)
                                        i += 1
                                        aux1 = False
                            elif size == 2:
                                size = "mediano"
                                for platillo in self.menu:
                                    if platillo.Nombre() == nombre and platillo.Size() == size:
                                        platillos.append(platillo)
                                        i += 1
                                        aux1 = False
                            elif size == 3:
                                size = "grande"
                                for platillo in self.menu:
                                    if platillo.Nombre() == nombre and platillo.Size() == size:
                                        platillos.append(platillo)
                                        i += 1
                                        aux1 = False
                            else:
                                print("introduzca un metodo de preparacion valido")


    def Check_Menu(self):
        for i,platillo in enumerate(self.menu):
            print(f"{i} {platillo.Info()}")
    
    def Eliminar_Platillo(self):
        for platillo in self.menu:
            print(platillo.Info())
        platillo = False
        while platillo == False:
            aux = True
            while aux == True:
                nombre = input("Introduzca el nombre del platillo que desea eliminar del menu: ").lower()
                if nombre.isalpha:
                    aux = False
                else:
                    print("Introduzca un nombre valido")
            aux = True
            found = False
            while aux == True:
                seleccion = input("Es un alimento o una bebida?: ").lower()
                if seleccion == "alimento":
                    aux2 = True
                    while aux2 == True:
                        metodo = int(input("Presiona (1) si el alimento es de empque o (2) si es preparado: "))
                        if metodo == 1:
                            metodo = "empaque"
                            for alimento in self.menu:
                                if alimento.Nombre() == nombre and alimento.Metodo() == metodo:
                                    found = True
                                    self.menu.remove(alimento)
                            if found == False:
                                return "no existe ese platillo en el menu"
                            else:
                                return "El platillo ha sido eliminado del menu"
                        elif metodo == 2:
                            metodo = "preparacion"
                            for alimento in self.menu:
                                if alimento.Nombre() == nombre and  alimento.Metodo() == metodo:
                                    found = True
                                    self.menu.remove(alimento)
                            if found == False:
                                return "no existe ese platillo en el menu"
                            else:
                                return "El platillo ha sido eliminado del menu"
                        else:
                            print("Introduzca un metodo de preparacion valido")
                elif seleccion == "bebida":
                    aux2 = True
                    while aux2 == True:
                        size = input("Introduzca el tamaño de la bebida: ")
                        if size == "pequeño":
                            for bebida in self.menu:
                                if bebida.Nombre() == nombre and bebida.Size() == size:
                                    found = True
                                    self.menu.remove(bebida)
                            if found == False:
                                return "no existe ese platillo en el menu"
                            else:
                                return "El platillo ha sido eliminado del menu"
                        elif size == "mediano":
                            for bebida in self.menu:
                                if bebida.Nombre() == nombre and bebida.Size() == size:
                                    found = True
                                    self.menu.remove(bebida)
                            if found == False:
                                return "no existe ese platillo en el menu"
                            else:
                                return "El platillo ha sido eliminado del menu"
                        elif size == "grande":
                            for bebida in self.menu:
                                if bebida.Nombre() == nombre and bebida.Size() == size:
                                    found = True
                                    self.menu.remove(bebida)
                            if found == False:
                                return "no existe ese platillo en el menu"
                            else:
                                return "El platillo ha sido eliminado del menu"
                        else:
                            print("Introduzca un tamaño valido")
                else:
                    print("Ingrese si es alimento o bebida")
    

    




                        




                    

            
                    
