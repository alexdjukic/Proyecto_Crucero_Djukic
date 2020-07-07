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




def vender():
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
            cliente = Cliente(nombre,doc_identidad,edad,habitacion,monto,descuento)
            clientes.append(cliente)
            i += 1



        

def main():
    #aqui todo lo del proyecto crucero
    print("BIENVENIDO A SAMAN CRUCEROS")
    clientes = vender()
    for cliente in clientes:
        print(cliente.Factura())

   
main()