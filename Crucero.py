from Tour import Tour
from Restaurante import Restaurante
from Sencilla import Sencilla
from Premium import Premium
from Vip import Vip

class Crucero():
    ''' Clase encargada de crear todos los objetos de tipo Crucero
        Parametros
        ----------------------
        nombre: string , nombre del crucero
        ruta: list , ruta del crucero
        fecha : string , fecha de partida del crucero
        n_habtiacion: list, lista que contiene el diccionario con el numero de habitaciones por tipo
        capa_simple : int , capacidad de las habitaciones sencillas
        costo_simple : int , soto de las habitacione sencillas
        capa_premium : int , capacidad de las habitaciones premium
        costo_premium : int , soto de las habitacione premium
        capa_vip : int , capacidad de las habitaciones vip
        costo_vip : int , soto de las habitacione vip
        sells: dict : diccionario de ventas de comida del barco
        ticket: int, numero de tickets vendidos
        simple: list, matriz de habitacione simples
        premium: list, matrix de habitacion premium
        vip, list, matrix de habitaciones vip
        tours: list, lista de objetos Tour
        restaurante: obj, objeto de tipo restaurante
        '''
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
        '''Funcion encargada de retornar la informacion del crucero'''
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
        '''Funcion encargada de calcular cuantos tickets se han vendido en el crucero'''
        self.ticket = self.ticket + 1
    
    def Nombre(self):
        '''Funcion encargada de retornar el nombre del crucero'''
        return self.nombre.lower()
    
    def Ruta(self):
        '''Funcion encargada de retornar la ruta del crucero'''
        return self.ruta
    
    def Room_Info(self,tipo):
        '''Funcion encargada de retornar la capacidad y el costo de los distintos tipos de habitaciones''''
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
        '''Funcion encargada de crear las distitnas matrices de las habitaciones'''
        # se toma la tupla con el numero de pasillos y habitaciones por cada piso
        tupla = self.n_habitacion["simple"]
        # se llama al metodo Room_Map() para generar las matrices
        self.simple = self.Room_Map(tupla)
        tupla = self.n_habitacion["premium"]
        self.premium = self.Room_Map(tupla)
        tupla = self.n_habitacion["vip"]
        self.vip = self.Room_Map(tupla)

    def Room_Map(self,tupla):
        ''''Funcion encargada de generar las distintas matrices de los dsitintos tipos de habitacion
            Recibe: tupla: list, informacion de pasillos y habitacion es por piso
            Retorna la matriz de habitaciones'''
        matrix = []
        columna = []
        # numero de pasillos por tipo
        pasillos = (tupla[0]*2)+1
        # numero nde habitaciones por tipo
        habitaciones = tupla[1]
        pasillo = "■"
        # lista de letras para cada pasillo
        letras = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        k = 0
        # se genera la matriz
        for i in range(habitaciones):
            k = 0
            for j in range(pasillos):
                # si j es igual al numero de pasillos -1 se agrega una columna a la matriz
                if j == pasillos-1:
                    matrix.append(columna)
                    columna = []
                else:
                    # si j es multiplo de 2 se agrega un pasillo
                    if j % 2 == 0:
                        columna.append(pasillo)
                    # en caso contrario se agrega una habitacion
                    else:
                        columna.append(f"{letras[k]}.{i+1}")
                        k += 1
        return matrix
    
    def Room(self,room_type,rooms):
        '''Funcion encargada de la reservacion de las habitaciones
            Recibe:
            ---------------
            room_type: string , tipo de habitacion
            rooms: int cantidad de cuartos a reservar
            retorna una lsita con los objetos de tipo habitacion reservados '''
        # se imprime la matriz de las habitaciones dependiendo del tipo de habitacion
        if room_type== "simple":
            #se iguala matrix al atributo dependiendo del tipo de habitacion
            matrix = self.simple
            #se recorre la matriz
            for row in matrix:
                for cell in row:
                    # se imprime la fila
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
            # si k es igual al numero de cuartos
            if k >= rooms:
                aux = False
            else:
                f = False
                seleccion = []
                aux2 = True
                # se le pide al usuario el pasillo en el que desea su habitacion
                while aux2 == True:
                    pasillo = input("seleccione la letra del pasillo de la habitacion: ").upper()
                    if pasillo.isalpha:
                        seleccion.append(pasillo)
                        aux2 = False
                    else:
                        print("introduzca una letra valida")
                aux2 = True
                #se le ptrgunta al usuario el numero de habitacion a reservar
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
                # se juntan el pasillo y el numero para mantener la consistencia en la matriz
                seleccion = ".".join(seleccion)
                k += 1
                # se busca en la matrix el cuarto seleccionado
                for i in range(len(matrix)):
                    for j in range(len(matrix[i])):
                        # si se encuentra el cuarto
                        if matrix[i][j] == seleccion:
                            # se agrega a la lista habitaciones
                            habitaciones.append(seleccion)
                            #se cambia el numero en esta posicion por una x indicando que esta ocupada
                            matrix[i][j] = "X"
                            f = True
                # se imprime nuevamente la matrix modificada
                for row in matrix:
                    for cell in row:
                        print(cell, end=' ')
                    print()
        #si no se encuentra la habitacion      
        if f == False:
            return "La habitacion ya esta ocupada"
        # si se encuentra la habitacion se crea el obejto de tipo Habitacion
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
        '''Funcion encargada de ocupar los cuartos guardados en el txt
        Recibe:
        ----------------------------
        tipo: string, tipo de habitacion
        numero: string: pasilo y numero de la habitacion'''
        if tipo == "simple":
            matrix = self.simple
            # se busca la habitacion dentro de la amtriz respectiva y se cambia por una x
            for i in range(len(matrix)):
                for j in range(len(matrix[i])):
                    if matrix[i][j] == numero:
                        matrix[i][j] = "X"
            # se iguala el atributo respectivoa a la matriz modificada
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
        '''Funcion encargada de crear los obejtos de tipo Tour'''
        # si no existe ningun tour en el atributo tours
        if len(self.tours) == 0:
            # se crean los objetos con las especificaciones del instructivo del proyecto
            puerto = Tour("Tour Puerto",30,10,"7 Am")
            self.tours.append(puerto)
            comida = Tour("Degustacion",100,100,"12 Pm")
            self.tours.append(comida)
            trote = Tour("Trote",0,1000,"6 Am")
            self.tours.append(trote)
            historia = Tour("Lugares Historicos",40,15,"10 Am")
            self.tours.append(historia)
            return self.tours
        # en caso contrario retorna la lista tours
        else:
            return self.tours
    
    def Restaurante(self):
        '''Funcion encargada de crear el obejto de tipo restaurante de cada crucero'''
        self.restaurante = Restaurante()
        return self.restaurante
    
    def Sells(self):
        '''Funcion encargada de retornar las ventas del crucero'''
        return self.sells
    
    def Write(self):
        '''Funcion encargada de llamar a la funcion de restaurante'''
        self.restaurante.Data(self.nombre)
    
    def Stats(self):
        '''Funcion encargada de retornar la cantiadad de tickets vendidos'''
        return self.ticket

    