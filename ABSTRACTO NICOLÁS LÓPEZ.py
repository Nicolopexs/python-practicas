from abc import ABC, abstractmethod
# Clase abstracta Gestor que define los métodos básicos de manejo de tareas
class Gestor(ABC): # Define la clase Gestor como una clase abstracta
    def __init__(self, archivo, descripcion): # Constructor de la clase Gestor
        self.archivo = archivo # Inicializa el atributo archivo
        self.descripcion = descripcion # Inicializa el atributo descripcion

    @abstractmethod # Marca el método como abstracto, obligando a las clases hijas a implementarlo
    def getCrear_tarea(self): # Método abstracto para crear una tarea
        pass

    @abstractmethod # Marca el método como abstracto, obligando a las clases hijas a implementarlo
    def editar_tarea(self, nueva_descripcion): # Método abstracto para editar una tarea
        pass

    @abstractmethod # Marca el método como abstracto, obligando a las clases hijas a implementarlo
    def eliminar_tarea(self): # Método abstracto para eliminar una tarea
        pass

    def subir_tarea(self): # Método concreto para subir una tarea
        if self.archivo: # Verifica si hay un archivo (si no es None)
            print("La tarea se ha subido correctamente")
        else:
            print("No se ha podido subir la tarea")

# Clase Tarea que hereda de Gestor y define la implementación concreta de los métodos
class Tarea(Gestor): # Define la clase Tarea que hereda de Gestor
    def __init__(self, archivo, descripcion): # Constructor de la clase Tarea
        super().__init__(archivo, descripcion) # Llama al constructor de la clase padre

    def getCrear_tarea(self): # Implementación concreta del método para crear una tarea
        # Código para crear la tarea
        print(f"El archivo {self.archivo} se ha creado \nDescripción: {self.descripcion}")

    def editar_tarea(self, nueva_descripcion): # Implementación concreta del método para editar una tarea
        # Editar la descripción de la tarea
        self.descripcion = nueva_descripcion
        print(f"Se ha editado la tarea {self.archivo}")
        print(f"Nuevo titulo: {self.archivo}")
        print(f"Nueva descripción: {self.descripcion}")

    def eliminar_tarea(self): # Implementación concreta del método para eliminar una tarea
        # Código para eliminar la tarea
        print(f"Se ha eliminado la tarea {self.archivo}")

def mostrar_menu(): # Función para mostrar el menú
    print("===== MENÚ =====")
    print("1. Crear tarea")
    print("2. Editar tarea")
    print("3. Eliminar tarea")
    print("4. Subir tarea")
    print("5. Salir")
    print("================")

