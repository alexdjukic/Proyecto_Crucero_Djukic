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
    aux = True
    while aux == True:
        if i == doc_identidad:
            return True
        elif doc_identidad % i == 0:
            return False
        else:
            i += 1

def is_abundant(doc_identidad, i = 2):
    aux = True
    divisores = []
    while aux == True:
        if i == doc_identidad:
            aux = False
        elif doc_identidad % i == 0:
            divisores.append(i)
            i += 1
        else:
            i += 1
    suma = 0
    for i in range(len(divisores)):
        suma += divisores[i]
    
    if suma > doc_identidad:
        return True
    else:
        return False

def descuentos(monto,doc_identidad,edad):
    if is_prime(doc_identidad) == True:
        descuento = monto * 0.1
        return descuento
    
    elif is_abundant(doc_identidad) == True:
        descuento = monto * 0.15
        return descuento
    
    elif edad >= 65:
        aux = True
        while aux == True:
            discapacidad = input("Posee alguna discapacidad: ").lower()
            if discapacidad == "si":
                descuento = monto * 0.3
                return descuento
            elif discapacidad == "no":
                descuento = 0
                return descuento
            else:
                print("Introduzca si o no")
    else:
        descuento = 0 
        return descuento

def cruceros_disponibles(cruceros):
    cruceros_disponibes = []
    for crucero in cruceros:
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
        barco = Crucero(nombre,ruta,fecha,n_habitaciones,cantidad_sencilla,costo_simple,cantidad_premium,costo_premium,cantidad_vip,costo_vip,sells)
        barco.Create_rooms()
        barco.Restaurante()
        cruceros_disponibes.append(barco)
    return cruceros_disponibes

def complete_form():
    aux = True
    client = []
    name = []
    print("A continuacion se imprime el formulario de la persona que va a pagar")
    while aux == True:
        nombre = input("Introduzca su nombre: ").lower()
        if nombre.isalpha:
            name.append(nombre)
            aux = False
        else:
            print("Introduzca un nombre valido")
    aux = True
    while aux == True:
        apellido = input("Introduzca su apellido: ").lower()
        if apellido.isalpha:
            name.append(apellido)
            aux = False
        else:
            print("Introduzca un apellido valido")
    
    name = " ".join(name)
    client.append(name)
    aux = True
    while aux == True:
        try:
            edad = int(input("Introduzca su edad: "))
            if edad > 18:
                client.append(edad)
                aux = False
            else:
                print("Introduzca una edad valida")
        except ValueError:
            print("Introduzca una edad valida")
    aux = True
    while aux == True:
        try:
            dni = int(input("Introduzca su DNI: "))
            if dni > 0:
                client.append(dni)
                aux = False
        except ValueError:
            print("Introduzca un DNI valido")
        
    return client

def rest_form(travelers):
    travel = False
    clients = []
    i = 0
    while travel == False:
        if i == travelers:
            return clients
        else:
            aux = True
            client = []
            name = []
            print("A continuacion se imprime el formulario para los acompañantes")
            while aux == True:
                nombre = input("Introduzca su nombre: ").lower()
                if nombre.isalpha:
                    name.append(nombre)
                    aux = False
                else:
                    print("Introduzca un nombre valido")
            aux = True
            while aux == True:
                apellido = input("Introduzca su apellido: ").lower()
                if apellido.isalpha:
                    name.append(apellido)
                    aux = False
                else:
                    print("Introduzca un apellido valido")
            
            name = " ".join(name)
            client.append(name)
            aux = True
            while aux == True:
                try:
                    edad = int(input("Introduzca su edad: "))
                    if edad > 0:
                        client.append(edad)
                        aux = False
                    else:
                        print("Introduzca una edad valida")
                except ValueError:
                    print("Introduzca una edad valida")
            aux = True
            while aux == True:
                try:
                    dni = int(input("Introduzca su DNI: "))
                    if dni > 0:
                        client.append(dni)
                        aux = False
                except ValueError:
                    print("Introduzca un DNI valido")
            i += 1
            clients.append(client)
            
