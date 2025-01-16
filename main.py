import pygame
import sys
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, updatable, drawable)


    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    p1 = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2, shots_group=shots)
    rocks = AsteroidField()
    while(True):
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                return     
        screen.fill((0,0,0))
        
        for sprite in updatable:
            sprite.update(dt)

        for sprite in drawable:
            sprite.draw(screen)
        
        for sprite in asteroids:
            if sprite.collisions(p1):
                sys.exit("Game over!")
        
        for sprite in asteroids:
            for sprite2 in shots:
                 if sprite2.collisions(sprite):
                    sprite2.kill()
                    sprite.split()


        pygame.display.flip()
        dt = clock.tick(60) / 1000

    #print("Starting asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}\nScreen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
    