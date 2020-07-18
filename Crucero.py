from Tour import Tour
from Restaurante import Restaurante
class Crucero():
    def __init__(self,nombre,ruta,fecha,n_habitacion,capa_simple,costo_simple,capa_premium,costo_premium,capa_vip,costo_vip,simple = [],premium = [],vip = [],tours = [],restaurante = False):
        self.nombre = nombre
        self.ruta = ruta
        self.fecha = fecha
        self.n_habitacion = n_habitacion
        self.capa_simple = capa_simple
        self.costo_simple = costo_simple
        self.capa_premium = capa_premium
        self.costo_premium = costo_premium
        self.capa_vip = capa_vip
        self.costo_vip = costo_vip
        self.simple = simple
        self.premium = premium
        self.vip = vip
        self.tours = tours
        self.restaurante = restaurante

    
    
    def Info_Barco(self):
        return f"""   ------- Infromacion del Barco -------
        
                    Nombre : {self.nombre}
                    Ruta: {self.ruta}
                    Fecha de Salida: {self.fecha}
                    Capacidad de habitaciones Sencillas: {self.capa_simple} personas
                    Costo habitaciones Sencillas: {self.costo_simple}$
                    Capacidad de habitaciones Premium: {self.capa_premium} personas
                    Costo habitaciones Premium: {self.costo_premium}$
                    Capacidad de habitaciones VIP: {self.capa_vip} personas
                    Costo habitaciones VIP: {self.costo_vip}$
                    
                    """
    def Nombre(self):
        return self.nombre.lower()
    
    def Ruta(self):
        return self.ruta
    def Room_Info(self,tipo):
        room_info = []
        if tipo == "simple":
            room_info.append(self.capa_simple)
            room_info.append(self.costo_simple)
            return room_info
        elif tipo == "premium":
            room_info.append(self.capa_premium)
            room_info.append(self.costo_premium)
            return room_info
        elif tipo == "vip":
            room_info.append(self.capa_vip)
            room_info.append(self.costo_vip)
            return room_info
        
        

    def Room_Map(self,tupla):
        matrix = []
        columna = []
        pasillos = (tupla[0]*2)+1
        habitaciones = tupla[1]
        pasillo = "■"
        letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        k = 0
        for i in range(habitaciones):
            k = 0
            for j in range(pasillos):
                if j == pasillos-1:
                    matrix.append(columna)
                    columna = []
                else:
                    if j % 2 == 0:
                        columna.append(pasillo)
                    else:
                        columna.append(f"{letras[k]}{i+1}")
                        k += 1
        return matrix
    
    def Room(self,room_type,rooms):
        tupla = self.n_habitacion["simple"]
        self.simple = self.Room_Map(tupla)
        tupla = self.n_habitacion["premium"]
        self.premium = self.Room_Map(tupla)
        tupla = self.n_habitacion["vip"]
        self.vip = self.Room_Map(tupla)

        if room_type== "simple":
            matrix = self.simple
            for row in matrix:
                for cell in row:
                    print(cell, end=' ')
                print()
        elif room_type == "premium":
            matrix = self.premium
            for row in matrix:
                for cell in row:
                    print(cell, end=' ')
                print()
        elif room_type == "vip":
            matrix = self.vip
            for row in matrix:
                for cell in row:
                    print(cell, end=' ')
                print()
        k = 0
        habitaciones = []
        aux = True
        while aux == True:
            if k >= rooms:
                aux = False
            else:
                f = False
                seleccion = input("Introduzca la letra en mayuscula y el numero de habitacion que desea comprar: ")
                k += 1
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        if matrix[i][j] == seleccion:
                            habitaciones.append(seleccion)
                            matrix[i][j] = "X"
                            f = True
                for row in matrix:
                    for cell in row:
                        print(cell, end=' ')
                    print()
                
                print(k,rooms)
                
        if f == False:
            return "La habitacion ya esta ocupada"
        
        else:
            return habitaciones
            

                


        
        


    def Tours(self):
        if len(self.tours) == 0:
            puerto = Tour("Tour Puerto",30,10,"7 Am")
            self.tours.append(puerto)
            comida = Tour("Degustacion",100,100,"12 Pm")
            self.tours.append(comida)
            trote = Tour("Trote",0,1000,"6 Am")
            self.tours.append(trote)
            historia = Tour("Lugares Historicos",40,15,"10 Am")
            self.tours.append(historia)
            return self.tours
        else:
            return self.tours
    
    def Restaurante(self):
        if self.restaurante == False:
            self.restaurante = Restaurante()
            return self.restaurante
        else:
            return self.restaurante

    