from Crucero import Crucero
from Habitacion import Habitacion 
from Sencilla import Sencilla 
from Premium import Premium
from Vip import Vip
from Cliente import Cliente 
from Tour import Tour

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




def vender(cruceros):
    for crucero in cruceros:
        print(crucero.Info_Barco())
        barco = crucero.Nombre()
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
            cliente = Cliente(nombre,doc_identidad,edad,barco,habitacion,monto,descuento)
            clientes.append(cliente)
            i += 1

def vender_tour(tours,clientes):
    aux = True
    while aux == True:
        barco = input("Inreoduzca el nombre de su barco: ").lower()
        if barco.isalpha:
            aux = False
        else:
            print("Introduzca un nombre de barco valido")

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
        else:
            print("Seleccione una opcion valida")
                
            

              



        


        

def main():
    #aqui todo lo del proyecto crucero
    fin = False
    cruceros = []
    crucero = Crucero("royal","bahamas","22/7/20",100,30,20,5)
    cruceros.append(crucero)
    for crucero in cruceros:
        tours = crucero.Tours()
    while fin == False:
        print("BIENVENIDO A SAMAN CRUCEROS")
        clientes = vender(cruceros)
        for cliente in clientes:
            print(cliente.Factura())
        print(vender_tour(tours,clientes))
        aux = True
        while aux == True:
            opcion = input("Desea introducir a otro cliente: ").lower()
            if opcion == "no":
                aux = False
                fin = True
            elif opcion == "si":
                aux = False
            else:
                print("Introduzca si o no")


   
main()