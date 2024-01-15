import pygame
import random

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Geometry Dash")

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Jugador
player_width = 50
player_height = 50
player_x = 50
player_y = screen_height // 2 - player_height // 2
player_speed = 5

def draw_player():
    pygame.draw.rect(screen, WHITE, (player_x, player_y, player_width, player_height))

# Enemigos
enemy_width = 50
enemy_height = random.randint(10, screen_height - 10)
enemy_x = screen_width
enemy_y = screen_height - enemy_height
enemy_speed = 3

def draw_enemy():
    pygame.draw.rect(screen, WHITE, (enemy_x, enemy_y, enemy_width, enemy_height))

# Juego principal
running = True

while running:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Lógica del juego
    player_y += player_speed
    enemy_x -= enemy_speed

    # Dibujar en pantalla
    screen.fill(BLACK)
    draw_player()
    draw_enemy()

    # Actualizar pantalla
    pygame.display.flip()

    # Control de FPS
    pygame.time.Clock().tick(60)

# Salir del juego
pygame.quit()
