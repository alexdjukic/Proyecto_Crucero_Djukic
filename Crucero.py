from Tour import Tour
from Restaurante import Restaurante
from Sencilla import Sencilla
from Premium import Premium
from Vip import Vip

class Crucero():
    def __init__(self,nombre,ruta,fecha,n_habitacion,capa_simple,costo_simple,capa_premium,costo_premium,capa_vip,costo_vip,sells,ticket = 0,simple = [],premium = [],vip = [],tours = [],restaurante = False):
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
        self.sells = sells
        self.ticket = ticket
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
    def Tickets(self):
        self.ticket = self.ticket + 1
    
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
        
    def Create_rooms(self):
        tupla = self.n_habitacion["simple"]
        self.simple = self.Room_Map(tupla)
        tupla = self.n_habitacion["premium"]
        self.premium = self.Room_Map(tupla)
        tupla = self.n_habitacion["vip"]
        self.vip = self.Room_Map(tupla)

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
                        columna.append(f"{letras[k]}.{i+1}")
                        k += 1
        return matrix
    
    def Room(self,room_type,rooms):

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
                seleccion = []
                aux2 = True
                while aux2 == True:
                    pasillo = input("seleccione la letra del pasillo de la habitacion: ").upper()
                    if pasillo.isalpha:
                        seleccion.append(pasillo)
                        aux2 = False
                    else:
                        print("introduzca una letra valida")
                aux2 = True
                while aux2 == True:
                    try:
                        numero = int(input("seleccione el numero de la habitacion: "))
                        if numero > 0 and numero < len(matrix)+1:
                            numero = str(numero)
                            seleccion.append(numero)
                            aux2 = False
                        else:
                            print("selecione un numero valido")
                    except ValueError:
                        print("seleccione un numero valido")
                seleccion = ".".join(seleccion)
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
                
        if f == False:
            return "La habitacion ya esta ocupada"
        
        else:
            rooms = []
            for habitacion in habitaciones:
                if room_type == "simple":
                    tipo = room_type
                    capacidad = self.capa_simple
                    costo = self.costo_simple
                    hab = habitacion.split(".")
                    pasillo = hab[0]
                    numero = hab[1]
                    simple = Sencilla(tipo,capacidad,costo,pasillo,numero,True)
                    rooms.append(simple)
                elif room_type == "premium":
                    tipo = room_type
                    capacidad = self.capa_premium
                    costo = self.costo_premium
                    hab = habitacion.split(".")
                    pasillo = hab[0]
                    numero = hab[1]
                    premium = Premium(tipo,capacidad,costo,pasillo,numero,True)
                    rooms.append(premium)
                elif room_type == "vip":
                    tipo = room_type
                    capacidad = self.capa_vip
                    costo = self.costo_vip
                    hab = habitacion.split(".")
                    pasillo = hab[0]
                    numero = hab[1]
                    vip = Vip(tipo,capacidad,costo,pasillo,numero,True)
                    rooms.append(vip)
            return rooms

    def Ocupar_Room(self,tipo,numero):
        if tipo == "simple":
            matrix = self.simple
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == numero:
                        matrix[i][j] = "X"
            self.simple = matrix
            
        elif tipo == "premium":
            matrix = self.premium
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == numero:
                        matrix[i][j] = "X"
            self.premium = matrix
            
        if tipo == "vip":
            matrix = self.vip
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == numero:
                        matrix[i][j] = "X"
            self.vip = matrix
            
        

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
        self.restaurante = Restaurante()
        return self.restaurante
    
    def Sells(self):
        return self.sells
    
    def Write(self):
        self.restaurante.Data(self.nombre)
    
    def Stats(self):
        return self.ticket

    