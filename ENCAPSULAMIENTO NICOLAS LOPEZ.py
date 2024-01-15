
class CuentaBancaria:  # Clase que representa una cuenta bancaria
    def __init__(self, nombre_titular, numero_cuenta, monto):  # Constructor de la clase
        self.__saldo = 0  # Atributo privado para el saldo de la cuenta
        self.__nombre_titular = nombre_titular  # Atributo privado para el nombre del titular
        self.__numero_cuenta = numero_cuenta  # Atributo privado para el número de cuenta
        self.monto = monto  # Atributo adicional (no utilizado en el código proporcionado)
    
    @property  # Decorador para el método getter del saldo
    def saldo(self):  # Método getter para el saldo de la cuenta
        return self.__saldo
    
    @saldo.setter  # Decorador para el método setter del saldo
    def saldo(self, valor):  # Método setter para el saldo de la cuenta
        self.__saldo = valor  # Actualiza el saldo de la cuenta
        
    @property  # Decorador para el método getter del nombre del titular
    def nombre_titular(self):  # Método getter para el nombre del titular de la cuenta
        return self.__nombre_titular
    
    @nombre_titular.setter  # Decorador para el método setter del nombre del titular
    def nombre_titular(self, nombre_titular):  # Método setter para el nombre del titular de la cuenta
        self.__nombre_titular = nombre_titular
    
    @property  # Decorador para el método getter del número de cuenta
    def numero_cuenta(self):  # Método getter para el número de cuenta
        return self.__numero_cuenta
    
    @numero_cuenta.setter  # Decorador para el método setter del número de cuenta
    def numero_cuenta(self, numero_cuenta):  # Método setter para el número de cuenta
        self.__numero_cuenta = numero_cuenta

    def depositar(self, monto):  # Método para realizar un depósito en la cuenta
        if monto > 0:  # Verifica que el monto sea mayor que cero
            self.__saldo += monto  # Incrementa el saldo de la cuenta
            print(f"Se depositaron {monto} unidades en la cuenta.")
        else:
            print("El monto debe ser mayor que cero.")

    def retirar(self, monto):  # Método para realizar un retiro de la cuenta
        if 0 < monto <= self.__saldo:  # Verifica que el monto sea mayor que cero y no supere el saldo actual
            self.__saldo -= monto  # Reduce el saldo de la cuenta
            print(f"Se retiraron {monto} unidades de la cuenta.")
        else:
            print("No se pudo realizar la operación de retiro.")

nombre, cuenta, monto = None, None, None  # Variables para almacenar los valores de nombre, cuenta y monto

while True:  # Bucle principal del programa
    print("\nBienvenido al Banco:")  # Muestra un mensaje de bienvenida
    opciones = int(input("¿Qué operación desea realizar?\n1. Abrir una cuenta\n2. Depositar en la cuenta\n3. Retirar dinero\n4. Verificar saldo de la cuenta\nIngrese un número: "))  # Solicita al usuario una opción
    
    if opciones == 1:  # Opción para abrir una cuenta
        print("\n-----NUEVA CUENTA-----")  # Muestra un mensaje para abrir una nueva cuenta
        nombre = input("Ingrese su nombre: ")  # Solicita al usuario que ingrese su nombre
        cuenta = input("Ingrese su número de cuenta: ")  # Solicita al usuario que ingrese su número de cuenta
        p = CuentaBancaria(nombre, cuenta, "")  # Crea una nueva instancia de la clase CuentaBancaria
        p.setnombre_titular = nombre
        p.setnumero_cuenta = cuenta
        
        continue
    
    elif opciones == 2:  # Opción para realizar un depósito
        if nombre is None or cuenta is None:  # Verifica que se haya abierto una cuenta previamente
            print("\n¡Primero debes abrir una cuenta!\n")  # Muestra un mensaje de error
            continue
        else:
            print("\n-----DEPÓSITO-----")  # Muestra un mensaje para realizar un depósito
            monto = int(input("Ingrese el valor que desea depositar: "))  # Solicita al usuario que ingrese el monto a depositar
            p.depositar(monto)  # Realiza un depósito en la cuenta
            print("\nSu depósito se realizó con éxito.\n")  # Muestra un mensaje de éxito para el depósito

    elif opciones == 3:  # Opción para realizar un retiro
        if monto is None:  # Verifica que se haya realizado un depósito previo
            print("\n¡Primero debes hacer un depósito!\n")  # Muestra un mensaje de error
            continue
        else:
            print("\n-----RETIRO-----")  # Muestra un mensaje para realizar un retiro
            monto = int(input("Ingrese el valor que desea retirar: "))  # Solicita al usuario que ingrese el monto a retirar
            p.retirar(monto)  # Realiza un retiro de la cuenta

    elif opciones == 4:  # Opción para verificar el saldo de la cuenta
        if nombre is None or cuenta is None:  # Verifica que se haya abierto una cuenta previamente
            print("\n¡Primero debes abrir una cuenta!\n")  # Muestra un mensaje de error
            continue
        else:
            print("\n-----SALDO-----")  # Muestra un mensaje para verificar el saldo
            print(f"Cuenta bancaria: {p.numero_cuenta}")  # Muestra el número de cuenta
            print(f"Titular: {p.nombre_titular}")  # Muestra el nombre del titular de la cuenta
            print(f"Saldo actual: ${p.saldo}\n")  # Muestra el saldo actual de la cuenta
    else:
        print("\nOpción inválida. Por favor, ingrese un número válido.\n")  # Muestra un mensaje de error para opciones inválidas
        break

