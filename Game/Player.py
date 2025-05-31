import pygame
import math



ANCHO = 800
ALTO = 600
BLANCO = (255, 255, 255)
class Personaje(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        try:
            self.image = pygame.image.load("Image/player-01.png")
            self.image = pygame.transform.scale(self.image, (50, 50))
        except:
            # Si no se encuentra la imagen, crear un triángulo como nave
            self.image = pygame.Surface((50, 50), pygame.SRCALPHA)
            pygame.draw.polygon(self.image, BLANCO, [(25, 0), (0, 50), (50, 50)])
        
        self.rect = self.image.get_rect()
        self.rect.center = (ANCHO // 2, ALTO // 2)
        self.velocidad = 0
        self.angulo = 0
        self.aceleracion = 0.1
        self.rotacion_velocidad = 5
        self.friccion = 0.98

    def update(self):
        # Rotación
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.angulo += self.rotacion_velocidad
        if teclas[pygame.K_RIGHT]:
            self.angulo -= self.rotacion_velocidad
        
        # Aceleración
        if teclas[pygame.K_UP]:
            self.velocidad += self.aceleracion
        
        # Actualizar posición basada en velocidad y ángulo
        self.rect.x += math.cos(math.radians(self.angulo)) * self.velocidad
        self.rect.y -= math.sin(math.radians(self.angulo)) * self.velocidad
        
        # Aplicar fricción
        self.velocidad *= self.friccion
        
        # Rotar la imagen
        self.image = pygame.transform.rotate(self.image, self.angulo)
        self.rect = self.image.get_rect(center=self.rect.center)
        
        # Mantener al personaje dentro de la pantalla
        if self.rect.left > ANCHO:
            self.rect.right = 0
        elif self.rect.right < 0:
            self.rect.left = ANCHO
        if self.rect.top > ALTO:
            self.rect.bottom = 0
        elif self.rect.bottom < 0:
            self.rect.top = ALTO