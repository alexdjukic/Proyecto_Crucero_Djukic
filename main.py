from Crucero import Crucero
from Habitacion import Habitacion 
from Sencilla import Sencilla 
from Premium import Premium
from Vip import Vip
def vender():
    aprovado = False
    while aprovado == False:
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
                documento_identidad = int(input("Introduzca el numero de su documento de identidad: "))
                if documento_identidad > 0:
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



        

def main():
    #aqui todo lo del proyecto crucero
    print("BIENVENIDO A SAMAN CRUCEROS")
   
main()