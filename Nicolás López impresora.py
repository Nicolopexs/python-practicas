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
def main():
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

# Ejecuta la función main si este archivo es el programa principal
if __name__ == "__main__":
    main()