# Ejemplo de uso del Gestor de tareas con menú
tarea = None  # Variable para almacenar la tarea actual

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        archivo = input("Ingrese el nombre del archivo: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        tarea = Tarea(archivo, descripcion)
        tarea.getCrear_tarea()

    elif opcion == "2":
        if tarea:
            nueva_descripcion = input("Ingrese la nueva descripción de la tarea: ")
            tarea.editar_tarea(nueva_descripcion)
        else:
            print("No hay tarea creada. Por favor, cree una tarea primero.")
    elif opcion == "3":
        if tarea:
            tarea.eliminar_tarea()
            tarea = None  # Reiniciar la variable de la tarea
        else:
            print("No hay tarea creada. Por favor, cree una tarea primero.")
    elif opcion == "4":
        if tarea:
            tarea.subir_tarea()
        else:
            print("No hay tarea creada. Por favor, cree una tarea primero.")
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida del menú.")



#Simulador de vuelo

from abc import ABC, abstractmethod

class Motor(ABC):  # Define la clase abstracta Motor
    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def encender(self):  # Método abstracto para encender el motor
        pass

    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def apagar(self):  # Método abstracto para apagar el motor
        pass

# Clase abstracta para las Alas
class Alas(ABC):  # Define la clase abstracta Alas
    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def despegar(self):  # Método abstracto para despegar las alas
        pass

    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def aterrizar(self):  # Método abstracto para aterrizar las alas
        pass

# Clase abstracta para el Tren de Aterrizaje
class TrenAterrizaje(ABC):  # Define la clase abstracta TrenAterrizaje
    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def extender(self):  # Método abstracto para extender el tren de aterrizaje
        pass

    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def retraer(self):  # Método abstracto para retraer el tren de aterrizaje
        pass

# Clase para el Avión que hereda de las clases abstractas
class Avion(Motor, Alas, TrenAterrizaje):  # Define la clase Avion que hereda de las clases abstractas Motor, Alas y TrenAterrizaje
    def __init__(self):  # Constructor de la clase Avion
        self.motor_encendido = False  # Inicializa el atributo motor_encendido a False
        self.alas_desplegadas = False  # Inicializa el atributo alas_desplegadas a False
        self.tren_aterrizaje_extendido = False  # Inicializa el atributo tren_aterrizaje_extendido a False

    def encender(self):  # Implementación del método encender de la clase Motor
        self.motor_encendido = True  # Cambia el atributo motor_encendido a True
        print("Motor encendido")  # Imprime un mensaje indicando que el motor ha sido encendido

    def apagar(self):  # Implementación del método apagar de la clase Motor
        self.motor_encendido = False  # Cambia el atributo motor_encendido a False
        print("Motor apagado")  # Imprime un mensaje indicando que el motor ha sido apagado

    def despegar(self):  # Implementación del método despegar de la clase Alas
        if self.motor_encendido and not self.alas_desplegadas and not self.tren_aterrizaje_extendido:
            self.alas_desplegadas = True  # Cambia el atributo alas_desplegadas a True
            print("Despegando...")  # Imprime un mensaje indicando que el avión está despegando
        else:
            print("No se puede despegar. Verifica el motor, las alas y el tren de aterrizaje.")  # Imprime un mensaje de error si no se puede despegar

    def aterrizar(self):  # Implementación del método aterrizar de la clase Alas
        if self.motor_encendido and self.alas_desplegadas and self.tren_aterrizaje_extendido:
            self.alas_desplegadas = False  # Cambia el atributo alas_desplegadas a False
            self.tren_aterrizaje_extendido = False  # Cambia el atributo tren_aterrizaje_extendido a False
            print("Aterrizando...")  # Imprime un mensaje indicando que el avión está aterrizando
        else:
            print("No se puede aterrizar. Verifica el motor, las alas y el tren de aterrizaje.")  # Imprime un mensaje de error si no se puede aterrizar

    def extender(self):  # Implementación del método extender de la clase TrenAterrizaje
        self.tren_aterrizaje_extendido = True  # Cambia el atributo tren_aterrizaje_extendido a True
        print("Tren de aterrizaje extendido")  # Imprime un mensaje indicando que el tren de aterrizaje ha sido extendido

    def retraer(self):  # Implementación del método retraer de la clase TrenAterrizaje
        self.tren_aterrizaje_extendido = False  # Cambia el atributo tren_aterrizaje_extendido a False
        print("Tren de aterrizaje retraído")  # Imprime un mensaje indicando que el tren de aterrizaje ha sido retraído

# Función para probar el simulador de vuelo

avion = Avion()  # Crea un objeto de la clase Avion
avion.encender()  # Enciende el motor del avión
avion.despegar()  # Despega el avión
avion.extender()  # Extiende el tren de aterrizaje
avion.despegar()  # Intenta despegar nuevamente
avion.aterrizar()  # Aterriza el avión
avion.retraer()  # Retrae el tren de aterrizaje
avion.aterrizar()  # Intenta aterrizar nuevamente
avion.apagar()  # Apaga el motor del avión


#PROGRAMA 3

from abc import ABC, abstractmethod

class Producto(ABC):  # Define la clase abstracta Producto
    def __init__(self, nombre, precio, cantidad):  # Constructor de la clase Producto
        self.nombre = nombre  # Inicializa el atributo nombre
        self.precio = precio  # Inicializa el atributo precio
        self.cantidad = cantidad  # Inicializa el atributo cantidad

    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def mostrar_informacion(self):  # Método abstracto para mostrar la información del producto
        pass

    @abstractmethod  # Marca el método como abstracto, debe ser implementado en las clases hijas
    def calcular_total(self):  # Método abstracto para calcular el total del producto
        pass

# Clase para representar productos alimenticios
class Alimento(Producto):  # Define la clase Alimento que hereda de la clase Producto
    def __init__(self, nombre, precio, cantidad, fecha_vencimiento):  # Constructor de la clase Alimento
        super().__init__(nombre, precio, cantidad)  # Llama al constructor de la clase padre
        self.fecha_vencimiento = fecha_vencimiento  # Inicializa el atributo fecha_vencimiento

    def mostrar_informacion(self):  # Implementación del método mostrar_informacion de la clase Alimento
        print(f"Producto: {self.nombre}")  # Imprime el nombre del producto
        print(f"Precio: {self.precio}$")  # Imprime el precio del producto
        print(f"Cantidad: {self.cantidad}")  # Imprime la cantidad del producto
        print(f"Fecha de Vencimiento: {self.fecha_vencimiento}")  # Imprime la fecha de vencimiento del producto

    def calcular_total(self):  # Implementación del método calcular_total de la clase Alimento
        return self.precio * self.cantidad  # Calcula el total del producto multiplicando el precio por la cantidad

# Clase para representar productos electrónicos
class Electronico(Producto):  # Define la clase Electronico que hereda de la clase Producto
    def __init__(self, nombre, precio, cantidad, garantia_meses):  # Constructor de la clase Electronico
        super().__init__(nombre, precio, cantidad)  # Llama al constructor de la clase padre
        self.garantia_meses = garantia_meses  # Inicializa el atributo garantia_meses

    def mostrar_informacion(self):  # Implementación del método mostrar_informacion de la clase Electronico
        print(f"Producto: {self.nombre}")  # Imprime el nombre del producto
        print(f"Precio: {self.precio}$")  # Imprime el precio del producto
        print(f"Cantidad: {self.cantidad}")  # Imprime la cantidad del producto
        print(f"Garantía: {self.garantia_meses} meses")  # Imprime la garantía del producto en meses

    def calcular_total(self):  # Implementación del método calcular_total de la clase Electronico
        return self.precio * self.cantidad  # Calcula el total del producto multiplicando el precio por la cantidad

# Clase para representar productos de ropa
class Ropa(Producto):  # Define la clase Ropa que hereda de la clase Producto
    def __init__(self, nombre, precio, cantidad, talla):  # Constructor de la clase Ropa
        super().__init__(nombre, precio, cantidad)  # Llama al constructor de la clase padre
        self.talla = talla  # Inicializa el atributo talla

    def mostrar_informacion(self):  # Implementación del método mostrar_informacion de la clase Ropa
        print(f"Producto: {self.nombre}")  # Imprime el nombre del producto
        print(f"Precio: {self.precio}$")  # Imprime el precio del producto
        print(f"Cantidad: {self.cantidad}")  # Imprime la cantidad del producto
        print(f"Talla: {self.talla}")  # Imprime la talla del producto

    def calcular_total(self):  # Implementación del método calcular_total de la clase Ropa
        return self.precio * self.cantidad  # Calcula el total del producto multiplicando el precio por la cantidad

# Función para probar el sistema de gestión de inventario
def main():
    # Creamos algunos productos
    cafe = Alimento("Café", 2.5, 50, "31/12/2023")  # Crea un objeto de la clase Alimento
    celular = Electronico("Celular", 600, 8, 18)  # Crea un objeto de la clase Electronico
    pantalon = Ropa("Pantalón", 30, 15, "L")  # Crea un objeto de la clase Ropa

    # Mostramos información y calculamos el total para cada producto
    print("Producto 1:")  # Imprime el título del primer producto
    cafe.mostrar_informacion()  # Muestra la información del primer producto (Alimento)
    print("Total:", cafe.calcular_total())  # Calcula y muestra el total del primer producto (Alimento)
    print()

    print("Producto 2:")  # Imprime el título del segundo producto
    celular.mostrar_informacion()  # Muestra la información del segundo producto (Electronico)
    print("Total:", celular.calcular_total())  # Calcula y muestra el total del segundo producto (Electronico)
    print()

    print("Producto 3:")  # Imprime el título del tercer producto
    pantalon.mostrar_informacion()  # Muestra la información del tercer producto (Ropa)
    print("Total:", pantalon.calcular_total())  # Calcula y muestra el total del tercer producto (Ropa)

if __name__ == "__main__":
    main()  # Llama a la función principal para probar el sistema de gestión de inventario






