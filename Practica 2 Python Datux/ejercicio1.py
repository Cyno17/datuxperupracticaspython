# Realice un programa que pueda gestionar tickets de buses
# las clases a usar seran buses  , conductores
# 1. Un menu iteractivo con las siguiente opciones: agregar bus , agregar ruta a bus 
# registrar horario a bus, agregar conductor , agregar horario a conductor(*) y asignar bus a conductor(**)
# * consideremos que el horario de los conductores solo es a nivel de horas mas no dias ni fechas
# **validar que no haya conductores en ese horario ya asignados

class Conductor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.horarios = []  # Horarios asignados al conductor (en horas)

    def agregar_horario(self, hora):
        if hora in self.horarios:
            return False  # Horario ya asignado
        self.horarios.append(hora)
        return True
    pass

class Bus:
    def __init__(self, ruta):
        self.ruta = ruta
        self.conductores_asignados = []  # Lista de conductores
        self.horarios = []  # Horarios del bus (en horas)

    def asignar_conductor(self, conductor, hora):
        if hora in self.horarios:
            for c in self.conductores_asignados:
                if hora in c.horarios:
                    return False  # Horario ya ocupado por otro conductor

        self.horarios.append(hora)
        conductor.agregar_horario(hora)
        self.conductores_asignados.append(conductor)
        return True
    pass

class Admin:
    def __init__(self):
        self.buses = []
        self.conductores = []

    def agregar_bus(self, ruta):
        bus = Bus(ruta)
        self.buses.append(bus)
        return bus

    def agregar_conductor(self, nombre):
        conductor = Conductor(nombre)
        self.conductores.append(conductor)
        return conductor

    def asignar_bus_a_conductor(self, ruta, nombre_conductor, hora):
        bus = next((b for b in self.buses if b.ruta == ruta), None)
        conductor = next((c for c in self.conductores if c.nombre == nombre_conductor), None)

        if not bus or not conductor:
            return False  # Bus o conductor no encontrados

        return bus.asignar_conductor(conductor, hora)

    def mostrar_buses(self):
        for bus in self.buses:
            print(f"Bus Ruta: {bus.ruta}, Horarios: {bus.horarios}")

    def mostrar_conductores(self):
        for conductor in self.conductores:
            print(f"Conductor: {conductor.nombre}, Horarios: {conductor.horarios}")
    pass        

# Programa principal
admin = Admin()

print("\nGestión de Tickets de Buses")

# Paso 1: Agregar Buses
num_buses = int(input("¿Cuántos buses desea agregar?: "))
for _ in range(num_buses):
    ruta = input("Ingrese la ruta del bus: ")
    admin.agregar_bus(ruta)
    print(f"Bus con ruta '{ruta}' agregado con éxito.")

# Paso 2: Agregar Conductores
num_conductores = int(input("\n¿Cuántos conductores desea agregar?: "))
for _ in range(num_conductores):
    nombre = input("Ingrese el nombre del conductor: ")
    admin.agregar_conductor(nombre)
    print(f"Conductor '{nombre}' agregado con éxito.")

# Paso 3: Asignar Conductores a Buses
print("\nAsignación de conductores a buses")
asignaciones = int(input("¿Cuántas asignaciones desea realizar?: "))
for _ in range(asignaciones):
    ruta = input("Ingrese la ruta del bus: ")
    nombre = input("Ingrese el nombre del conductor: ")
    hora = int(input("Ingrese el horario (en horas): "))
    if admin.asignar_bus_a_conductor(ruta, nombre, hora):
        print(f"Conductor '{nombre}' asignado al bus con ruta '{ruta}' en el horario {hora}h.")
    else:
        print("Error al asignar conductor. Verifique los datos o disponibilidad del horario.")

# Paso 4: Mostrar resultados finales
print("\nResumen de Buses:")
admin.mostrar_buses()

print("\nResumen de Conductores:")
admin.mostrar_conductores()

print("\nPrograma finalizado.")