def vender(barcos):
    aux = True
    while aux == True:
        opcion = int(input("Desea comprar su boleto por (1) nombre del barco, (2) ruta del barco o (3) desea ver los cruceros disponibles:  "))
        if opcion == 1:
            found = False
            nombre = input("Introduzca el nombre del barco: ").lower()
            for crucero in barcos:
                if crucero.Nombre().lower() == nombre:
                    found = True
                    nombre_barco = crucero.Nombre()
                    crucero.Tickets()
                    print(crucero.Info_Barco())
                    aux = False
            if found == False:
                print("no se encontro un crucero con ese nombre")

        elif opcion == 2:
            found = False
            salida = input("Introduzca el lugar de partida de su preferencia: ").lower()
            for crucero in barcos:
                ruta = crucero.Ruta()
                if ruta[0].lower() == salida:
                    found = True
                    nombre_barco = crucero.Nombre()
                    crucero.Tickets()
                    print(crucero.Info_Barco())
                    aux = False
            if found == False:
                print("No se encontro crucero con ese punto de salida")

        elif opcion == 3:
            found = False
            for i,crucero in enumerate(barcos):
                print(f"{i+1} {crucero.Info_Barco()}")
            seleccion = int(input("Seleccion el barco de su preferencia: "))
            for i,crucero in enumerate(barcos):
                if i+1 == seleccion:
                    found = True
                    nombre_barco = crucero.Nombre()
                    crucero.Tickets()
                    print(f" Usted selecciono {crucero.Info_Barco()}")
                    aux = False
            if found == False:
                print("Introduzca un numero valido")

        else:
            print("Introduzca una opcion valida")
            
    clientes = []
    main_traveler = complete_form()
    aux = True
    while aux == True:
        try:
            travelers = int(input("Introduzca el numero de personas que viajan con usted: "))
            if travelers >= 0:
                aux = False
            else:
                print("Introduzca un numero de acompañantes valido")
        except ValueError:
            print("Introduzca un numero de acompañantes valido")

    side_travelers = rest_form(travelers)

    aux = True
    while aux == True:
        print("Que tipo de habitacion desea comprar?")
        seleccion = input("Presione (1) Sencilla, (2) para Premium o (3) para Vip: ")
        if seleccion == "1":
            room_type = "simple"
            for crucero in barcos:
                if crucero.Nombre() == nombre_barco:
                    info = crucero.Room_Info(room_type)
            print(f"""------ Informacion del tipo de cuarto ------
                        Capacidad: {info[0]} personas
                        Precio: {info[1]}$
                        Posee servicio al Cuarto """ )
            if travelers > info[0]:
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
        if seleccion == "2":
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
        if seleccion == "3":
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
    while aux == True:
        tour = input("Desea comprar un tour?: ").lower()
        if tour == "si":
            precio_tour = vender_tour(nombre_barco,travelers+1,barcos)
            tour = True
            aux = False
        elif tour == "no":
            tour = False
            aux = False
        else:
            print("Introduzca una opcion valida")

    if len(side_travelers) == 0:
        descuento = descuentos(precio,main_traveler[2],main_traveler[1])
        if tour == True:
            precio += precio_tour
        for habitacion in room:
            habitacion = room[0]
            print(habitacion.Info())

        cliente = Cliente(main_traveler[0],main_traveler[2],main_traveler[1],nombre_barco,habitacion,precio,descuento,tour)
        clientes.append(cliente)
        return clientes
    
    elif len(side_travelers) > 0:
        p = 1
        h = 0       
        for i in range(len(side_travelers)):
            name = side_travelers[i][0]
            edad = side_travelers[i][1]
            dni = side_travelers[i][2]
            price = 0
            discount = 0
            if p % info[0] == 0 and len(room) != 1:
                h += 1
                habitacion = room[h]
            else:
                habitacion = room[h]
            print(habitacion)
            cliente = Cliente(name,dni,edad,nombre_barco,habitacion,price,discount,tour)
            clientes.append(cliente)
            p += 1
            descuento = descuentos(precio,side_travelers[i][2],side_travelers[i][1])
        if tour == True:
            precio += precio_tour 
        for habitacion in room:
            print(habitacion.Info())                  
        cliente = Cliente(main_traveler[0],main_traveler[2],main_traveler[1],nombre_barco,room_type,habitacion,precio,descuento)
        clientes.append(cliente)
        return clientes
    
def vender_tour(nombre_barco,travelers,barcos):
    for crucero in barcos:
        if nombre_barco == crucero.Nombre():
            tours = crucero.Tours()
    aux = True
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
        seleccion = int(input("Seleccione un tour: "))
        if seleccion == 1:
            aux2 = True
            while aux2 == True:
                try:
                    personas = int(input("Cuntas personas van al tour: "))
                    if personas > 0:
                        aux2 = False
                except ValueError:
                    print("Introduzca un numero de perosnas valido")
            
            nombre = "Tour Puerto"
            for tour in tours:
                if nombre == tour.Nombre():
                    precio = tour.Cupos(personas)
                    if precio.isdecimal:
                        precio = int(precio)
                        return precio
                    else:
                        print(precio)
                
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

        else:
            print("Seleccione una opcion valida")

