import pygame
import sys
import math
import random

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
