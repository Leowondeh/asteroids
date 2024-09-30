import pygame, sys, os
from func.fileManagement import getVersion
from func.sendGreeting import *
from constants import *
from circleshape import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():

    # Pygame initialization
    pygame.init()
    pygame.display.set_caption(f"Asteroids_demo {getVersion()}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    deltaTime = 0
    
    # Containers for processing (BEFORE any objects are defined)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # Start instances & containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroidfield = AsteroidField()

    # Init message
    os.system('clear')
    sendGreeting('start')
    # Game loop
    while True:
        # X button fix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                os.system('clear')
                sendGreeting('quickexit')
                return

        for item in updatable:
            item.update(deltaTime)

        for asteroid in asteroids:
            if asteroid.isColliding(player):
                os.system('clear')
                sendGreeting('gameover')
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