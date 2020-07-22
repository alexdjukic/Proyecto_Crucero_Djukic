from Crucero import Crucero
from Habitacion import Habitacion 
from Sencilla import Sencilla 
from Premium import Premium
from Vip import Vip
from Cliente import Cliente 
from Tour import Tour
from Restaurante import Restaurante
import requests
import math

def is_prime(doc_identidad,i = 2):
    '''Funcion encargada de calcular si el dni de un cliente es primo
        Recibe el dni del cliente
        Retorna un booleano identificando si el dni es primo o no'''
    aux = True
    # uso de un ciclo while para determinar si el numero es primo
    while aux == True:
        #si i es igual al dni el dni es primo 
        if i == doc_identidad:
            return True
        # si i es divisor del dni el numero no es primo
        elif doc_identidad % i == 0:
            return False
        else:
            i += 1

def is_abundant(doc_identidad, i = 2):
    '''Funcion encargada de verificar si el dni de un cliente es un numero abundante
        Recibe el dni del cliente y una variable i que comienza en 2
        Retorna un booleano verificando si el dni es abundante o no'''
    aux = True
    # lista donde se guardan todos los divisores del dni
    divisores = []
    # uso de un ciclo para recolectar todos los divisores
    while aux == True:
        # si i es igual al dni se para el ciclo
        if i == doc_identidad:
            aux = False
        # si i es divisor de dni se agrega a la lista de divisores y se suma 1 a i
        elif doc_identidad % i == 0:
            divisores.append(i)
            i += 1
        else:
            i += 1
    suma = 0
    # se suman todos los divisores dentro de la lista a la variable suma
    for i in range(len(divisores)):
        suma += divisores[i]
    #si suma es mayor que dni el numero es abundante
    if suma > doc_identidad:
        return True
    else:
        return False

def descuentos(monto,doc_identidad,edad):
    '''Funcion encargada de calcular el descuento del cliente si es que aplica
        Recibe
        -------
        monto : float , monto al cual se le a a aplicar el descuento
        doc_identidad : int, dni del cliente que aplica para un descuento
        edad : int, edad del cliente que aplica para el descuento
        
        Retorna la variable descuento que contiene el monto que se le restara al monto total'''
    #se llama a la funcion is_prime() para verificar si el dni es primo
    if is_prime(doc_identidad) == True:
        # si aplica se retorna un descuento de  10%
        descuento = monto * 0.1
        return descuento
    # se llama a la funcion is_abundant() para verificar si el dni es abundante
    elif is_abundant(doc_identidad) == True:
        #si aplica se retorna un descuento de 15%
        descuento = monto * 0.15
        return descuento
    #si la edad del cliente es mayor de 65 años
    elif edad >= 65:
        aux = True
        # se le pregunta mediatne un ciclo while para evitar malas respuestas
        while aux == True:
            #se le pregunta si tiene alguna discapacidad
            discapacidad = input("Posee alguna discapacidad: ").lower()
            # si rsponde si se le retorna un descuento de 30%
            if discapacidad == "si":
                descuento = monto * 0.3
                return descuento
            # si responde que no, no se le retorna descuento
            elif discapacidad == "no":
                descuento = 0
                return descuento
            # para evitar errores se le imprime que introduzca una opcion correcta
            else:
                print("Introduzca si o no")
    # si el cliente no aplica para ningun descuento se retorna el valor de 0
    else:
        descuento = 0 
        return descuento

def cruceros_disponibles(cruceros):
    '''Funcion encargada de crear los objetos de tipo Crucero proporcionados por el api
        Recibe
        -----------------
        cruceros : list , lista que contiene los diccionarios proporcionados por el api
        
        Retorna una lista con todos los objetos de tipo crucero ya creados'''
    cruceros_disponibes = []
    # se recorre la lista cruceros para obtener la informacion necesaria para crear los objetos de tipo Crucero
    for crucero in cruceros:
        # se toman los datos necesarios del diccionario apra crear cada uno de los atributos del objeto
        nombre = crucero["name"]
        ruta = crucero["route"]
        fecha = crucero["departure"]
        n_habitaciones = crucero["rooms"]
        cantidad_sencilla = int(crucero["capacity"]["simple"])
        costo_simple = float(crucero["cost"]["simple"])
        cantidad_premium = int(crucero["capacity"]["premium"])
        costo_premium = float(crucero["cost"]["premium"])
        cantidad_vip = int(crucero["capacity"]["vip"])
        costo_vip = float(crucero["cost"]["vip"])
        sells = crucero["sells"]
        # se crea el objeto de tipo Crucero con todos los atributos una vez colocados en su respectivas variables
        barco = Crucero(nombre,ruta,fecha,n_habitaciones,cantidad_sencilla,costo_simple,cantidad_premium,costo_premium,cantidad_vip,costo_vip,sells)
        # se llama a la funcion del Crucero Create_rooms() para crear las matrices de los distintos tipos de habitaciones
        barco.Create_rooms()
        # se llama a la funcion de la clase Crucero para crear el resturante del crucero
        barco.Restaurante()
        # se aggrega el objeto a la lista de cruceros disponibles
        cruceros_disponibes.append(barco)
    return cruceros_disponibes

