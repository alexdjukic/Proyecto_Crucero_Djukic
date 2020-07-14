from Crucero import Crucero
from Habitacion import Habitacion 
from Sencilla import Sencilla 
from Premium import Premium
from Vip import Vip
from Cliente import Cliente 
from Tour import Tour
from Restaurante import Restaurante
import requests

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
        cantidad_sencilla = int(crucero["capacity"]["simple"])
        costo_simple = float(crucero["cost"]["simple"])
        cantidad_premium = int(crucero["capacity"]["premium"])
        costo_premium = float(crucero["cost"]["premium"])
        cantidad_vip = int(crucero["capacity"]["vip"])
        costo_vip = float(crucero["cost"]["vip"])
        barco = Crucero(nombre,ruta,fecha,cantidad_sencilla,costo_simple,cantidad_premium,costo_premium,cantidad_vip,costo_vip)
        cruceros_disponibes.append(barco)
    
    return cruceros_disponibes

def vender(cruceros):
    barcos = cruceros_disponibles(cruceros)
    aux = True
    while aux == True:
        opcion= int(input("Desea comprar su boleto por (1) nombre del barco, (2) ruta del barco o (3) desea ver los cruceros disponibles:  "))
        if opcion == 1:
            found = False
            nombre = input("Introduzca el nombre del barco: ").lower()
            for crucero in barcos:
                if crucero.Nombre().lower() == nombre:
                    found = True
                    nombre_barco = crucero.Nombre()
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
                    print(f" Usted selecciono {crucero.Info_Barco()}")
                    aux = False
            if found == False:
                print("Introduzca un numero valido")

        else:
            print("Introduzca una opcion valida")


    aux = True
    while aux == True:
        try:
            viajeros = int(input("Cuantas personas viajan en el crucero: "))
            if viajeros > 0:
                aux = False
            else:
                print("Introduzca un numero de viajeros valido")
        except ValueError:
            print("Introduzca un numero de viajeros valido")

    i = 0
    monto = 0
    total = 0
    clientes = []
    habitacion = "A113"
    registro = False
    while registro == False:
        if i == viajeros:
            for crucero in cruceros:
                crucero.Cupos(viajeros)
            return clientes
        else:
            aux = True
            while aux == True:
                nombre = input("Introduzca su nombre: ").lower()
                if nombre.isalpha:
                    aux = False
                else:
                    print("introduzca un nombre valido")
            aux = True
            while aux == True:
                try:
                    doc_identidad = int(input("Introduzca el numero de su documento de identidad: "))
                    if doc_identidad > 0:
                        aux = False
                    else:
                        print("Introduzca un documento de identidad valido")
                except ValueError:
                    print("Introduzca un documento de identidad valido")
            aux = True
            while aux == True:
                try:
                    edad = int(input("Introduzca su edad: "))
                    if edad > 0:
                        aux = False
                    else:
                        print("Introduzca una edad valida")
                except ValueError:
                    print("Introduzca una edad valida")
            total += monto
            descuento = descuentos(total,doc_identidad,edad)
            cliente = Cliente(nombre,doc_identidad,edad,nombre_barco,habitacion,monto,descuento)
            clientes.append(cliente)
            i += 1

def vender_tour(clientes,cruceros):
    aux = True
    while aux == True:
        barco = input("Inreoduzca el nombre de su barco: ").lower()
        if barco.isalpha:
            aux = False
        else:
            print("Introduzca un nombre de barco valido")
    for crucero in cruceros:
        if barco == crucero.Nombre():
            tours = crucero.Tours()
    aux = True
    while aux == True:
        try:
            dni = int(input("Introduzca su dni: "))
            if dni > 0:
                aux = False
            else:
                print("Introduzca un dni valido")
        except ValueError:
            print("Introduzca un dni valido")
    found = False
    for cliente in clientes:
        if dni == cliente.DNI() and barco == cliente.Crucero():
            found = True

    if found == False:
        print("El cliente no esta registrado en ningun crucero")
    
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
                    return tour.Cupos(personas)
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
                    return tour.Cupos(personas)
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
                    return tour.Cupos(personas)
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
                    return tour.Cupos(personas)

        else:
            print("Seleccione una opcion valida")
                
            
def restaurante(cruceros):
    aux = True
    found = False
    while aux == True:
        barco = input("Inroduzca el nombre de su barco: ").lower()
        if barco.isalpha:
            for crucero in cruceros:
                if barco == crucero.Nombre():
                    found = True
            if found  == True:
                restaurante = Restaurante()
                aux = False
            else:
                print("No se ha encontrado un barco con ese nombre")
        else:
            print("Introduzca un nombre de barco valido")
    aux = True
    while aux == True:
        opcion = input("Introduzca (1) para agregar un platillo, (2) para revisar el menu, (3) para eliminar un platillo del menu, (4) Para salir del modulo de resturantes: ")
        if opcion == "1":
            aux2 = True
            while aux2 == True:
                print(restaurante.Add_Platillo())
                again = input("esea agragar otro platillo o  revisar el menu?: ").lower()
                if again == "no":
                    return "Gracias por su asistencia"
                    aux2 = False
                    aux = False
                elif again == "si":
                    aux2 = False
                else:
                    print("Introduzca si o no")
        elif opcion == "2":
            print(restaurante.Check_Menu())
        elif opcion == "3":
            print(restaurante.Eliminar_Platillo())
        elif opcion == "4":
            return "Gracias por su asistencia"

def crucero_API():
    url = 'https://saman-caribbean.vercel.app/api/cruise-ships'
    response = requests.request("GET",url)
    return response.json()

def main():
    #aqui todo lo del proyecto crucero
    fin = False
    cruceros = crucero_API()
    while fin == False:
        print("BIENVENIDO A SAMAN CRUCEROS")
        aux = True
        while aux == True:
            opcion = input("Introduzca (1) para comprar un boleto, (2) para comprar un tour o (3) para el modulo de restaurantes: ")
            if opcion == "1":       
                clientes = vender(cruceros)
                for cliente in clientes:
                    print(cliente.Factura())
                aux = False
            elif opcion == "2":      
                print(vender_tour(clientes,cruceros))
                aux = False
            elif opcion == "3":
                print(restaurante(cruceros))
                aux = False
            else:
                print("Introduzca una opcion valida")
        aux = True
        while aux == True:
            opcion = input("Desea introducir a otro cliente o realizar otra funcion dentro del programa?: ").lower()
            if opcion == "no":
                aux = False
                fin = True
            elif opcion == "si":
                aux = False
            else:
                print("Introduzca si o no")


   
main()