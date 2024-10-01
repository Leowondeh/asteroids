import pygame, sys, os, logging, time
from func.sendGreeting import *
from func.updateTitle import updateTitle
from constants import *
from sprites.circleShape import *
from sprites.player import *
from sprites.asteroid import *
from sprites.asteroidField import *
from sprites.shot import Shot

def main():

    # LOGGING
    logging.basicConfig(level=logging.DEBUG)
    # Pygame initialization
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Background
    backgroundImage = pygame.image.load('assets/bg.jpg').convert()
    backgroundRect = backgroundImage.get_rect()
    backgroundRect.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2

    # Vars
    gameClock = pygame.time.Clock()
    deltaTime = 0
    lives = 3
    score = 0
    gamemode = 'START'
    
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

    os.system('clear')
    sendGreeting('startprogram')
    updateTitle(gamemode, lives, score)

    # Game loop
    while True:
        try:
            while gamemode == 'RUNNING':
                # X button fix
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        os.system('clear')
                        sendGreeting('quickexit')
                        sys.exit()

                for item in updatable:
                    item.update(deltaTime)

                for asteroid in asteroids:
                    if asteroid.isColliding(player):
                        lives -= 1
                        if lives == 0:
                            os.system('clear')
                            sendGreeting('gameover')
                            sys.exit()
                        else:
                            updateTitle(gamemode, lives, score)
                            score -= 10
                            asteroid.kill()
                    for shot in shots:
                        if shot.isColliding(asteroid):
                            if asteroid.radius <= 20:
                                score += 1
                            elif asteroid.radius <= 40:
                                score += 2
                            else:
                                score += 3
                            shot.kill()
                            asteroid.split()
                            updateTitle(gamemode, lives, score)

                # Draw background
                screen.fill('black')
                screen.blit(backgroundImage, backgroundRect)
                pygame.draw.rect(screen, 'black', backgroundRect, 1)
                
                for item in drawable:
                    item.draw(screen)

                pygame.display.flip()

                # 60fps tickrate. maybe add option for this later?
                deltaTime = gameClock.tick(60) / 1000
            while gamemode == 'START':
                inp = input()
                if inp == 'q' or inp == 'quit':
                    os.system('clear')
                    sendGreeting('quickexit')
                    sys.exit()
                elif inp == 'o' or inp == 'opt' or inp == 'options':
                    raise NotImplementedError
                elif inp == 's' or inp == 'start':
                    os.system('clear')
                    sendGreeting('startgame')
                    gamemode = "RUNNING"
                    updateTitle(gamemode, lives, score)

        except KeyboardInterrupt:
            os.system('clear')
            sendGreeting('quickexit')
            sys.exit()



# Run main only if file is run directly
if __name__ == '__main__':
    main()