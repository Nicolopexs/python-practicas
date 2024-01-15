# Definición de la clase EditorDeTexto que implementará un editor de texto con funcionalidad de deshacer/rehacer.
class EditorDeTexto:
    # Constructor de la clase, inicializa el texto actual y las pilas para deshacer y rehacer.
    def __init__(self):
        self.texto = ""
        self.deshacer_stack = []  # Pila para almacenar las acciones realizadas y deshacerlas.
        self.rehacer_stack = []  # Pila para almacenar las acciones deshechas y rehacerlas.

    # Método para mostrar el menú del editor con las opciones disponibles.
    def mostrar_menu(self):
        print("\n--- Editor de Texto ---")
        print("1. Escribir texto")
        print("2. Eliminar texto")
        print("3. Reemplazar texto")
        print("4. Deshacer")
        print("5. Rehacer")
        print("6. Mostrar texto actual")
        print("7. Salir")

    # Método para escribir texto, añade el texto ingresado al texto actual y limpia la pila de rehacer.
    def escribir_texto(self, texto):
        self.deshacer_stack.append(self.texto)  # Guardar el estado actual del texto antes de la acción.
        self.texto += texto
        self.rehacer_stack.clear()  # Limpiar la pila de rehacer, ya que se ha realizado una nueva acción.

    # Método para eliminar texto, elimina el texto dentro del rango indicado y limpia la pila de rehacer.
    def eliminar_texto(self, inicio, fin):
        self.deshacer_stack.append(self.texto)  # Guardar el estado actual del texto antes de la acción.
        self.texto = self.texto[:inicio] + self.texto[fin:]
        self.rehacer_stack.clear()  # Limpiar la pila de rehacer, ya que se ha realizado una nueva acción.

    # Método para reemplazar texto, reemplaza el texto dentro del rango indicado y limpia la pila de rehacer.
    def reemplazar_texto(self, inicio, fin, nuevo_texto):
        self.deshacer_stack.append(self.texto)  # Guardar el estado actual del texto antes de la acción.
        self.texto = self.texto[:inicio] + nuevo_texto + self.texto[fin:]
        self.rehacer_stack.clear()  # Limpiar la pila de rehacer, ya que se ha realizado una nueva acción.

    # Método para deshacer la última acción realizada, restaura el estado anterior del texto.
    def deshacer(self):
        if self.deshacer_stack:  # Verificar si hay acciones para deshacer.
            self.rehacer_stack.append(self.texto)  # Guardar el estado actual del texto antes de deshacer.
            self.texto = self.deshacer_stack.pop()

    # Método para rehacer la última acción deshecha, restaura el estado posterior del texto.
    def rehacer(self):
        if self.rehacer_stack:  # Verificar si hay acciones para rehacer.
            self.deshacer_stack.append(self.texto)  # Guardar el estado actual del texto antes de rehacer.
            self.texto = self.rehacer_stack.pop()

    # Método para mostrar el texto actual en pantalla.
    def mostrar_texto_actual(self):
        print("\nTexto actual:")
        print(self.texto)

if __name__ == "__main__":
    # Crear una instancia del editor de texto.
    editor = EditorDeTexto()

    # Bucle principal del programa.
    while True:
        # Mostrar el menú del editor.
        editor.mostrar_menu()

        # Obtener la opción seleccionada por el usuario.
        opcion = input("Seleccione una opción: ")

        # Ejecutar la acción correspondiente según la opción seleccionada.
        if opcion == "1":
            texto = input("Ingrese el texto a escribir: ")
            editor.escribir_texto(texto)
        elif opcion == "2":
            inicio = int(input("Ingrese el índice de inicio del texto a eliminar: "))
            fin = int(input("Ingrese el índice de fin del texto a eliminar: "))
            editor.eliminar_texto(inicio, fin)
        elif opcion == "3":
            inicio = int(input("Ingrese el índice de inicio del texto a reemplazar: "))
            fin = int(input("Ingrese el índice de fin del texto a reemplazar: "))
            nuevo_texto = input("Ingrese el nuevo texto: ")
            editor.reemplazar_texto(inicio, fin, nuevo_texto)
        elif opcion == "4":
            editor.deshacer()
        elif opcion == "5":
            editor.rehacer()
        elif opcion == "6":
            editor.mostrar_texto_actual()
        elif opcion == "7":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
