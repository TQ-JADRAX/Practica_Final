import pygame
import math

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((10, 10), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 255, 255), (5, 5), 5)
        self.rect = self.image.get_rect()
        
        # Calcular la posición inicial de la bala en la punta de la nave
        # La nave tiene un tamaño de 50x50, así que usamos 25 como distancia desde el centro
        distancia = 25  # Distancia desde el centro de la nave
        self.rect.centerx = x + math.cos(math.radians(angle)) * distancia
        self.rect.centery = y - math.sin(math.radians(angle)) * distancia
        
        self.velocidad = 10
        self.angulo = angle
        self.tiempo_vida = 60  # Duración en frames (aproximadamente 1 segundo a 60 FPS)

    def update(self):
        # Mover la bala en la dirección del ángulo
        self.rect.x += math.cos(math.radians(self.angulo)) * self.velocidad
        self.rect.y -= math.sin(math.radians(self.angulo)) * self.velocidad
        
        # Reducir el tiempo de vida
        self.tiempo_vida -= 1
        
        # Eliminar la bala si se sale de la pantalla o se acaba su tiempo de vida
        if (self.rect.right < 0 or self.rect.left > 800 or 
            self.rect.bottom < 0 or self.rect.top > 600 or 
            self.tiempo_vida <= 0):
            self.kill()
