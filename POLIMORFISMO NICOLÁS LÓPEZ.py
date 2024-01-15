from abc import ABC, abstractmethod
import math

class Figura(ABC):  # Definición de la clase abstracta Figura.
    @abstractmethod  # Marcador para definir un método abstracto.
    def calcular_area(self):  # Método abstracto para calcular el área de la figura.
        pass  # Se debe implementar en las clases concretas.

class Circulo(Figura):  # Definición de la clase concreta Circulo que extiende la clase Figura.
    def __init__(self, radio):  # Constructor de la clase Circulo.
        self.radio = radio  # Variable para almacenar el radio del círculo.

    def calcular_area(self):  # Implementación del método calcular_area para la clase Circulo.
        return math.pi * self.radio**2  # Calcular y retornar el área del círculo.

class Rectangulo(Figura):  # Definición de la clase concreta Rectangulo que extiende la clase Figura.
    def __init__(self, base, altura):  # Constructor de la clase Rectangulo.
        self.base = base  # Variable para almacenar la base del rectángulo.
        self.altura = altura  # Variable para almacenar la altura del rectángulo.

    def calcular_area(self):  # Implementación del método calcular_area para la clase Rectangulo.
        return self.base * self.altura  # Calcular y retornar el área del rectángulo.

def menu():  # Definición de la función menu para mostrar el menú al usuario.
    print("===== MENÚ =====")
    print("1. Sacar Area del Círculo")
    print("2. Sacar Area del Rectángulo")
    print("3. Salir")
    print("================")

while True:  # Bucle infinito para mantener el programa en ejecución hasta que el usuario decida salir.
    menu()  # Llamar a la función menu para mostrar el menú al usuario.
    opcion = input("Seleccione una opción: ")  # Pedir al usuario que seleccione una opción del menú.

    if opcion == "1":  # Opción para calcular el área del círculo.
        radio = float(input("Ingrese el radio del círculo: "))  # Pedir al usuario que ingrese el radio.
        circulo = Circulo(radio)  # Crear una instancia de Circulo con el radio proporcionado.
        area = circulo.calcular_area()  # Calcular el área del círculo.
        print(f"El área del círculo es: {area}")  # Imprimir el resultado del área del círculo.

    elif opcion == "2":  # Opción para calcular el área del rectángulo.
        base = float(input("Ingrese la base del rectángulo: "))  # Pedir al usuario que ingrese la base.
        altura = float(input("Ingrese la altura del rectángulo: "))  # Pedir al usuario que ingrese la altura.
        rectangulo = Rectangulo(base, altura)  # Crear una instancia de Rectangulo con la base y altura proporcionadas.
        area = rectangulo.calcular_area()  # Calcular el área del rectángulo.
        print(f"El área del rectángulo es: {area}")  # Imprimir el resultado del área del rectángulo.

    elif opcion == "3":  # Opción para salir del programa.
        print("Saliendo del programa...")  # Mensaje de despedida.
        break  # Salir del bucle while y terminar el programa.

    else:  # Opción inválida.
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")



#Programa 2

from abc import ABC, abstractmethod

class Empleado(ABC):  # Definición de la clase abstracta Empleado.
    def __init__(self, nombre, salario_base):  # Constructor de la clase Empleado.
        self.nombre = nombre  # Variable para almacenar el nombre del empleado.
        self.salario_base = salario_base  # Variable para almacenar el salario base del empleado.

    @abstractmethod  # Marcador para definir un método abstracto.
    def calcularSalario(self):  # Método abstracto para calcular el salario del empleado.
        pass  # Se debe implementar en las clases concretas.

    def imprimirDetalles(self):  # Método para imprimir los detalles del empleado.
        print(f"Nombre: {self.nombre}")  # Imprimir el nombre del empleado.
        print(f"Salario Base: {self.salario_base}")  # Imprimir el salario base del empleado.
        print(f"Salario Total: {self.calcularSalario()}")  # Imprimir el salario total del empleado.

class Gerente(Empleado):  # Definición de la clase concreta Gerente que extiende la clase Empleado.
    def __init__(self, nombre, salario_base, bono):  # Constructor de la clase Gerente.
        super().__init__(nombre, salario_base)  # Llamar al constructor de la clase Empleado.
        self.bono = bono  # Variable para almacenar el bono del gerente.

    def calcularSalario(self):  # Implementación del método calcularSalario para la clase Gerente.
        return self.salario_base + self.bono  # Calcular y retornar el salario total del gerente.

class Vendedor(Empleado):  # Definición de la clase concreta Vendedor que extiende la clase Empleado.
    def __init__(self, nombre, salario_base, comisiones):  # Constructor de la clase Vendedor.
        super().__init__(nombre, salario_base)  # Llamar al constructor de la clase Empleado.
        self.comisiones = comisiones  # Variable para almacenar las comisiones del vendedor.

    def calcularSalario(self):  # Implementación del método calcularSalario para la clase Vendedor.
        return self.salario_base + self.comisiones  # Calcular y retornar el salario total del vendedor.

if __name__ == "__main__":  # Bloque principal del programa.
    gerente1 = Gerente("David", 5000, 2000)  # Crear una instancia de Gerente con nombre, salario base y bono.
    vendedor1 = Vendedor("José", 3000, 1000)  # Crear una instancia de Vendedor con nombre, salario base y comisiones.

    empleados = [gerente1, vendedor1]  # Crear una lista con objetos de las clases Gerente y Vendedor.

    for empleado in empleados:  # Iterar sobre la lista de empleados.
        empleado.imprimirDetalles()  # Llamar al método imprimirDetalles de cada empleado.
        print("--------------------")  # Imprimir un separador para diferenciar los resultados.


#PROGRAMA 3
from abc import ABC, abstractmethod

from abc import ABC, abstractmethod

class Animal(ABC):  # Definición de la clase abstracta Animal.
    @abstractmethod  # Marcador para definir un método abstracto.
    def comer(self):  # Método abstracto para que todas las clases derivadas lo implementen.
        pass  # Se debe implementar en las clases concretas.

    @abstractmethod  # Otro método abstracto.
    def hacerSonido(self):  # Otro método abstracto para que todas las clases derivadas lo implementen.
        pass  # Se debe implementar en las clases concretas.

class Perro(Animal):  # Definición de la clase concreta Perro que extiende la clase abstracta Animal.
    def comer(self):  # Implementación del método comer para la clase Perro.
        print("El perro está comiendo croquetas.")

    def hacerSonido(self):  # Implementación del método hacerSonido para la clase Perro.
        print("El perro hace: ¡Guau, guau!")

class Gato(Animal):  # Definición de la clase concreta Gato que extiende la clase abstracta Animal.
    def comer(self):  # Implementación del método comer para la clase Gato.
        print("El gato está comiendo whiskas")

    def hacerSonido(self):  # Implementación del método hacerSonido para la clase Gato.
        print("El gato hace: ¡Miau, miau!")

if __name__ == "__main__":  # Bloque principal del programa.
    animales = [Perro(), Gato()]  # Creamos una lista con objetos de las clases Perro y Gato.

    for animal in animales:  # Iteramos sobre la lista de animales.
        animal.comer()  # Llamamos al método comer de cada animal.
        animal.hacerSonido()  # Llamamos al método hacerSonido de cada animal.
        print("--------------------")  # Imprimimos un separador para diferenciar los resultados.