def complete_form():
    ''' Funcion encargada de imprimir el formulario del cliente que va a pagar 
        No recibe ningun parametro
        Retorna los datos del cliente dentro de una lista'''
    aux = True
    client = []
    name = []
    print("A continuacion se imprime el formulario de la persona que va a pagar")
    # se utiliza un ciclo while para evitar errores 
    while aux == True:
        # se le pide al cliente que introduzca su nombre
        nombre = input("Introduzca su nombre: ").lower()
        # si el nombre no contiene numeros, simbolos o espacios
        if nombre.isalpha:
            # se agrega a la lista name 
            name.append(nombre)
            aux = False
        else:
            print("Introduzca un nombre valido")
    aux = True
    while aux == True:
        # se le pregunta al cliente su apellido
        apellido = input("Introduzca su apellido: ").lower()
        # si el apellido no contiene espacios, numeros o simbolos
        if apellido.isalpha:
            # se abrega el apellido a lista name
            name.append(apellido)
            aux = False
        else:
            print("Introduzca un apellido valido")
    # se juntan el nombre y apellido del clieente en una sola variable
    name = " ".join(name)
    # se agrega la variable name a la lista client
    client.append(name)
    aux = True
    # se utiliza unciclo while para evitar errores
    while aux == True:
        # se utiliza el try/ except para verificar si la edad de la persona es un numero
        try:
            edad = int(input("Introduzca su edad: "))
            # si la persona a pagar es mayor a 18 años
            if edad > 18:
                # se agrega la edad del cliente a la lsita client
                client.append(edad)
                aux = False
            else:
                print("Introduzca una edad valida")
        #si el input del cliente no es un numero imprime un mensaje de error
        except ValueError:
            print("Introduzca una edad valida")
    aux = True
    # se utiliza un ciclo while para evitar errores
    while aux == True:
        # se utiliza un try/except para verificar si el dni es un numero
        try:
            dni = int(input("Introduzca su DNI: "))
            # si el dni es un numero de 8 digitos
            if dni > 10000000:
                # se agrega el dni a la lista client
                client.append(dni)
                aux = False
        # si el input del cliente no es un numero imprime un mensaje de error
        except ValueError:
            print("Introduzca un DNI valido")
    # se retorna la lista client   
    return client

def rest_form(travelers):
    '''Funcion encargada de imprimir el formulario restringido a los acompañantes del cliente anterior
        
        Recibe: travelers : int, numero de viajeros que acompañan al cliente que va a pagar
        
        Retorna la lista client con la informacion de todos los acompañantes'''
    travel = False
    clients = []
    i = 0
    # se utiliza un ciclo while para repetir el formulario el numero de veces necesario
    while travel == False:
        # si i es igual al numero de travelers se retorna la lista con toda la informacion de los acompañantes
        if i == travelers:
            return clients
        # en caso contrario se despliegan las preguntas necesarias
        else:
            aux = True
            client = []
            name = []
            print("A continuacion se imprime el formulario para los acompañantes")
            # se le pide al cliente su nombre
            while aux == True:
                nombre = input("Introduzca su nombre: ").lower()
                # si el nombre no contiene numeros,espacios o simbolos
                if nombre.isalpha:
                    # se agrega a la lista name
                    name.append(nombre)
                    aux = False
                else:
                    print("Introduzca un nombre valido")
            aux = True
            # se le pide el apellido al cliente
            while aux == True:
                apellido = input("Introduzca su apellido: ").lower()
                # si el apellido no contiene numeros, espacios o simbolos
                if apellido.isalpha:
                    # se agrega a la lista name
                    name.append(apellido)
                    aux = False
                else:
                    print("Introduzca un apellido valido")
            # se juntan el nombre y el apellido en un solo string
            name = " ".join(name)
            # se agrega name a la lista client
            client.append(name)
            aux = True
            # se le pide la edad al cliente
            while aux == True:
                # se utuliza try/except par evitar errores
                try:
                    edad = int(input("Introduzca su edad: "))
                    if edad > 0:
                        client.append(edad)
                        aux = False
                    else:
                        print("Introduzca una edad valida")
                # si edad no es un numero despliega un mensaje de error
                except ValueError:
                    print("Introduzca una edad valida")
            aux = True
            # se le pide al cliente su dni
            while aux == True:
                # se utiliza try/except para evitar errores
                try:
                    dni = int(input("Introduzca su DNI: "))
                    # si dni es un numero de 8 digitos
                    if dni > 10000000:
                        client.append(dni)
                        aux = False
                # en caso del dni no ser un numero despliega un mensaje de error
                except ValueError:
                    print("Introduzca un DNI valido")
            # se suma 1 a la variable i para ver sise repite el proceso o no
            i += 1
            clients.append(client)
            