def restaurante(barcos):
    aux = True
    found = False
    while aux == True:
        barco = input("Inroduzca el nombre de su barco: ").lower()
        for crucero in barcos:
            if barco == crucero.Nombre():
                found = True
        if found  == True:
            restaurante = Restaurante()
            restaurante.API_Platillos(crucero.Sells())
            aux = False
        else:
            print("No se ha encontrado un barco con ese nombre")
    aux = True
    while aux == True:
        opcion = input("Introduzca (1) para agregar un platillo,(2) Agregar un combo, (3) Comprar, (4) para eliminar un platillo del menu,(5) para modificar un platillo o (6) Para salir del modulo de resturantes: ")
        if opcion == "1":
            aux2 = True
            while aux2 == True:
                print(restaurante.Add_Platillo())
                again = input("Desea agragar otro platillo o realizar otra accion dentro del modulo?: ").lower()
                if again == "no":
                    return "Gracias por su asistencia"
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        elif opcion == "2":
            aux2 = True
            while aux2 == True:
                print(restaurante.Add_Combo())
                again = input("esea agragar otro combo o realizar otra accion dento del modulo?: ").lower()
                if again == "no":
                    return "Gracias por su asistencia"
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        elif opcion == "3":
            aux2 = True
            while aux2 == True:
                print(restaurante.Buy())
                again = input("Desea comprar otro platillo del restaurante?: ").lower()
                if again == "no":
                    return "Gracias por su compra"
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        elif opcion == "4":
            print(restaurante.Eliminar_Platillo())
        elif opcion == "5":
            print(restaurante.Modificar())
        elif opcion == "6":
            return "Gracias por su asistencia"

def estadisticas(barcos,clientes):
    info_clientes = []
    top_3 = []
    promedio_gastos = 0
    no_tour = 0
    for cliente in clientes:
        info_clientes.append(cliente.Stats())
    info_clientes = sorted(info_clientes)
    info_clientes.reverse()
    for i in range(len(info_clientes)):
        promedio_gastos += info_clientes[i][0]
        if i <= 2:
            top_3.append(info_clientes[i])
        if info_clientes[i][2] == "False":
            no_tour += 1
    promedio_gastos = promedio_gastos / len(info_clientes)
    print(f"El promedio de gastos de todos los clientes es: {promedio_gastos}$")
    notour = (no_tour*100) / len(info_clientes)
    print(f"El porcentaje de personas que no compran tour es: {notour}%")
    print("Los 3 Clientes mas fieles a Saman Cruceros son:")
    i = 0
    for cliente in clientes:
        if cliente.Nombre() == top_3[i][1]:
            print(f"{i+1} {cliente.Info()}")
            if i < 2:
                i += 1
    for barco in barcos:
        for i in range(len(info_clientes)):
            if info_clientes[i][3] == barco.Nombre():
                barco.Tickets()
    tickets = []
    for barco in barcos:
        ticket = barco.Stats()
        tickets.append(ticket)
    tickets = sorted(tickets)
    tickets.reverse()
    i = 0
    print("Los 3 barcos con los tickets mas vendidos son: ")
    for barco in barcos:
        if barco.Stats() == tickets[i]:
            print(f"{i+1} {barco.Info_Barco()}")
            if i < 2:
                i += 1


                


def read(txt_file,barcos = 0):
    lista = []
    with open(txt_file,"r") as t:
        for line in t:
            line = line.strip()
            lista.append(line.split(";"))
    saves = []
    for i in range(len(lista)):
        if lista[i][0] == "cliente":
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
            cliente = Cliente(nombre,identidad,edad,nombre_barco,habitacion,monto,descuento,tour)
            cliente.Habitacion()
            saves.append(cliente)
        elif lista[i][0] == "comida":
            for i in range(len(lista)):
                barco = lista[i][1]
                for barco in barcos:
                    if barco.Nombre() == barco:
                        platillo = []
                        platillo.append(lista[i][2])
                        platillo.append(float(lista[i][3]))
                        platillo.append(int(lista[i][4]))
                        platillo.append(int(lista[i][5]))
                        restaurante = barco.Restaurante()
                        restaurante.Txt_platillos(platillo)             
    return saves

def write(lista):
    for item in lista:
        item.Write_data()  

def crucero_API():
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    response = requests.request("GET",url)
    return response.json()

def main():
    #aqui todo lo del proyecto crucero
    fin = False
    cruceros = crucero_API()
    barcos = cruceros_disponibles(cruceros)
    clientes = read("cliente.txt")
    read("menu.txt",barcos)
    for barco in barcos:
        for cliente in clientes:
            info = cliente.Ocupar()
            if barco.Nombre() == info[0]:
                barco.Ocupar_Room(info[1],info[2])
    while fin == False:
        print("BIENVENIDO A SAMAN CRUCEROS")
        aux = True
        while aux == True:
            opcion = input("Introduzca (1) para comprar un boleto, (2) para el modulo de restaurantes o (3) para el modulo de estadisticas: ")
            if opcion == "1":       
                personas = vender(barcos)
                for persona in personas:
                    print(persona.Factura())
                    clientes.append(persona)
                aux = False
            elif opcion == "2":
                print(restaurante(barcos))
                aux = False
            elif opcion == "3":
                if len(clientes) == 0:
                    print("Todavia no se pueden acceder a las estadisticas")
                else:
                    print(estadisticas(barcos,clientes))
                    aux = False
            else:
                print("Introduzca una opcion valida")
        aux = True
        while aux == True:
            opcion = input("Desea introducir a otro cliente o realizar otra funcion dentro del programa?: ").lower()
            if opcion == "no":
                write(clientes)
                for barco in barcos:
                    barco.Write()
                aux = False
                fin = True
            elif opcion == "si":
                aux = False
            else:
                print("Introduzca si o no")


   
main()