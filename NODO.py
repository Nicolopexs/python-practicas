class Directorio:
    # Definición de la clase Directorio, que representa un directorio en el sistema de archivos.

    def __init__(self, nombre):
        # Constructor de la clase Directorio. Recibe el nombre del directorio como argumento.

        self.nombre = nombre
        # Asigna el nombre pasado como argumento al atributo 'nombre' del objeto Directorio.

        self.subdirectorios = []
        # Inicializa el atributo 'subdirectorios' como una lista vacía para almacenar los subdirectorios del directorio.

        self.archivos = []
        # Inicializa el atributo 'archivos' como una lista vacía para almacenar los nombres de los archivos en el directorio.

    def agregar_subdirectorio(self, subdirectorio):
        # Método para agregar un subdirectorio al directorio actual. Recibe un objeto Directorio como argumento.

        self.subdirectorios.append(subdirectorio)
        # Agrega el subdirectorio pasado como argumento a la lista de subdirectorios del directorio.

    def agregar_archivo(self, archivo):
        # Método para agregar un archivo al directorio actual. Recibe el nombre del archivo como argumento.

        self.archivos.append(archivo)
        # Agrega el nombre del archivo pasado como argumento a la lista de archivos del directorio.

    def imprimir(self, nivel=0):
        # Método para imprimir la estructura del directorio en forma de árbol. Recibe un nivel opcional para la indentación.

        # Imprime el nombre del directorio con una indentación proporcional al nivel.
        print("    " * nivel + "|---" + self.nombre)

        # Imprime los nombres de los archivos en este directorio con una indentación mayor.
        for archivo in self.archivos:
            print("    " * (nivel + 1) + "|---" + archivo)

        # Recorre los subdirectorios y llama al método imprimir de forma recursiva para imprimir su contenido.
        for subdirectorio in self.subdirectorios:
            subdirectorio.imprimir(nivel + 1)

# Crear la estructura de directorios.
raiz = Directorio("C:")
dir1 = Directorio("Program Files")
dir2 = Directorio("Users")
dir3 = Directorio("Documents")

archivo1 = "notas.txt"
archivo2 = "imagen.jpg"

# Construir la estructura.
raiz.agregar_subdirectorio(dir1)
raiz.agregar_subdirectorio(dir2)
raiz.agregar_subdirectorio(dir3)

dir3.agregar_archivo(archivo1)
dir2.agregar_archivo(archivo2)

# Imprimir la estructura.
raiz.imprimir()

class Persona:  # Aquí se define la clase Persona, que representa a un individuo en el árbol genealógico.

    def __init__(self, nombre, edad, genero):  # Aquí se define el constructor de la clase Persona. Recibe el nombre, edad y género como argumentos.
        self.nombre = nombre  # Aquí se asigna el nombre pasado como argumento al atributo 'nombre' del objeto Persona.
        self.edad = edad  # Aquí se asigna la edad pasada como argumento al atributo 'edad' del objeto Persona.
        self.genero = genero  # Aquí se asigna el género pasado como argumento al atributo 'genero' del objeto Persona.
        self.padre = None  # Aquí se inicializa el atributo 'padre' como None, ya que aún no se ha establecido la relación con el padre.
        self.madre = None  # Aquí se inicializa el atributo 'madre' como None, ya que aún no se ha establecido la relación con la madre.
        self.hijos = []  # Aquí se inicializa el atributo 'hijos' como una lista vacía para almacenar los hijos del individuo.

    def agregar_hijo(self, hijo):  # Aquí se define el método para agregar un hijo al individuo actual. Recibe un objeto Persona como argumento.
        self.hijos.append(hijo)  # Aquí se agrega el hijo pasado como argumento a la lista de 'hijos' del objeto Persona.
        if self.genero == 'Masculino':  # Aquí se verifica si el género del individuo actual es 'Masculino'.
            hijo.padre = self  # Si es 'Masculino', se establece al objeto Persona actual como el padre del hijo.
        elif self.genero == 'Femenino':  # Aquí se verifica si el género del individuo actual es 'Femenino'.
            hijo.madre = self  # Si es 'Femenino', se establece al objeto Persona actual como la madre del hijo.

    def mostrar_familia(self, nivel=0):  # Aquí se define el método para mostrar la familia del individuo actual en forma de árbol. Recibe un nivel opcional para la indentación.
        espaciado = "    " * nivel  # Aquí se calcula el espacio de indentación proporcional al nivel.
        print(f"{espaciado}{self.nombre}, {self.edad} años, {self.genero}")  # Aquí se imprime la información del individuo con la indentación correspondiente.
        for hijo in self.hijos:  # Aquí se itera sobre los hijos del individuo actual.
            hijo.mostrar_familia(nivel + 1)  # Aquí se llama de forma recursiva al método mostrar_familia para imprimir los hijos del hijo actual.

# Crear el árbol genealógico
abuelo_paterno = Persona("Juan", 80, "Masculino")
abuela_paterna = Persona("Maria", 78, "Femenino")
abuelo_materno = Persona("Pedro", 75, "Masculino")
abuela_materna = Persona("Luisa", 72, "Femenino")
padre = Persona("Carlos", 50, "Masculino")
madre = Persona("Laura", 48, "Femenino")
hijo1 = Persona("Jorge", 25, "Masculino")
hijo2 = Persona("Ana", 22, "Femenino")

# Establecer las relaciones
abuelo_paterno.agregar_hijo(padre)
abuela_paterna.agregar_hijo(padre)
abuelo_materno.agregar_hijo(madre)
abuela_materna.agregar_hijo(madre)
padre.agregar_hijo(hijo1)
padre.agregar_hijo(hijo2)

# Mostrar el árbol genealógico
abuelo_paterno.mostrar_familia()