class Personaje:  # Clase que representa un personaje del juego
    def __init__(self, nombre, salud, fuerza, poder_ataque):  # Constructor de la clase
        self.__nombre = nombre  # Atributo privado para el nombre del personaje
        self.__salud = salud  # Atributo privado para la salud del personaje
        self.__fuerza = fuerza  # Atributo privado para la fuerza del personaje
        self.__poder_ataque = poder_ataque  # Atributo privado para el poder de ataque del personaje
    
    def mover(self, direccion):  # Método para mover al personaje en una dirección
        print(f"{self.__nombre} se mueve hacia {direccion}.")
    
    def atacar(self, enemigo):  # Método para que el personaje ataque a un enemigo
        print(f"{self.__nombre} ataca a 10 {enemigo} con una fuerza de {self.__fuerza + self.__poder_ataque}.")
    
    def usar_elemento(self, elemento):  # Método para que el personaje use un elemento
        print(f"{self.__nombre} utiliza el elemento {elemento}.")

    # Getters y setters para los atributos encapsulados

    def get_nombre(self):  # Método getter para obtener el nombre del personaje
        return self.__nombre
    
    def set_nombre(self, nombre):  # Método setter para establecer el nombre del personaje
        self.__nombre = nombre

    def get_salud(self):  # Método getter para obtener la salud del personaje
        return self.__salud
    
    def set_salud(self, salud):  # Método setter para establecer la salud del personaje
        self.__salud = salud
    
    def get_fuerza(self):  # Método getter para obtener la fuerza del personaje
        return self.__fuerza
    
    def set_fuerza(self, fuerza):  # Método setter para establecer la fuerza del personaje
        self.__fuerza = fuerza
    
    def get_poder_ataque(self):  # Método getter para obtener el poder de ataque del personaje
        return self.__poder_ataque
    
    def set_poder_ataque(self, poder_ataque):  # Método setter para establecer el poder de ataque del personaje
        self.__poder_ataque = poder_ataque

# Pedir al usuario que ingrese los atributos del personaje
nombre = input("Ingrese el nombre del personaje: ")
salud = int(input("Ingrese la salud del personaje: "))
fuerza = int(input("Ingrese la fuerza del personaje: "))
poder_ataque = int(input("Ingrese el poder de ataque del personaje: "))

# Crear una instancia de Personaje con los atributos ingresados
personaje = Personaje(nombre, salud, fuerza, poder_ataque)
personaje.set_nombre(nombre)

# Obtener y establecer los atributos encapsulados utilizando los getters y setters
print(personaje.get_nombre())
# Llamar a los métodos de la clase Personaje
personaje.mover("adelante")
personaje.atacar("jugadores")
personaje.usar_elemento("Poción")



class PaginaWeb:  # Clase que representa una página web
    def __init__(self, titulo, url):  # Constructor de la clase
        self.__titulo = titulo  # Atributo privado para el título de la página
        self.__url = url  # Atributo privado para la URL de la página
        self.__contenido = ""  # Atributo privado para el contenido de la página
    
    def cargar_pagina(self):  # Método para cargar la página
        print(f"Cargando página: {self.__url}")
    
    def mostrar_pagina(self):  # Método para mostrar la página
        print(f"Título: {self.__titulo}")
        print(f"URL: {self.__url}")
        print("Contenido:")
        print(self.__contenido)
    
    def agregar_contenido(self, contenido):  # Método para agregar contenido a la página
        self.__contenido += contenido

    # Getters y setters para los atributos encapsulados

    def get_titulo(self):  # Método getter para obtener el título de la página
        return self.__titulo
    
    def set_titulo(self, titulo):  # Método setter para establecer el título de la página
        self.__titulo = titulo

    def get_url(self):  # Método getter para obtener la URL de la página
        return self.__url
    
    def set_url(self, url):  # Método setter para establecer la URL de la página
        self.__url = url

    def get_contenido(self):  # Método getter para obtener el contenido de la página
        return self.__contenido
    
    def set_contenido(self, contenido):  # Método setter para establecer el contenido de la página
        self.__contenido = contenido

# Ejemplo de uso de la clase PaginaWeb

# Crear una instancia de PaginaWeb
pagina = PaginaWeb("Mi página web", "https://www.mipaginaweb.com")

# Obtener y establecer los atributos encapsulados utilizando los getters y setters
print(pagina.get_titulo())  # Imprime: Mi página web
pagina.set_titulo("Nueva página web")
print(pagina.get_titulo())  # Imprime: Nueva página web

# Llamar a los métodos de la clase PaginaWeb
pagina.cargar_pagina()  # Imprime: Cargando página: https://www.mipaginaweb.com
pagina.agregar_contenido("¡Bienvenidos a mi página web!")
pagina.mostrar_pagina()

