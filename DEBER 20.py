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
