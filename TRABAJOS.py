class Empleado:
    def __init__(self, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil, correo_electronico):
        self.nombres_apellidos = nombres_apellidos
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.num_movil = num_movil
        self.correo_electronico = correo_electronico

    def calcular_salario(self):
        pass

    def imprimir_datos(self):
        print("Datos del empleado:")
        print(f"Nombres y Apellidos: {self.nombres_apellidos}")
        print(f"# de cédula: {self.cedula}")
        print(f"Nacionalidad: {self.nacionalidad}")



class DesarrolladorSoftware(Empleado):
    def calcular_salario(self):
        sueldo_base = 1500
        bono = 350
        salario_total = sueldo_base + bono
        return salario_total


class AsistenteAdministrativa(Empleado):
    def calcular_salario(self):
        sueldo_base = 900
        bono = 200
        salario_total = sueldo_base + bono
        return salario_total


class Mantenimiento(Empleado):
    def calcular_salario(self):
        sueldo_base = 700
        bono = 100
        salario_total = sueldo_base + bono
        return salario_total


class SoporteTecnico(Empleado):
    def calcular_salario(self):
        sueldo_base = 1100
        bono = 250
        salario_total = sueldo_base + bono
        return salario_total


class Mensajero(Empleado):
    def calcular_salario(self):
        sueldo_base = 750
        bono = 100
        salario_total = sueldo_base + bono
        return salario_total


# Ejemplo de uso
empleado1 = DesarrolladorSoftware(
    input("Nombres y Apellidos: "),
    input("# de cédula: "),
    input("Fecha de nacimiento: "),
    input("Nacionalidad: "),
    input("# de móvil: "),
    input("Correo electrónico: ")
)

empleado2 = AsistenteAdministrativa(
    input("Nombres y Apellidos: "),
    input("# de cédula: "),
    input("Fecha de nacimiento: "),
    input("Nacionalidad: "),
    input("# de móvil: "),
    input("Correo electrónico: ")
)
empleado3 = Mantenimiento(
    input("Nombres y Apellidos: "),
    input("# de cédula: "),
    input("Fecha de nacimiento: "),
    input("Nacionalidad: "),
    input("# de móvil: "),
    input("Correo electrónico: ")
)

empleado4 = SoporteTecnico(
    input("Nombres y Apellidos: "),
    input("# de cédula: "),
    input("Fecha de nacimiento: "),
    input("Nacionalidad: "),
    input("# de móvil: "),
    input("Correo electrónico: ")
)

empleado5 = Mensajero(
    input("Nombres y Apellidos: "),
    input("# de cédula: "),
    input("Fecha de nacimiento: "),
    input("Nacionalidad: "),
    input("# de móvil: "),
    input("Correo electrónico: ")
)
print("**************EMPLEADOS*****************")
empleado1.imprimir_datos()
salario_empleado1 = empleado1.calcular_salario()
print(f"Salario: ${salario_empleado1}")
print("")
empleado2.imprimir_datos()
salario_empleado2 = empleado2.calcular_salario()
print(f"Salario: ${salario_empleado2}")
print("")
empleado3.imprimir_datos()
salario_empleado3 = empleado3.calcular_salario()
print(f"Salario: ${salario_empleado3}")
print("")
empleado4.imprimir_datos()
salario_empleado4 = empleado4.calcular_salario()
print(f"Salario: ${salario_empleado4}")
print("")
empleado5.imprimir_datos()
salario_empleado5 = empleado5.calcular_salario()
print(f"Salario: ${salario_empleado5}")