def vender(barcos):
    '''Funcion encargada de las ventas de Saman Cruceros
    
        Recibe la lista con los objetos de tipo Crucero
        
        Retorna una lista con los objetos de tipo cliente'''
    aux = True
    # se le pregunta al cliente el metodo por el que desea escoger su barco
    while aux == True:
        opcion = int(input("Desea comprar su boleto por (1) nombre del barco, (2) ruta del barco o (3) desea ver los cruceros disponibles:  "))
        # si escoge por nombre del barco
        if opcion == 1:
            found = False
            nombre = input("Introduzca el nombre del barco: ").lower()
            # se recorre la lista de barcos con todos los obejtos de tipo Crucero
            for crucero in barcos:
                # se llama al metodo de Crucero Nombre() y si se encuentra un barco con ese nombre
                if crucero.Nombre().lower() == nombre:
                    found = True
                    # se iguala la variable nombre_barco al nombre del crucero seleccionado
                    nombre_barco = crucero.Nombre()
                    # se llama al metodo de Crucero Tickets() 
                    crucero.Tickets()
                    # se imprime la informacion del barco seleccionado mediante el metodo Info_Barco()
                    print(crucero.Info_Barco())
                    aux = False\
            # si no hay ningun barco con el nombre introducido
            if found == False:
                print("no se encontro un crucero con ese nombre")
        # si la opcion del cliente es por la ruta del barco
        elif opcion == 2:
            found = False
            # se le pide que introduzca el lugar de partida que desea
            salida = input("Introduzca el lugar de partida de su preferencia: ").lower()
            # se recorre la lista de objetos de tipo Crucero
            for crucero in barcos:
                # se llama al metodo de Crucero Ruta()
                ruta = crucero.Ruta()
                # si el lugar de salida introducido es igual al lugar de salida desplegado en el crucero
                if ruta[0].lower() == salida:
                    found = True
                    nombre_barco = crucero.Nombre()
                    crucero.Tickets()
                    print(crucero.Info_Barco())
                    aux = False
            # si no hay ningun barco con esa ruta
            if found == False:
                print("No se encontro crucero con ese punto de salida")
        # si el cliente solo desea ver todos los barcos disponibles
        elif opcion == 3:
            found = False
            # se enumeran e imprime la informacion de todos los cruceros mediante el metodo Info_Barco()
            for i,crucero in enumerate(barcos):
                print(f"{i+1} {crucero.Info_Barco()}")
            # se le pide al cliente que introduzca el numero del barco a seleccionar
            seleccion = int(input("Seleccion el barco de su preferencia: "))
            # se recorre la lista con los objetos de tipo Crucero
            for i,crucero in enumerate(barcos):
                # si seleccion es igual a la posicion del objeto dentro de la lista + 1
                if i+1 == seleccion:
                    found = True
                    nombre_barco = crucero.Nombre()
                    crucero.Tickets()
                    print(f" Usted selecciono {crucero.Info_Barco()}")
                    aux = False
            if found == False:
                print("Introduzca un numero valido")
        # si no se encuentra la seleccion
        else:
            print("Introduzca una opcion valida")
    # a continuacion se recopila la informacion de los clientes        
    clientes = []
    # se llama a la funcion compelte_form()
    main_traveler = complete_form()
    aux = True
    # se le pregunta al cliete si tiene acompañantes
    while aux == True:
        # se utiliza try/except para evitar errores
        try:
            travelers = int(input("Introduzca el numero de personas que viajan con usted: "))
            if travelers >= 0:
                aux = False
            else:
                print("Introduzca un numero de acompañantes valido")
        # si travelers no es un numero despliega un mensaje de error
        except ValueError:
            print("Introduzca un numero de acompañantes valido")
    # se llama a la funcion rest_form() para obtener la informacion de los acompañantes
    side_travelers = rest_form(travelers)

    aux = True
    # se le pregunta al cliente la informacion de la habitacion de su proeferencia
    while aux == True:
        print("Que tipo de habitacion desea comprar?")
        seleccion = input("Presione (1) Sencilla, (2) para Premium o (3) para Vip: ")
        # si selecciona una habitacion simple
        if seleccion == "1":
            room_type = "simple"
            # se recorre la lista de objetos de tipo Crucero
            for crucero in barcos:
                # si el crucero posee el nombre del crucero seleccionado anteriormente
                if crucero.Nombre() == nombre_barco:
                    # se llama al metodo Room_Info()
                    info = crucero.Room_Info(room_type)
            # se imprime la informacion del tipo de habitacion seleccionado
            print(f"""------ Informacion del tipo de habitacion ------
                        Capacidad: {info[0]} personas
                        Precio: {info[1]}$
                        Posee servicio al Cuarto """ )
            # si el numero de viajeros es mayor a la capacidad del cuarto seleccionado
            if travelers > info[0]:
                print("Debera comprar multiples habitaciones de este tipo")
                aux2 = True
                # se le pregunta si desea comprar una habitacion mas grande para acomodar a todos los viajeros
                while aux2 == True:
                    opcion = input("Desea comprar una habitacion mas grande? ").lower()
                    # si el cliente responde que no se seleccionaran multiples habitaciones
                    if opcion == "no":
                        # se divide el numero de viajeros entre la capacidad del cuarto para determinar cuantas habitaciones se deberan comprar
                        rooms = math.ceil((travelers+1)/info[0])
                        precio = info[1]*rooms
                        for crucero in barcos:
                            if crucero.Nombre() == nombre_barco:
                                # se llama al metodo de Crucero Room()
                                room = crucero.Room(room_type,rooms)
                                aux2 = False
                                aux = False
                    # si el cliente escoge que desea comprar una habitacion mas grande se repite el proceso       
                    elif opcion == "si":
                        aux2 = False
                    else:
                        print("Introduzca si o no")
            # si el numero de viajeros en menor o igual a la capacidad de la habitacion
            else:
                rooms = 1
                precio = info[1]
                for crucero in barcos:
                    if crucero.Nombre() == nombre_barco:
                        # se llama al metodo de Crucero Room()
                        room = crucero.Room(room_type,rooms)
                        aux = False
        # si el cliente selecciona el tipo de habitacion premium
        elif seleccion == "2":
            room_type = "premium"
            for crucero in barcos:
                if crucero.Nombre() == nombre_barco:
                    info = crucero.Room_Info(room_type)
            print(f"""------ Informacion del tipo de cuarto ------
                        Capacidad: {info[0]} personas
                        Precio: {info[1]}$
                        Posee Vista el mar""")
            if travelers+1 > info[0]:
                print("Debera comprar multiples habitaciones de este tipo")
                aux2 = True
                while aux2 == True:
                    opcion = input("Desea comprar una habitacion mas grande? ").lower()
                    if opcion == "no":
                        rooms = math.ceil((travelers+1)/info[0])
                        precio = info[1]*rooms
                        for crucero in barcos:
                            if crucero.Nombre() == nombre_barco:
                                room = crucero.Room(room_type,rooms)

                        aux2 = False
                        aux = False
                    elif opcion == "si":
                        aux2 = False
                    else:
                        print("Introduzca si o no")
            else:
                rooms = 1
                precio = info[1]
                for crucero in barcos:
                    if crucero.Nombre() == nombre_barco:
                        room = crucero.Room(room_type,rooms)
                aux = False
        # si el cliente selecciona el tipo de habitacion vip
        elif seleccion == "3":
            room_type = "vip"
            for crucero in barcos:
                if crucero.Nombre() == nombre_barco:
                    info = crucero.Room_Info(room_type)
            print(f"""------ Informacion del tipo de cuarto ------
                        Capacidad: {info[0]} personas
                        Precio: {info[1]}$
                        Posee la capacidad de hacer fiestas """)
            if travelers+1 > info[0]:
                print("Debera comprar multiples habitaciones de este tipo")
                aux2 = True
                while aux2 == True:
                    opcion = input("Desea comprar una habitacion mas grande? ").lower()
                    if opcion == "no":
                        rooms = math.ceil((travelers+1)/info[0])
                        precio = info[1]*rooms
                        for crucero in barcos:
                            if crucero.Nombre() == nombre_barco:
                                room = crucero.Room(room_type,rooms)
                        aux2 = False
                        aux = False
                    elif opcion == "si":
                        aux2 = False
                    else:
                        print("Introduzca si o no")
            else:
                rooms = 1
                precio = info[1]
                for crucero in barcos:
                    if crucero.Nombre() == nombre_barco:
                        room = crucero.Room(room_type,rooms)
                aux = False
    aux = True
    # se le pregunta al cliente si desea comprar un tour
    while aux == True:
        tour = input("Desea comprar un tour?: ").lower()
        # si escoge que si
        if tour == "si":
            #se llama a la funcion vender_tour()
            precio_tour = vender_tour(nombre_barco,travelers+1,barcos)
            tour = True
            aux = False
        # en caso contrario se omite este paso
        elif tour == "no":
            tour = False
            aux = False
        else:
            print("Introduzca una opcion valida")
    # si solo hay 1 viajero
    if len(side_travelers) == 0:
        # se llama a la funcion descuento
        descuento = descuentos(precio,main_traveler[2],main_traveler[1])
        # si se compro un tour
        if tour == True:
            precio += precio_tour
        # se saca la habitacion de la lsita room
        for habitacion in room:
            habitacion = room[0]
            print(habitacion.Info())
        # se crea el objeto de tipo Cliente con toda la informacion recopilada
        cliente = Cliente(main_traveler[0],main_traveler[2],main_traveler[1],nombre_barco,habitacion,precio,descuento,tour)
        # se agrega el objeto a la lista clientes
        clientes.append(cliente)
        return clientes
    # si hay mas de 1 viajero
    elif len(side_travelers) > 0:
        # p = personas y h = habitacioens
        p = 1
        h = 0  
        # se recorre la lista de acompañantes para crear los distintos objetos de tipo Cliente     
        for i in range(len(side_travelers)):
            name = side_travelers[i][0]
            edad = side_travelers[i][1]
            dni = side_travelers[i][2]
            price = 0
            discount = 0
            # si hay mas de una habitacion de distribuyen entre los viajeros
            if p % info[0] == 0 and len(room) != 1:
                h += 1
                habitacion = room[h]
            else:
                habitacion = room[h]
            # se crea el objeto de tipo Cliente
            cliente = Cliente(name,dni,edad,nombre_barco,habitacion,price,discount,tour)
            clientes.append(cliente)
            # se suma 1 a p para repetir el proceso
            p += 1
            # se llama ala funcion descuento para calcular el descuento
            descuento = descuentos(precio,side_travelers[i][2],side_travelers[i][1])
        # en caso de comprar tour
        if tour == True:
            precio += precio_tour 
        # se imprime la informacion de las habitaciones
        for habitacion in room:
            print(habitacion.Info())   
        # se crea el objeto de tipo Cliente de la eprsona a pagar             
        cliente = Cliente(main_traveler[0],main_traveler[2],main_traveler[1],nombre_barco,room_type,habitacion,precio,descuento)
        clientes.append(cliente)
        return clientes
    
