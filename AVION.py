from abc import ABC, abstractmethod


class Motor(ABC):

    @abstractmethod
    def encender(self):
        pass

    @abstractmethod
    def apagar(self):
        pass

# Clase abstracta para las Alas
class Alas(ABC):

    @abstractmethod
    def despegar(self):
        pass

    @abstractmethod
    def aterrizar(self):
        pass

# Clase abstracta para el Tren de Aterrizaje
class TrenAterrizaje(ABC):

    @abstractmethod
    def extender(self):
        pass

    @abstractmethod
    def retraer(self):
        pass

# Clase para el Avión que hereda de las clases abstractas
class Avion(Motor, Alas, TrenAterrizaje):

    def __init__(self):
        self.motor_encendido = False
        self.alas_desplegadas = False
        self.tren_aterrizaje_extendido = False

    def encender(self):
        self.motor_encendido = True
        print("Motor encendido")

    def apagar(self):
        self.motor_encendido = False
        print("Motor apagado")

    def despegar(self):
        if self.motor_encendido and not self.alas_desplegadas and not self.tren_aterrizaje_extendido:
            self.alas_desplegadas = True
            print("Despegando...")
        else:
            print("No se puede despegar. Verifica el motor, las alas y el tren de aterrizaje.")

    def aterrizar(self):
        if self.motor_encendido and self.alas_desplegadas and self.tren_aterrizaje_extendido:
            self.alas_desplegadas = False
            self.tren_aterrizaje_extendido = False
            print("Aterrizando...")
        else:
            print("No se puede aterrizar. Verifica el motor, las alas y el tren de aterrizaje.")

    def extender(self):
        self.tren_aterrizaje_extendido = True
        print("Tren de aterrizaje extendido")

    def retraer(self):
        self.tren_aterrizaje_extendido = False
        print("Tren de aterrizaje retraído")

# Función para probar el simulador de vuelo

avion = Avion()
avion.encender()
avion.despegar()
avion.extender()
avion.despegar()
avion.aterrizar()
avion.retraer()
avion.aterrizar()
avion.apagar()
