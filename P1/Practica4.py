class Ticket:
    def __init__(self, id, tipo, prioridad):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "Pendiente"

class empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def trabajar_en_ticket(self, Ticket):
        print(f"El empleado {self.nombre} revisa el ticket {Ticket.id}")

class desarollador(empleado):
    def trabajar_en_ticket(self, Ticket):
        if Ticket.tipo == "software":
            Ticket.estado = "Resuelto"
            print(f"El desarrollador {self.nombre} ha resuelto el ticket {Ticket.id}")
        else:
            print(f"El desarrollador {self.nombre} no puede trabajar en el ticket {Ticket.id} de tipo {Ticket.tipo}") 

class tester(empleado):
    def trabajar_en_ticket(self, Ticket):
        if Ticket.tipo == "prueba":
            Ticket.estado = "Resuelto"
            print(f"El tester {self.nombre} ha resuelto el ticket {Ticket.id}")
        else:
            print(f"El tester {self.nombre} no puede trabajar en el ticket {Ticket.id} de tipo {Ticket.tipo}") 

class projectmanager(empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)

# Crear tickets y empleados
#ticket1 = Ticket(1, "software", "alta")
#ticket2 = Ticket(2, "prueba", "media")

developer1 = desarollador("Carlitos")
tester1 = tester("Juanillo")

pm = projectmanager("Juanote")

#pm.asignar_ticket(ticket2, tester1)

#Agregar un menu interactivo con while y con if para:
#1. Crear tickets
#2. ver los tickets
#3. Asignar un ticket
#4. guardar tickets en un archivo txt
#5. ver empleados
#6. Salir
class Ticket:
    def __init__(self, id, tipo, prioridad):
        self.id = id
        self.tipo = tipo
        self.prioridad = prioridad
        self.estado = "Pendiente"

class empleado:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def trabajar_en_ticket(self, Ticket):
        print(f"El empleado {self.nombre} revisa el ticket {Ticket.id}")

class desarollador(empleado):
    def trabajar_en_ticket(self, Ticket):
        if Ticket.tipo.lower() == "software":
            Ticket.estado = "Resuelto"
            print(f"El desarrollador {self.nombre} ha resuelto el ticket {Ticket.id}")
        else:
            print(f"El desarrollador {self.nombre} no puede trabajar en el ticket {Ticket.id} de tipo {Ticket.tipo}") 

class tester(empleado):
    def trabajar_en_ticket(self, Ticket):
        if Ticket.tipo.lower() == "prueba":
            Ticket.estado = "Resuelto"
            print(f"El tester {self.nombre} ha resuelto el ticket {Ticket.id}")
        else:
            print(f"El tester {self.nombre} no puede trabajar en el ticket {Ticket.id} de tipo {Ticket.tipo}") 

class projectmanager(empleado):
    def asignar_ticket(self, ticket, empleado):
        print(f"{self.nombre} asignó el ticket {ticket.id} al empleado {empleado.nombre}")
        empleado.trabajar_en_ticket(ticket)

# Crear empleados
developer1 = desarollador("Carlitos")
tester1 = tester("Juanillo")
pm = projectmanager("Juanote")

tickets = []
empleados = [developer1, tester1, pm]

bandera = True
while bandera:
    print("\n--- Menú ---")
    print("1. Crear ticket")
    print("2. Ver tickets")
    print("3. Asignar ticket")
    print("4. Guardar tickets en archivo")
    print("5. Ver empleados")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")

    
    if opcion == "1":
        id = int(input("Ingrese el ID del ticket: "))
        tipo = input("Ingrese el tipo de ticket (software/prueba): ").lower()
        prioridad = input("Ingrese la prioridad del ticket (alta/media/baja): ").lower()
        nuevo_ticket = Ticket(id, tipo, prioridad)
        tickets.append(nuevo_ticket)
        print(f"Ticket {nuevo_ticket.id} creado.")
        input("Presione Enter para continuar...")


    elif opcion == "2":
        print("Lista de tickets:")
        if not tickets:
            print("No hay tickets registrados.")
        else:
            for t in tickets:
                print(f"ID: {t.id}, Tipo: {t.tipo}, Prioridad: {t.prioridad}, Estado: {t.estado}")
        input("Presione Enter para continuar...")

    
    elif opcion == "3":
        if not tickets:
            print("No hay tickets disponibles para asignar.")
            input("Presione Enter para continuar...")
        else:
            print("Tickets disponibles:")
            for t in tickets:
                if t.estado.lower() == "pendiente":
                    print(f"ID: {t.id}, Tipo: {t.tipo}, Prioridad: {t.prioridad}, Estado: {t.estado}")

            print("Empleados disponibles:")
            for e in empleados:
                print(f"Nombre: {e.nombre}")

            ticket_id = int(input("Ingrese el ID del ticket a asignar: "))
            empleado_nombre = input("Ingrese el nombre del empleado al que se asignará el ticket: ").lower()

            
            ticket_encontrado = None
            for t in tickets:
                if t.id == ticket_id:
                    ticket_encontrado = t
                    break

            empleado_encontrado = None
            for e in empleados:
                if e.nombre.lower() == empleado_nombre:
                    empleado_encontrado = e
                    break

            if ticket_encontrado and empleado_encontrado:
                pm.asignar_ticket(ticket_encontrado, empleado_encontrado)
            else:
                print("Error: Ticket o empleado no encontrado.")
            input("Presione Enter para continuar...")

    
    elif opcion == "4":
        if not tickets:
            print("No hay tickets para guardar.")
        else:
            with open("tickets.txt", "w") as archivo:
                for t in tickets:
                    archivo.write(f"ID: {t.id}, Tipo: {t.tipo}, Prioridad: {t.prioridad}, Estado: {t.estado}\n")
            print("Tickets guardados en 'tickets.txt'")
        input("Presione Enter para continuar...")

    
    elif opcion == "5":
        print("Lista de empleados:")
        for e in empleados:
            print(f"Nombre: {e.nombre}, Rol: {e.__class__.__name__}")
        input("Presione Enter para continuar...")

    
    elif opcion == "6":
        pregunta = input("¿Está seguro que desea salir? (s/n): ").lower()
        if pregunta == "s":
            print("Saliendo del programa...")
            bandera = False
    else:
        print("Opción no válida.")
        input("Presione Enter para continuar...")