def vender_tour(nombre_barco,travelers,barcos):
    '''Funcion encargada de vender los tours a los clientes
        Recibe: 
        --------------------------
        nombre_barco : string, nombre del crucero seleccionado
        travelers : int, numero de viajeros
        barcos : list, lista de objetos de tipo crucero
        
        Retorna el precio a pagar por el tour seleccionado'''
    # se recorre la lsita de objetos de tipo Crucero
    for crucero in barcos:
        if nombre_barco == crucero.Nombre():
            # se llama al metodo de Crucero Tours()
            tours = crucero.Tours()
    aux = True
    # se imprime la informacion de los tours
    while aux == True:
        print("""------- Tipos de tour disponibles -------
                 1.- Tour en el puerto:
                       Precio: 30$ c/u
                       Hora: 7 A.M
                 2.- Degustacion de comida:
                       Precio: 100$ c/u
                       Hora: 12 P.M
                 3.- Trote por el pueblo:
                       Precio: Gratis
                       Hora: 6 A.M
                 4.- Visita a lugares historicos: 
                       Precio: 40$ c/u
                       Hora: 10 A.M""")
        # se le pide al cliente que seleccione un tour
        seleccion = int(input("Seleccione un tour: "))
        # si se selecciona el tour del puerto
        if seleccion == 1:
            aux2 = True
            while aux2 == True:
                try:
                    # se pregunta cuantas personas van al tour
                    personas = int(input("Cuntas personas van al tour: "))
                    if personas > 0:
                        aux2 = False
                # en caso de persopnas no ser un numero
                except ValueError:
                    print("Introduzca un numero de perosnas valido")
            
            nombre = "Tour Puerto"
            # se recorre la lista de objetos de tipo Tour
            for tour in tours:
                # si el tour seleccionado es igual al nombre del objeto Tour
                if nombre == tour.Nombre():
                    # se llama al metodo de Tour Cupos()
                    precio = tour.Cupos(personas)
                    # si el precio del tour es un numero
                    if precio.isdecimal:
                        precio = int(precio)
                        return precio
                    # en caso de no haber cupos
                    else:
                        print(precio)
         # si se selecciona la degustacion       
        elif seleccion == 2:
            aux2 = True
            while aux2 == True:
                try:
                    personas = int(input("Cuntas personas van al tour: "))
                    if personas > 0:
                        aux2 = False
                except ValueError:
                    print("Introduzca un numero de perosnas valido")
            
            nombre = "Degustacion"
            for tour in tours:
                if nombre == tour.Nombre():
                   precio = tour.Cupos(personas)
                   if precio.isdecimal:
                       precio = int(precio)
                       return precio
                   else:
                        print(precio)
        # si se selecciona el trote
        elif seleccion == 3:
            aux2 = True
            while aux2 == True:
                try:
                    personas = int(input("Cuntas personas van al tour: "))
                    if personas > 0:
                        aux2 = False
                except ValueError:
                    print("Introduzca un numero de perosnas valido")
            
            nombre = "Trote"
            for tour in tours:
                if nombre == tour.Nombre():
                    precio = tour.Cupos(personas)
                    if precio.isdecimal:
                        precio = int(precio)
                        return precio
                    else:
                        print(precio) 
        # si se selecciona la visita a lugares historicos
        elif seleccion == 4:
            aux2 = True
            while aux2 == True:
                try:
                    personas = int(input("Cuntas personas van al tour: "))
                    if personas > 0:
                        aux2 = False
                except ValueError:
                    print("Introduzca un numero de perosnas valido")
            
            nombre = "Lugares Historicos"
            for tour in tours:
                if nombre == tour.Nombre():
                    precio = tour.Cupos(personas)
                    if precio.isdecimal:
                        precio = int(precio)
                        return precio
                    else:
                        print(precio)
        # en caso de una seleccion erronea
        else:
            print("Seleccione una opcion valida")

