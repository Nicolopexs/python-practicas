class Vehiculo:
    def __init__(self, marca, modelo, año, color, placa, matricula, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.placa = placa
        self.matricula = matricula
        self.tipo = tipo

    def imprimir(self):
        print("Marca:", self.marca)
        print("Modelo:", self.modelo)
        print("Año:", self.año)
        print("Color:", self.color)
        print("Placa:", self.placa)
        print("Matrícula:", self.matricula)
        print("Tipo de vehículo:", self.tipo)

class VehiculoHijo(Vehiculo):  # Clase hija que hereda de Vehiculo
    def __init__(self, marca, modelo, año, color, placa, matricula, tipo):
        super().__init__(marca, modelo, año, color, placa, matricula, tipo)



# Obtener los valores desde el teclado
marca = input("Marca: ")
modelo = input("Modelo: ")
año = int(input("Año: "))
color = input("Color: ")
placa = input("Placa: ")
matricula = input("Matrícula: ")
tipo = input("Tipo de vehículo: ")


vehiculo = VehiculoHijo(marca, modelo, año, color, placa, matricula, tipo)
vehiculo.imprimir()



