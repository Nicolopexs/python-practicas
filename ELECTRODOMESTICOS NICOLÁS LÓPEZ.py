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
