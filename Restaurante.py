from Plato import Plato
from Alimento import Alimento
from Bebida import Bebida
class Restaurante():
    def __init__(self,menu = []):
        self.menu = menu

    def Add_Platillo(self):
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
                    metodo = input(" El aliemento es de (1) Empaque o (2) Preparacion: ")
                    if metodo == "1":
                        platillo = Alimento(nombre,clasificacion,precio,metodo)
                        self.menu.append(platillo)
                        aux = False
                        aux1 = False
                    elif metodo == "2":
                        platillo = Alimento(nombre,clasificacion,precio,metodo)
                        self.menu.append(platillo)
                        aux = False
                        aux1 = False
                    else:
                        print("Introduzca un metodo valido")
            elif clasificacion == "bebida":
                aux1 = True
                while aux1 == True:
                    size = input("Indique el tamaño de la bebida: ").lower()
                    if size == "pequeño":
                        platillo = Bebida(nombre,clasificacion,precio,size)
                        self.menu.append(platillo)
                        aux1 = False
                        aux = False
                    elif size == "mediano":
                        platillo = Bebida(nombre,clasificacion,precio,size)
                        self.menu.append(platillo)
                        aux1 = False
                        aux = False
                    elif size == "grande":
                        platillo = Bebida(nombre,clasificacion,precio,size)
                        self.menu.append(platillo)
                        aux1 = False
                        aux = False
                    else:
                        print("Introduzca un tamaño valido")
            else:
                print("Introduzca una clasificacion valida")
        
        return "El platillo ha sido agregado"

    def Check_Menu(self):
        for platillo in self.menu:
            return platillo.Info()



                    

            
                    
