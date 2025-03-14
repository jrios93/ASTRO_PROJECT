import pygame
from circleshape import CircleShape
from constants import *
from shoot import Shot


class Player(CircleShape, pygame.sprite.Sprite):
    containers = None


    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self,self.containers)
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.position = pygame.Vector2(x,y)
        self.timer = 0




    def triangle(self):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        right = pygame.Vector2(0,1).rotate(self.rotation + 90) * self.radius / 1.5
        

        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self,screen):
        pygame.draw.polygon(screen, "white",self.triangle(),2)

    def rotate(self,direction, dt):
        self.rotation += direction * PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= dt

        if keys[pygame.K_a]:
            # ?
           self.rotate(-1,dt)
        if keys[pygame.K_d]:
            # ?
            self.rotate(1,dt)
        if keys[pygame.K_w]:
            self.move(1,dt)
        if keys[pygame.K_s]:
            self.move(-1,dt)
        if keys[pygame.K_SPACE] and self.timer <=0:
            self.shoot()
            self.timer = PLAYER_SHOOT_COOLDOWN
            

    def move(self,direction,dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt * direction

    def shoot(self):
        if Shot.containers:
            Shot(self.position.x, self.position.y, self.rotation)


            

