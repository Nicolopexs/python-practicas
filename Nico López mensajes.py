# Definición de la clase MensajeQueue
class MensajeQueue:
    # Constructor de la clase, inicializa una cola vacía para los mensajes
    def __init__(self):
        self.cola_mensajes = []

    # Método para enviar un mensaje y agregarlo a la cola de mensajes
    def enviar_mensaje(self, mensaje):
        self.cola_mensajes.append(mensaje)
        print(self.cola_mensajes)

    # Método para recibir un mensaje de la cola de mensajes
    def recibir_mensaje(self):
        # Comprueba si hay mensajes en la cola
        if self.cola_mensajes:
            # Extrae y devuelve el mensaje más antiguo de la cola
            return self.cola_mensajes.pop()
        else:
            # Si no hay mensajes, devuelve None
            return None

# Función principal del programa
def main_mensaje_queue():
    # Crea una instancia de la clase MensajeQueue
    cola = MensajeQueue()

    while True:
        # Imprime el menú de opciones
        print("\n--- Menú ---")
        print("1. Enviar mensaje")
        print("2. Recibir mensaje")
        print("3. Salir")

        # Solicita al usuario que ingrese la opción deseada
        opcion = input("Ingrese el número de la opción deseada: ")

        if opcion == "1":
            # El usuario seleccionó enviar un mensaje, se solicita el mensaje y se envía
            mensaje = input("Ingrese el mensaje a enviar: ")
            cola.enviar_mensaje(mensaje)
            print("Mensaje enviado exitosamente.")

        elif opcion == "2":
            # El usuario seleccionó recibir un mensaje, se intenta recibir un mensaje de la cola
            mensaje_recibido = cola.recibir_mensaje()
            if mensaje_recibido:
                print(f"Mensaje recibido: {mensaje_recibido}")
            else:
                print("No hay mensajes en la cola.")

        elif opcion == "3":
            # El usuario seleccionó salir del programa, se imprime un mensaje y se sale del bucle while
            print("Saliendo del programa.")
            break

        else:
            # Opción no válida, se le pide al usuario que ingrese una opción válida
            print("Opción no válida. Intente nuevamente.")


# Definición de la clase FilaDeImpresion
class FilaDeImpresion:
    # Constructor de la clase, inicializa una cola vacía para las impresiones
    def __init__(self):
        self.cola = []

    # Método para agregar una impresión a la cola de impresión
    def agregar_impresion(self, imprimir):
        self.cola.append(imprimir)

    # Método para imprimir el trabajo en el primer lugar de la cola de impresión
    def imprimir_trabajo(self):
        # Comprueba si hay trabajos en la cola
        if self.cola:
            # Toma e imprime el trabajo en el primer lugar de la cola
            imprimir = self.cola.pop(0)
            print(f"Imprimiendo trabajo: [{imprimir}]")
        else:
            # Si no hay trabajos, imprime un mensaje indicando que la cola está vacía
            print("La cola de impresión está vacía.")

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("\n--- Menú ---")
    print("1. Agregar impresión")
    print("2. Imprimir trabajo")
    print("3. Salir")

# Función principal del programa
def main_fila_de_impresion():
    # Crea una instancia de la clase FilaDeImpresion
    fila_impresion = FilaDeImpresion()

    while True:
        # Muestra el menú de opciones
        mostrar_menu()

        # Solicita al usuario que ingrese la opción deseada
        opcion = input("Ingrese el número de opción: ")

        if opcion == '1':
            # El usuario seleccionó agregar impresión, solicita la cantidad de impresiones a realizar
            n = int(input("¿Cuántas impresiones desea realizar?: "))
            for _ in range(n):
                # Solicita el nombre del archivo a imprimir y lo agrega a la cola
                imprimir = input("Nombre del archivo: ")
                fila_impresion.agregar_impresion(imprimir)
            print(f"{n} trabajos agregados exitosamente.")

        elif opcion == '2':
            # El usuario seleccionó imprimir trabajos, imprime los trabajos en la cola
            for _ in range(len(fila_impresion.cola)):
                fila_impresion.imprimir_trabajo()

        elif opcion == '3':
            # El usuario seleccionó salir del programa, imprime un mensaje y sale del bucle while
            print("Saliendo del programa.")
            break

        else:
            # Opción inválida, se le pide al usuario que ingrese una opción válida
            print("Opción inválida. Por favor, seleccione una opción válida.")


def mostrar_menu_principal():
    print("\n--- Menú Principal ---")
    print("1. Programa de Sistema de mensajes")
    print("2. Programa de Fila de impresión")
    print("3. Salir")

def main():
    while True:
        mostrar_menu_principal()

        opcion = input("Ingrese el número de opción deseada: ")

        if opcion == "1":
            main_mensaje_queue()
        elif opcion == "2":
            main_fila_de_impresion()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
