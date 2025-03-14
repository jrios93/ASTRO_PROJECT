import pygame
import random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape, pygame.sprite.Sprite):

    containers = None

    def __init__(self,x,y,radius):
        pygame.sprite.Sprite.__init__(self, self.containers)
        super().__init__(x,y,radius)

        self.position = pygame.Vector2(x,y)
        self.velocity = pygame.Vector2(1,0)


    def draw(self,screen):
        pygame.draw.circle(screen,"white",(int(self.position.x),int(self.position.y)),self.radius,2)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        if self.radius <= ASTEROID_MIN_RADIUS:
            self.kill()
            
        
        random_angle = random.uniform(20, 50)

        # Crear dos nuevos vectores de dirección
        velocity1 = self.velocity.rotate(random_angle) * 1.2  # Más rápido
        velocity2 = self.velocity.rotate(-random_angle) * 1.2

        # Nuevo radio de los asteroides más pequeños
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # Crear dos nuevos asteroides
        new_asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # Asignar las nuevas velocidades
        new_asteroid1.velocity = velocity1
        new_asteroid2.velocity = velocity2

        # Añadir a los grupos correspondientes
        self.containers[0].add(new_asteroid1, new_asteroid2)  # updatable
        self.containers[1].add(new_asteroid1, new_asteroid2)  # drawable
        self.containers[2].add(new_asteroid1, new_asteroid2)  # asteroids_group

        # Eliminar el asteroide original
        self.kill()







