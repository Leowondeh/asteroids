import pygame
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *

def main():

    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("Asteroids_demo0.0.1")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    deltaTime = 0
    
    # Containers for processing (BEFORE any objects are defined)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # Start instances & containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()
    
    # Game loop
    while True:
        # X button fix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for item in updatable:
            item.update(deltaTime)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                print("Game over!")
                return
        screen.fill("black")
        
        for item in drawable:
            item.draw(screen)

        pygame.display.flip()

        # 60fps tickrate. maybe add option for this later?
        deltaTime = gameClock.tick(60) / 1000

# Run main only if file is run directly
if __name__ == "__main__":
    main()