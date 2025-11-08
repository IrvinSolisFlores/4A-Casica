print("Tienda de Juegos")
productos =["Hell Divers","GTA VI","Pou2 online fps"]
precios = [500, 1600, 20000]

def calcular_total(cantidades, precios):
    total = 0
    for i in range(len(cantidades)):
        total += cantidades[i] + precios[i]
    return total

print("###########Bienvenido a nuestra tienda de juegos#################")
nombre = input("Ingrese su nombre: ")
print(f"Hola {nombre}")
print(f"Los juegos que tenemos disponiblre son :")
a = 1
for i in range(len(productos)):
    a = a + 1
    pre = precios[i]
    print(f"    \n{productos[i]} ${pre}")
cantidades = []

lugar = 0
res = ""
res = input("Ingresa le nombre de lo que deseas comprar? º: ")

if (res == "Hell Divers"):
    lugar = 0
    cantidad = int(input("Cuantas unidades deseas comprar? : "))
    total = cantidad * precios[lugar]
elif (res == "GTA VI"):
    lugar = 1
    cantidad = int(input("Cuantas unidades deseas comprar? : "))
    total = cantidad * precios[lugar]
elif (res == "Pou2 online fps"):
    lugar = 2
    cantidad = int(input("Cuantas unidades deseas comprar? : "))
    total = cantidad * precios[lugar]
else:
    print("No tenemos ese producto")


print("\n\n\n##############Tiket de compra################")
print(f"\nProducto: {res}")
print(f"\nCantidad: {cantidad}")
print(f"\nTotal a pagar: ${total}")
print("\nGracias por su compra, vuelva pronto")