def restaurante(barcos):
    '''Funcion encargada del modulo de restaurantes
        Recibe: barcos : list, lista de objetos de tipo crucero'''
    aux = True
    found = False
    # se le pide al cliente que introduzca el nombre de su barco
    while aux == True:
        barco = input("Inroduzca el nombre de su barco: ").lower()
        # se recorer la lista barcos
        for crucero in barcos:
            # si el nombre introducido es igual al nomrbe de un crucero
            if barco == crucero.Nombre():
                # se cambia el booleano a true
                found = True
        # si se encontro el barco
        if found  == True:
            # se llama al metodo de Crucero Restaurante()
            restaurante = Restaurante()
            # se llama al metodo de Restaurante Api_Platillos()
            restaurante.API_Platillos(crucero.Sells())
            aux = False
        # en caso de no encontrarse el barco
        else:
            print("No se ha encontrado un barco con ese nombre")
    aux = True
    # se le pregunta el cliente que desea hacer en el modulo
    while aux == True:
        opcion = input("Introduzca (1) para agregar un platillo,(2) Agregar un combo, (3) Comprar, (4) para eliminar un platillo del menu,(5) para modificar un platillo o (6) Para salir del modulo de resturantes: ")
        # en caso de seleccionar agregar un platillo
        if opcion == "1":
            aux2 = True
            while aux2 == True:
                # se llama al metodo Add_Platillo()
                print(restaurante.Add_Platillo())
                # se le pregunta si desea agregar otro platillo
                again = input("Desea agragar otro platillo o realizar otra accion dentro del modulo?: ").lower()
                # en caso de no se termina el modulo
                if again == "no":
                    return "Gracias por su asistencia"
                # en caso de si se repite el ciclo
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        # si se seleccion agregar un combo
        elif opcion == "2":
            aux2 = True
            while aux2 == True:
                # se llama al metodo de Restaurante Add_Combo()
                print(restaurante.Add_Combo())
                again = input("esea agragar otro combo o realizar otra accion dento del modulo?: ").lower()
                if again == "no":
                    return "Gracias por su asistencia"
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        # si se desea comprar algo en el restaurante
        elif opcion == "3":
            aux2 = True
            while aux2 == True:
                # se llama al metodo de Restaurante Buy()
                print(restaurante.Buy())
                again = input("Desea comprar otro platillo del restaurante?: ").lower()
                if again == "no":
                    return "Gracias por su compra"
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        # si se desea eliminar un platillo o combo
        elif opcion == "4":
            # se llama al metodo Eliminar_Platillo()
            print(restaurante.Eliminar_Platillo())
        # si se desea modificar algo en el menu
        elif opcion == "5":
            # se llama al metodo Modificar()
            print(restaurante.Modificar())
        # si desea salir del modulo
        elif opcion == "6":
            return "Gracias por su asistencia"

