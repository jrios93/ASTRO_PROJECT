import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shoot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0



    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()


    Player.containers = updatable,drawable
    Asteroid.containers = updatable,drawable, asteroids_group
    AsteroidField.containers = updatable
    Shot.containers = updatable,drawable,shot_group


    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    

    asteroid_field = AsteroidField()

    

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for asteroid in asteroids_group:
            if player.collides_with(asteroid):
                print("Game Over!")
                running =False

        for shot in shot_group:
            for asteroid in asteroids_group:
                if shot.collides_with(asteroid):
                    asteroid.split()
                    shot.kill()

        screen.fill((0, 0, 0))
        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()
        
        dt = clock.tick(60) / 1000  # Corrección aquí

    pygame.quit()

if __name__ == "__main__":
    main()
