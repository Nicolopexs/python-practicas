import pygame

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO_PANTALLA = 800
ALTO_PANTALLA = 600

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))
pygame.display.set_caption("Rompecabezas")

# Color de fondo
COLOR_FONDO = (255, 255, 255)

# Clase para representar una pieza del rompecabezas
class Pieza:
    def __init__(self, imagen, x, y):
        self.imagen = pygame.image.load(imagen)
        self.rect = self.imagen.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.arrastrando = False

    def dibujar(self):
        pantalla.blit(self.imagen, self.rect)

    def actualizar(self):
        if self.arrastrando:
            self.rect.center = pygame.mouse.get_pos()

    def comenzar_arrastre(self):
        self.arrastrando = True

    def terminar_arrastre(self):
        self.arrastrando = False

# Crear las piezas del rompecabezas
pieza1 = Pieza("pieza1.png", 100, 100)
pieza2 = Pieza("pieza2.png", 300, 100)
pieza3 = Pieza("pieza3.png", 500, 100)

# Lista de piezas del rompecabezas
piezas = [pieza1, pieza2, pieza3]

# Bucle principal del juego
jugando = True
while jugando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            jugando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Comprobar si se hizo clic en una pieza
            for pieza in piezas:
                if pieza.rect.collidepoint(evento.pos):
                    pieza.comenzar_arrastre()
        elif evento.type == pygame.MOUSEBUTTONUP:
            # Terminar el arrastre de la pieza
            for pieza in piezas:
                if pieza.arrastrando:
                    pieza.terminar_arrastre()

    # Actualizar las piezas
    for pieza in piezas:
        pieza.actualizar()

    # Dibujar en la pantalla
    pantalla.fill(COLOR_FONDO)
    for pieza in piezas:
        pieza.dibujar()
    pygame.display.flip()

# Salir del juego
pygame.quit()