def estadisticas(barcos,clientes):
    '''Funcion encargada del modulo de estadisticas
        Recibe:
        ------------
        barcos: list, lista de objetos de tipo Crucero
        clientes: list, lista de objetos de tipo Cliente'''
    info_clientes = []
    top_3 = []
    promedio_gastos = 0
    no_tour = 0
    # se recorre la lista de clientes
    for cliente in clientes:
        # se llama al metodo Stats()
        info_clientes.append(cliente.Stats())
    # se ordena la lista info_clientes
    info_clientes = sorted(info_clientes)
    # se ordena de mayor a menor
    info_clientes.reverse()
    # se recorre la lsita info_clientes
    for i in range(len(info_clientes)):
        # se suma el monto de cada cliente a promedio_gastos
        promedio_gastos += info_clientes[i][0]
        if i <= 2:
            # se agregan los 3 primeros clietnes a top_3
            top_3.append(info_clientes[i])
        # si no compraron tour  
        if info_clientes[i][2] == "False":
            # se suma 1 por cada false encontrado en info_clientes
            no_tour += 1
    # se divide el la suma de los gastos entre la cantidad de clientes para calcular el promedio de los gastos
    promedio_gastos = promedio_gastos / len(info_clientes)
    # se imprime el promedio de los gastos
    print(f"El promedio de gastos de todos los clientes es: {promedio_gastos}$")
    # se calcula el porcentaje de clientes que no compraron tour
    notour = (no_tour*100) / len(info_clientes)
    # se imprime el porcentaje
    print(f"El porcentaje de personas que no compran tour es: {notour}%")
    # se impromen los 3 clientes que son mas fieles a la linea
    print("Los 3 Clientes mas fieles a Saman Cruceros son:")
    i = 0
    # se recorre la lista clientes
    for cliente in clientes:
        # si el nombre del cliente es igual al que esta en top_3
        if cliente.Nombre() == top_3[i][1]:
            # se imprime la informacion del cliente
            print(f"{i+1} {cliente.Info()}")
            if i < 2:
                i += 1
    # para calcular los barcos con mas venta de tickets
    for barco in barcos:
        # se recorre la lista barcos y se llama al metodo Tickets()
        for i in range(len(info_clientes)):
            if info_clientes[i][3] == barco.Nombre():
                barco.Tickets()
    tickets = []
    for barco in barcos:
        # se llama al metodo Stats() y se agrega el numero de tickets vendidos a la lsita tickets
        ticket = barco.Stats()
        tickets.append(ticket)
    # se ordena la lista y se invierte de mayor a menor
    tickets = sorted(tickets)
    tickets.reverse()
    i = 0
    # se imprimen la informacion de los barcos con mas tickets
    print("Los 3 barcos con los tickets mas vendidos son: ")
    for barco in barcos:
        if barco.Stats() == tickets[i]:
            print(f"{i+1} {barco.Info_Barco()}")
            if i < 2:
                i += 1

