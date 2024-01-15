class Vehículo:
    def __init__(self, marca, modelo, año, color, placa, matricula, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.placa = placa
        self.matricula = matricula
        self.tipo = tipo

    def imprimir_datos(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Color:", self.color)
        print("Placa:", self.placa)
        print("Matrícula:", self.matricula)
        print("Tipo de vehículo:", self.tipo)


class Automóvil(Vehículo):
    def __init__(self, marca, modelo, año, color, placa, matricula, tipo):
        super().__init__(marca, modelo, año, color, placa, matricula, tipo)
        

    def imprimir_datos(self):
        super().imprimir_datos()
        


marca = input("Ingrese la marca del automóvil: ")
modelo = input("Ingrese el modelo del automóvil: ")
año = input("Ingrese el año del automóvil: ")
color = input("Ingrese el color del automóvil: ")
placa = input("Ingrese el número de placa del automóvil: ")
matricula = input("Ingrese el número de matrícula del automóvil: ")
tipo = input("Ingrese el tipo de vehículo: ")

automovil = Automóvil(marca, modelo, año, color, placa, matricula, tipo)
automovil.imprimir_datos()


class Empleado:
    def __init__(self):
        self.nombres_apellidos = input("Ingrese nombres y apellidos del empleado: ")
        self.numero_cedula = input("Ingrese el número de cédula del empleado: ")
        self.fecha_nacimiento = input("Ingrese la fecha de nacimiento del empleado: ")
        self.nacionalidad = input("Ingrese la nacionalidad del empleado: ")
        self.numero_movil = input("Ingrese el número de móvil del empleado: ")
        self.correo_electronico = input("Ingrese el correo electrónico del empleado: ")

    def calcular_salario(self):
        pass

    def imprimir_datos(self):
        print("Nombres y Apellidos:", self.nombres_apellidos)
        print("Número de cédula:", self.numero_cedula)
        print("Fecha de nacimiento:", self.fecha_nacimiento)
        print("Nacionalidad:", self.nacionalidad)
        print("Número de móvil:", self.numero_movil)
        print("Correo electrónico:", self.correo_electronico)


class DesarrolladorSoftware(Empleado):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        sueldo_base = 1500
        bono = 350
        salario = sueldo_base + bono
        return salario


class AsistenteAdministrativa(Empleado):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        sueldo_base = 900
        bono = 200
        salario = sueldo_base + bono
        return salario


class Mantenimiento(Empleado):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        sueldo_base = 700
        bono = 100
        salario = sueldo_base + bono
        return salario


class SoporteTecnico(Empleado):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        sueldo_base = 1100
        bono = 250
        salario = sueldo_base + bono
        return salario


class Mensajero(Empleado):
    def __init__(self):
        super().__init__()

    def calcular_salario(self):
        sueldo_base = 750
        bono = 100
        salario = sueldo_base + bono
        return salario


# Crear objeto de un empleado
desarrollador = DesarrolladorSoftware()

# Calcular salario del empleado
salario = desarrollador.calcular_salario()

# Imprimir datos y salario del empleado
desarrollador.imprimir_datos()
print("Salario:", salario)


class Electrodoméstico:
    def __init__(self, nombre):
        self.nombre = nombre
        self.estado = "apagado"

    def encender(self):
        self.estado = "encendido"

    def apagar(self):
        self.estado = "apagado"

    def imprimir_estado(self):
        print(self.nombre, "está", self.estado)


class SmartTV(Electrodoméstico):
    def __init__(self):
        super().__init__("Smart TV")


class Refrigeradora(Electrodoméstico):
    def __init__(self):
        super().__init__("Refrigeradora")


class Lavadora(Electrodoméstico):
    def __init__(self):
        super().__init__("Lavadora")


class EquipoSonido(Electrodoméstico):
    def __init__(self):
        super().__init__("Equipo de sonido")


class Microondas(Electrodoméstico):
    def __init__(self):
        super().__init__("Microondas")


# Crear objetos de los electrodomésticos
smart_tv = SmartTV()
refrigeradora = Refrigeradora()
lavadora = Lavadora()
equipo_sonido = EquipoSonido()
microondas = Microondas()

# Encender algunos electrodomésticos
smart_tv.encender()
lavadora.encender()

# Imprimir el estado de los electrodomésticos
smart_tv.imprimir_estado()
refrigeradora.imprimir_estado()
lavadora.imprimir_estado()
equipo_sonido.imprimir_estado()
microondas.imprimir_estado()
