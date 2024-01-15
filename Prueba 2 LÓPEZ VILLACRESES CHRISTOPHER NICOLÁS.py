# Definición de la clase base Juego
class Juego:
    def jugar(self):
        print("¡Jugando al juego!")


# Definición de la subclase JuegoDeMesa, que hereda de Juego
class JuegoDeMesa(Juego):
    def configurar_juego(self):
        print("Configurando juego de mesa...")
    
    def mover_piezas(self):
        print("Moviendo piezas en el juego de mesa...")


# Definición de la subclase JuegoDeCartas, que hereda de Juego
class JuegoDeCartas(Juego):
    def configurar_juego(self):
        print("Configurando juego de cartas...")
    
    def repartir_cartas(self):
        print("Repartiendo cartas en el juego de cartas...")


# Definición de la subclase Videojuego, que hereda de Juego
class Videojuego(Juego):
    def configurar_juego(self):
        print("Configurando videojuego.")
    
    def mover_personaje(self):
        print("Moviendo personaje en el videojuego...")


# Creación de una instancia de JuegoDeMesa y llamada a sus métodos
juego_mesa = JuegoDeMesa()
juego_mesa.configurar_juego()
input("Presiona Enter para mover las piezas...")
juego_mesa.mover_piezas()
juego_mesa.jugar()

# Creación de una instancia de JuegoDeCartas y llamada a sus métodos
juego_cartas = JuegoDeCartas()
juego_cartas.configurar_juego()
input("Presiona Enter para repartir las cartas...")
juego_cartas.repartir_cartas()
juego_cartas.jugar()

# Creación de una instancia de Videojuego y llamada a sus métodos
videojuego = Videojuego()
videojuego.configurar_juego()
input("Presiona Enter para mover al personaje...")
videojuego.mover_personaje()
videojuego.jugar()