def read(txt_file,barcos = 0):
    '''Funcion encargada de leer los archivos txt y crear nuevamente los objetos guardados
        Recibe: 
        -----------------
        txt_file : archivo txt a leer
        barcos: lista de objetos de tipo Crucero
        retorna la lista de objetos creados'''
    lista = []
    # se lee el archivo txt y se extrae la informacion
    with open(txt_file,"r") as t:
        for line in t:
            line = line.strip()
            lista.append(line.split(";"))
    saves = []
    for i in range(len(lista)):
        # en caso de ser objetos de tipo cliente
        if lista[i][0] == "cliente":
            # se recopila la informacion para crear los atributos de los objetos
            nombre = lista[i][1]
            identidad = int(lista[i][2])
            edad = int(lista[i][3])
            nombre_barco = lista[i][4]
            habitacion = []
            habitacion.append(lista[i][5])
            habitacion.append(lista[i][6])
            habitacion.append(lista[i][7])
            habitacion.append(lista[i][8])
            habitacion.append(lista[i][9])
            monto = float(lista[i][10])
            descuento = float(lista[i][11])
            tour = lista[i][12]
            # se crea el objeto de tipo cliente
            cliente = Cliente(nombre,identidad,edad,nombre_barco,habitacion,monto,descuento,tour)
            # se llama al metodo Habitacion()
            cliente.Habitacion()
            # se agrega el objeto a la lsita saves
            saves.append(cliente)
        # en caso de ser objetos de tipo Plato
        elif lista[i][0] == "comida":
            for i in range(len(lista)):
                # se extrae el nombre del barco
                barco = lista[i][1]
                for barco in barcos:
                    # si se encuentra el crucero
                    if barco.Nombre() == barco:
                        # se extrae la informacion apra crear los objetos
                        platillo = []
                        platillo.append(lista[i][2])
                        platillo.append(float(lista[i][3]))
                        platillo.append(int(lista[i][4]))
                        platillo.append(int(lista[i][5]))
                        # se llama al metodo Restaurante()
                        restaurante = barco.Restaurante()
                        # se llama al metodo de Restaurante Txt_platillos()
                        restaurante.Txt_platillos(platillo)             
    return saves

