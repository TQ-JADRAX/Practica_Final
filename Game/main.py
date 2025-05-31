import pygame
import sys

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mi Juego")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

# Clase del personaje
class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        self.sprite = pygame.image.load("Image\player-01.png")
        super().__init__()
        # Crear una superficie para el personaje (temporalmente un rectángul
        self.velocidad = 5

    def update(self):
        # Obtener las teclas presionadas
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.rect.x -= self.velocidad
        if teclas[pygame.K_RIGHT]:
            self.rect.x += self.velocidad
        if teclas[pygame.K_UP]:
            self.rect.y -= self.velocidad
        if teclas[pygame.K_DOWN]:
            self.rect.y += self.velocidad

        # Mantener al personaje dentro de la pantalla
        self.rect.clamp_ip(pantalla.get_rect())

# Crear el personaje
personaje = Personaje()
todos_sprites = pygame.sprite.Group()
todos_sprites.add(personaje)

# Bucle principal del juego
reloj = pygame.time.Clock()
ejecutando = True

while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar
    todos_sprites.update()

    # Dibujar
    pantalla.fill(NEGRO)
    todos_sprites.draw(pantalla)
    pygame.display.flip()

    # Controlar FPS
    reloj.tick(60)

pygame.quit()
sys.exit()
