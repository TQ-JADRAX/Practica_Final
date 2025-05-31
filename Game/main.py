import pygame
import sys
from Pesonaje import * 
from Asteroid import * 

# Inicialización de Pygame
pygame.init()

# Configuración de la pantalla
ANCHO = 800
ALTO = 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Asteroids")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)


# Crear sprites
personaje = Personaje()
todos_sprites = pygame.sprite.Group()
asteroides = pygame.sprite.Group()
todos_sprites.add(personaje)

# Crear asteroides iniciales
for _ in range(6):
    asteroide = Asteroide()
    todos_sprites.add(asteroide)
    asteroides.add(asteroide)

# Bucle principal del juego
reloj = pygame.time.Clock()
ejecutando = True
puntuacion = 0
fuente = pygame.font.Font(None, 36)

while ejecutando:
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Actualizar
    todos_sprites.update()
    
    # Detectar colisiones
    colisiones = pygame.sprite.spritecollide(personaje, asteroides, True)
    for asteroide in colisiones:
        puntuacion += 10
        nuevo_asteroide = Asteroide()
        todos_sprites.add(nuevo_asteroide)
        asteroides.add(nuevo_asteroide)

    # Dibujar
    pantalla.fill(NEGRO)
    todos_sprites.draw(pantalla)
    
    # Mostrar puntuación
    texto_puntuacion = fuente.render(f"Puntuación: {puntuacion}", True, BLANCO)
    pantalla.blit(texto_puntuacion, (10, 10))
    
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
sys.exit()
