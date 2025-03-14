import pygame
from circleshape import CircleShape
from constants import *

class Shot(CircleShape,pygame.sprite.Sprite):
  containers=None
  def __init__(self,x,y,rotation):
      pygame.sprite.Sprite.__init__(self,self.containers)
      super().__init__(x,y,SHOT_RADIUS)

      self.velocity  = pygame.Vector2(0,1).rotate(rotation) * PLAYER_SHOOT_SPEED
  
  def draw(self,screen):
      pygame.draw.circle(screen,"white",(int(self.position.x),int(self.position.y)),SHOT_RADIUS,2)

  def update(self,dt):
     self.position += self.velocity * dt

      


