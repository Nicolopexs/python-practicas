class Electrodomestico:
    def __init__(self, nombre, estado=False):
        # El método __init__ se llama al crear una nueva instancia de la clase
        # Aquí se inicializan los atributos de la instancia: nombre y estado
        self.nombre = nombre
        self.estado = estado
    
    def encender(self):
        # Método para encender el electrodoméstico
        self.estado = True

    def apagar(self):
        # Método para apagar el electrodoméstico
        self.estado = False

    def __str__(self):
        # Método especial para representar el objeto como una cadena
        # Se usa para personalizar la forma en que se muestra la información del electrodoméstico
        estado_str = "encendido" if self.estado else "apagado"
        return f"Electrodoméstico: {self.nombre} / Estado: {estado_str}"


# Ejemplo de uso
# Creación de instancias de la clase Electrodomestico
electrodomestico1 = Electrodomestico(input("Ingrese el Electrodomestico: "))
electrodomestico2 = Electrodomestico(input("Ingrese el Electrodomestico: "))
electrodomestico3 = Electrodomestico(input("Ingrese el Electrodomestico: "))
electrodomestico4 = Electrodomestico(input("Ingrese el Electrodomestico: "))
electrodomestico5 = Electrodomestico(input("Ingrese el Electrodomestico: "))

# Muestra el estado inicial de los electrodomésticos
input("Presiona Enter para ver el estado de los electrodomesticos... ")
print(electrodomestico1)  # Imprime: Electrodoméstico: Lavadora / Estado: apagado
print(electrodomestico2)
print(electrodomestico3)
print(electrodomestico4)
print(electrodomestico5)

# Enciende los electrodomésticos
input("Presiona Enter para encender los electrodomesticos... ")
electrodomestico1.encender()
electrodomestico2.encender()
electrodomestico3.encender()
electrodomestico4.encender()
electrodomestico5.encender()

# Verifica el estado de los electrodomésticos después de encenderlos
input("Presiona Enter para verificar... ")
print(electrodomestico1)  # Imprime: Electrodoméstico Hijo: Lavadora / Estado: encendido
print(electrodomestico2)
print(electrodomestico3)
print(electrodomestico4)
print(electrodomestico5)
