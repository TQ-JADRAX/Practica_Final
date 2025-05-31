import pygame
import random
from main import *
from Pesonaje import *

ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
class Asteroide(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, BLANCO, [
            (20, 0), (40, 20), (20, 40), (0, 20)
        ])
        self.rect = self.image.get_rect()
        self.velocidad_x = random.uniform(-2, 2)
        self.velocidad_y = random.uniform(-2, 2)
        self.rotacion = random.uniform(-3, 3)
        self.angulo = 0
        
        # Posición inicial aleatoria en los bordes
        lado = random.choice(['arriba', 'abajo', 'izquierda', 'derecha'])
        if lado == 'arriba':
            self.rect.x = random.randint(0, ANCHO)
            self.rect.y = -40
        elif lado == 'abajo':
            self.rect.x = random.randint(0, ANCHO)
            self.rect.y = ALTO
        elif lado == 'izquierda':
            self.rect.x = -40
            self.rect.y = random.randint(0, ALTO)
        else:
            self.rect.x = ANCHO
            self.rect.y = random.randint(0, ALTO)

    def update(self):
        self.rect.x += self.velocidad_x
        self.rect.y += self.velocidad_y
        self.angulo += self.rotacion
        self.image = pygame.transform.rotate(self.image, self.rotacion)
        
        # Mantener los asteroides dentro de la pantalla
        if self.rect.left > ANCHO:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = ANCHO
        if self.rect.top > ALTO:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = ALTO