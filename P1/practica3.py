# Practica 3, Introduccion al polimorfismo
# simular un sistema de cobro de al menos 
# 4 tipos

class pago_targeta:
    def procesar_pago(self,cantidad):
        cantidad1 = cantidad
        return f"Procesando pago de $ {cantidad} con targeta de debito/credito "

class paypal:
    def procesar_pago(self,cantidad):
        nom = input("ingresa tu nombre :")
        return f"Procesando tu pago {nom} de $ {cantidad} con paypal"
    
class efectivo:
    def procesar_pago(self,cantidad):

        return f"Procesando pago de $ {cantidad} en efectivo"
    
class transferencia:
    def procesar_pago(self,cantidad):
        cantidad += 20
        return f"Procesando pago de $ {cantidad} con transferencia"

metodos_pago = [pago_targeta, paypal, efectivo, transferencia]

for i in metodos_pago:
    print(i.procesar_pago(500,500))


# Actividad 1 
#Procesar diferentes cantidades en cada opcion de pago 100 con targeta 400 con paypal en efectivo 600 y con transferencia 5000

pago1 =pago_targeta()
pago2 = paypal()
pago3 = efectivo()
pago4 = transferencia()

print(pago1.procesar_pago(100))
print(pago2.procesar_pago(400))
print(pago3.procesar_pago(600))
print(pago4.procesar_pago(5000))


# Actividad2 agregar funcionalidad adiconal al metodo procesar_pago( cuando sea deposito: sumar 20 (comision)a cantidad 
#cuando sea paypal pedirle al usuario su nombre