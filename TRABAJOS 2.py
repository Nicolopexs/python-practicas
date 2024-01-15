class Empleado:
    def __init__(self, cargo, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil, correo_electronico):
        self.cargo = cargo
        self.nombres_apellidos = nombres_apellidos
        self.cedula = cedula
        self.fecha_nacimiento = fecha_nacimiento
        self.nacionalidad = nacionalidad
        self.num_movil = num_movil
        self.correo_electronico = correo_electronico
        

    def calcular_salario(self):
        pass
        
    def imprimir_datos(self):
        print("*********Datos del empleado:*********")
        print(f"Cargo: {self.cargo}")
        print(f"Nombres y Apellidos: {self.nombres_apellidos}")
        print(f"# de cédula: {self.cedula}")
        print(f"Nacionalidad: {self.nacionalidad}")
        print(f"Correo electronico: {self.correo_electronico}")


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


cargo = input("Trabajo Asignado: ")

if cargo.lower() == "desarrollo de software":
    nombres_apellidos = input("Nombres y Apellidos: ")
    cedula = input("# de cédula: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nacionalidad = input("Nacionalidad: ")
    num_movil = input("# de móvil: ")
    correo_electronico = input("Correo electrónico: ")

    empleado = DesarrolladorSoftware(cargo, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil,correo_electronico)
    print("")
    empleado.imprimir_datos()
    salario = empleado.calcular_salario()
    print(f"Salario: ${salario}")

elif cargo.lower() == "asistente Administrativa":
    nombres_apellidos = input("Nombres y Apellidos: ")
    cedula = input("# de cédula: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nacionalidad = input("Nacionalidad: ")
    num_movil = input("# de móvil: ")
    correo_electronico = input("Correo electrónico: ")

    empleado = AsistenteAdministrativa(cargo, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil, correo_electronico)
    print("")
    empleado.imprimir_datos()
    salario = empleado.calcular_salario()
    print(f"Salario: ${salario}")

elif cargo.lower() == "soporte Tecnico":
    nombres_apellidos = input("Nombres y Apellidos: ")
    cedula = input("# de cédula: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nacionalidad = input("Nacionalidad: ")
    num_movil = input("# de móvil: ")
    correo_electronico = input("Correo electrónico: ")

    empleado = SoporteTecnico(cargo, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil, correo_electronico)
    print("")
    empleado.imprimir_datos()
    salario = empleado.calcular_salario()
    print(f"Salario: ${salario}")

elif cargo.lower() == "mantenimiento":
    nombres_apellidos = input("Nombres y Apellidos: ")
    cedula = input("# de cédula: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nacionalidad = input("Nacionalidad: ")
    num_movil = input("# de móvil: ")
    correo_electronico = input("Correo electrónico: ")

    empleado = Mantenimiento(cargo, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil, correo_electronico)
    print("")
    empleado.imprimir_datos()
    salario = empleado.calcular_salario()
    print(f"Salario: ${salario}")

elif cargo.lower() == "mensajero":
    nombres_apellidos = input("Nombres y Apellidos: ")
    cedula = input("# de cédula: ")
    fecha_nacimiento = input("Fecha de nacimiento: ")
    nacionalidad = input("Nacionalidad: ")
    num_movil = input("# de móvil: ")
    correo_electronico = input("Correo electrónico: ")

    empleado = Mensajero(cargo, nombres_apellidos, cedula, fecha_nacimiento, nacionalidad, num_movil, correo_electronico)
    print("")
    empleado.imprimir_datos()
    salario = empleado.calcular_salario()
    print(f"Salario: ${salario}")
    
else:
    print("Cargo no válido")
    exit()

