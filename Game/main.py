import pygame
import sys
from Player import *
from Asteroid import *
from Bullet import *

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
balas = pygame.sprite.Group()
todos_sprites.add(personaje)

# Crear asteroides iniciales
for _ in range(6):
    asteroide = Asteroide()
    todos_sprites.add(asteroide)
    asteroides.add(asteroide)

# Variables para el control de disparos
tiempo_ultimo_disparo = 0
intervalo_disparo = 3000  # 3 segundos en milisegundos

# Bucle principal del juego
reloj = pygame.time.Clock()
ejecutando = True
puntuacion = 0
fuente = pygame.font.Font(None, 36)

while ejecutando:
    tiempo_actual = pygame.time.get_ticks()
    
    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecutando = False

    # Disparo automático cada 3 segundos
    if tiempo_actual - tiempo_ultimo_disparo > intervalo_disparo:
        bala = Bullet(personaje.rect.centerx, personaje.rect.centery, personaje.angulo)
        todos_sprites.add(bala)
        balas.add(bala)
        tiempo_ultimo_disparo = tiempo_actual

    # Actualizar
    todos_sprites.update()
    
    # Detectar colisiones entre balas y asteroides
    colisiones_balas = pygame.sprite.groupcollide(balas, asteroides, True, True)
    for bala, asteroides_colisionados in colisiones_balas.items():
        for asteroide in asteroides_colisionados:
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
