import pygame
import sys
from pygame.locals import *

Negro = [0, 0, 0]
Blanco = [255, 255, 255]
Rojo = [255, 0, 0]
Verde = [0, 255, 0]
Azul = [0, 0, 255]
Amarillo = [255, 255, 0]
Cian = [0, 255, 255]
Magenta = [255, 0, 255]
Grisoscuro = [128, 128, 128]
Grisclaro = [192, 192, 192]
Naranja = [255, 165, 0]
Violeta = [238, 130, 238]
Marrón = [165, 42, 42]
Rosa = [255, 192, 203]
Turquesa = [64, 224, 208]
Oro = [255, 215, 0]
Plata = [192, 192, 192]
Celeste = [64, 207, 255]

class Figura():
    def __init__(self, alto, ancho, coordenadax, coordenaday):
        self.alto = alto
        self.ancho = ancho
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday

    def dibujarsuelo(self, ventana):
        pygame.draw.line(ventana, Marrón, [0, 400], [900, 400], 5)
        pygame.draw.rect(ventana, Verde, [self.coordenadax, self.coordenaday, self.ancho, self.alto])

        pygame.draw.line(ventana, Marrón, [self.coordenadax, self.coordenaday], [self.coordenadax + self.ancho, self.coordenaday], 4)
        pygame.draw.line(ventana, Marrón, [self.coordenadax, self.coordenaday + 1], [self.coordenadax + self.ancho, self.coordenaday + 1], 4)
        pygame.draw.line(ventana, Marrón, [self.coordenadax, self.coordenaday + 2], [self.coordenadax + self.ancho, self.coordenaday + 2], 4)
        pygame.draw.line(ventana, Marrón, [self.coordenadax, self.coordenaday + 3], [self.coordenadax + self.ancho, self.coordenaday + 3], 4)

        pygame.draw.line(ventana, [0, 100, 0], [self.coordenadax - 1, self.coordenaday - 1], [self.coordenadax + self.ancho + 1, self.coordenaday - 1], 4)
        pygame.draw.line(ventana, [0, 100, 0], [self.coordenadax - 1, self.coordenaday - 1], [self.coordenadax - 1, self.coordenaday + self.alto + 1], 4)
        pygame.draw.line(ventana, [0, 100, 0], [self.coordenadax + self.ancho + 1, self.coordenaday - 1], [self.coordenadax + self.ancho + 1, self.coordenaday + self.alto + 1], 4)
        pygame.draw.line(ventana, [0, 100, 0], [self.coordenadax - 1, self.coordenaday + self.alto + 1], [self.coordenadax + self.ancho + 1, self.coordenaday + self.alto + 1], 4)

    def dibujartriangulo(self, ventana):
        punto1 = [self.coordenadax, self.coordenaday]
        punto2 = [self.coordenadax + self.ancho, self.coordenaday]
        punto3 = [self.coordenadax + self.ancho / 2, self.coordenaday - self.alto]

        pygame.draw.polygon(ventana, Verde, [punto1, punto2, punto3])
        pygame.draw.polygon(ventana, [0, 100, 0], [punto1, punto2, punto3], 4)
        

class Jugador():
    def __init__(self, radio, coordenadax, coordenaday):
        self.radio = radio
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday
        self.velocidad_y = 0
        self.en_suelo = False

    def dibujar(self, ventana):
        pygame.draw.circle(ventana, Rojo, (self.coordenadax, self.coordenaday), self.radio)
    

    def saltar(self):
        if self.en_suelo:
            self.velocidad_y = -10
            self.en_suelo = False

    def aplicar_gravedad(self):
        if not self.en_suelo:
            self.velocidad_y += 0.3  # Reducir la gravedad para reducir la velocidad
            self.coordenaday += self.velocidad_y
            if self.coordenaday >= 380:
                self.coordenaday = 380
                self.velocidad_y = 0
                self.en_suelo = True

    def mover_izquierda(self):
        self.coordenadax -= 2  # Reducir la velocidad de movimiento a la izquierda

    def mover_derecha(self):
        self.coordenadax += 2  # Reducir la velocidad de movimiento a la derecha

class Enemigo():
    def __init__(self, ancho, alto, coordenadax, coordenaday):
        self.ancho = ancho
        self.alto = alto
        self.coordenadax = coordenadax
        self.coordenaday = coordenaday

    def dibujar(self, ventana):
        pygame.draw.rect(ventana, Rojo, [self.coordenadax, self.coordenaday, self.ancho, self.alto])

    def seguir_jugador(self, jugador):

        if self.coordenadax >= jugador.coordenadax:
            self.coordenadax -= 1
        elif self.coordenadax <= jugador.coordenadax:
             self.coordenadax -= 1

tamaño = (900, 500)
ventana = pygame.display.set_mode(tamaño)

suelo1 = Figura(150, 200, 100, 250)
suelo2 = Figura(199, 100, 300, 200)
triangulo1 = Figura(100, 100, 680, 395)
triangulo2 = Figura(150, 150, 750, 395)
triangulo3 = Figura(200, 200, 480, 395)
jugador = Jugador(18, 100, 300)
enemigo = Enemigo(20, 20, 800, 380)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                jugador.mover_izquierda()
            elif event.key == K_RIGHT:
                jugador.mover_derecha()
            elif event.key == K_UP:
                jugador.saltar()

    keys = pygame.key.get_pressed()
    if keys[K_LEFT]:
        jugador.mover_izquierda()
    if keys[K_RIGHT]:
        jugador.mover_derecha()

    jugador.aplicar_gravedad()
    enemigo.seguir_jugador(jugador)

    ventana.fill(Celeste)
    suelo1.dibujarsuelo(ventana)
    suelo2.dibujarsuelo(ventana)
    triangulo1.dibujartriangulo(ventana)
    triangulo2.dibujartriangulo(ventana)
    triangulo3.dibujartriangulo(ventana)
    jugador.dibujar(ventana)
    enemigo.dibujar(ventana)

    for x in range(tamaño[0]):
        color = [150, 75, 0]
        pygame.draw.line(ventana, color, [x, 400], [x, tamaño[1]], 1)

    # Verificar colisión entre el jugador y el enemigo
    if jugador.coordenadax + jugador.radio > enemigo.coordenadax and jugador.coordenadax < enemigo.coordenadax + enemigo.ancho:
        if jugador.coordenaday + jugador.radio > enemigo.coordenaday and jugador.coordenaday < enemigo.coordenaday + enemigo.alto:
            # El jugador ha sido golpeado por el enemigo (colisión)
            pygame.quit()
            sys.exit()

    pygame.display.flip()