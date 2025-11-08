#Practiva2: Classes, objetos, metodos y atributos
class persona:
    def __init__(self, nombre, apellido, edad):#Constructor de la clase
        #Creacion de atributos 
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.__cuenta = None
        
        #aTRIBUTOS PRIBADOS
    def asignarcuenta(self, cuenta):
        self.__cuenta = cuenta
        print(f"{self.nombre} ahora tiene una cuenta")

    def presentarse (self):
        print(f"Hola mi nombre es {self.nombre}, mi apellido es {self.apellido}, y tendo {self.edad} años")
    
    def cumplir_años(self):
        self.edad += 1
        print(f"Esta persona cumplió años y ahora tiene {self.edad} años")

    def consulatarsaldo(self):
        if self.__cuenta:
            print(f"El saldo de {self.nombre} es ${self.__cuenta.mostrarsaldo()}")#saldo
        else:
            print(f"{self.nombre} Aun no tiene una cuenta creada")




class cuenta_Bancaria:
    def __init__(self,numcuenta,saldo):
        self.numcuenta = numcuenta
        self.__saldo = saldo #Atributo privado


    def mostrarsaldo(self):
        return self.__saldo

    def depositar(self, depostio):
        if depostio>0:
            self.__saldo += depostio
            print(f"Se deposito {depostio} exitodamente") 
        else:
            print("Error valores erroneos")

    def retirar(self, sacar):
        if (sacar < self.__saldo and sacar > 0):
            print(f"Se retiro lca cantidad de {sacar} exitosamente")
            print(f"El saldo que le resta es de {self.__saldo}")
        else:
            print("Error saldo insuficiente")   

estudiante1 = persona("Irvin","Solis",19)
estudiante2 = persona("MArtin","Martines",19)
estudiante3 = persona("yuri","yuridia",18)
cuenta1 = cuenta_Bancaria("001", 500)
estudiante1.presentarse()
estudiante1.asignarcuenta(cuenta1)
cuenta1.depositar(300)
estudiante1.consulatarsaldo()


#Ejercicio 1.
#Crear un clase, objeto min 3 atributos y min 3 metodos distintos distintos

class carro:
    def __init__(self,nomcarro,motor,gasolina,tipo):
        self.nomcarro = nomcarro
        self.motor = motor
        self.gasolina = gasolina
        self.tipo = tipo

    def presentarse3(self):
        print(f"I am a car Beep Beep {self.nomcarro} y soy un carro {self.tipo}")
    
    def arrancar(self):
        self.gasolina = self.gasolina - 1
        print(f"Run Run Run Te quedan {self.gasolina}L de gasolina")

carro1 = carro("Corvete","V6 twin turbo",18,"Deportivo")

carro1.presentarse3()
carro1.arrancar()

class trabajo:
    def __init__(self,id, trabajador):
        self.id = id
        self.trabajador =  trabajador

    def trbajo(self):
        self.id = input("Ingrsa tu numero de matricula")
        self.trabajador= input("Ingrsa Tu nombre")

trabajador1 = trabajo()
trabajador1(trabajo.trbajo)
