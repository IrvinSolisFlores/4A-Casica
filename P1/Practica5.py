#Practica 5. siglenton
#Ejemolu de patron de disño
#Singelton - sistema de registro de logs

class logger:
    #Atributo de clase para guardar una instancia
    __instance = None
    #El metodo __new__ controla la creacion del objeto antes de init asegura que solo exista una sola instancia
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance.archivo = open("app.log","a")
        return cls.__instance #Devuelve siempre ala misma Instancia
    def registro(self, mensaje):
        self.archivo.write(mensaje)
        self.archivo.flush()#Forza al archivo para guardarse en el disco
        

registro1=logger()#Creamos la unica instancia
registro2=logger()#Devuelve la misma instancia sin crear una nueva

registro1.registro("Inicio de sesion en la aplicacion")
registro2.registro("El usuario se autoentifico")

print(registro1,registro2)