def write(lista):
    '''Funcion encargada de escribir los datos en los distintos txt
        Recibe: lista : list, lista que se desea guardat en el txt'''
    for item in lista:
        # se llama al metodo de objeto Write_data()
        item.Write_data()  

def crucero_API():
    '''Funcion encargada de obtener la informacion del api'''

    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    response = requests.request("GET",url)
    return response.json()

def main():
    '''Funcion encargada de correr el programa'''
    fin = False
    # se llama ala funcion crucero_Api()
    cruceros = crucero_API()
    # se obtienen los objetos de tipo crucero
    barcos = cruceros_disponibles(cruceros)
    # se llama ala funcion read() para obtener los clietnes guardados
    clientes = read("cliente.txt")
    # se llama a la funcion read para obtener los paltillos guardados
    read("menu.txt",barcos)
    # se recorre la lista barcos
    for barco in barcos:
        # se recorre la lsita clientes
        for cliente in clientes:
            # se llama al metodo de Cliente Ocupar()
            info = cliente.Ocupar()
            if barco.Nombre() == info[0]:
                # se llama al metodo de Crucero Ocupar_Room()
                barco.Ocupar_Room(info[1],info[2])
    # comienza el programa
    while fin == False:
        print("BIENVENIDO A SAMAN CRUCEROS")
        aux = True
        # se le pregunta al cliente que desea hacer
        while aux == True:
            opcion = input("Introduzca (1) para comprar un boleto, (2) para el modulo de restaurantes o (3) para el modulo de estadisticas: ")
            # si desea comprar un boleto
            if opcion == "1":
                # se llama a la funcioon vender()       
                personas = vender(barcos)
                # se agregan los nuevos clientes a la lista clientes
                for persona in personas:
                    # se llama al metodo Factura() de Cliente
                    print(persona.Factura())
                    clientes.append(persona)
                aux = False
            # si desea ver el modulo de restaurantes
            elif opcion == "2":
                print(restaurante(barcos))
                aux = False
            # si desea ver el modulo de estadisticas
            elif opcion == "3":
                if len(clientes) == 0:
                    print("Todavia no se pueden acceder a las estadisticas")
                else:
                    print(estadisticas(barcos,clientes))
                    aux = False
            else:
                print("Introduzca una opcion valida")
        aux = True
        # se pregunta si desea realizar algo ams en el programa
        while aux == True:
            opcion = input("Desea introducir a otro cliente o realizar otra funcion dentro del programa?: ").lower()
            # en caso de no
            if opcion == "no":
                # se escribe la informacion en sus respectivos txt
                write(clientes)
                for barco in barcos:
                    barco.Write()
                aux = False
                fin = True
            # en caso de si se repite el programa
            elif opcion == "si":
                aux = False
            else:
                print("Introduzca si o no")


   
main()