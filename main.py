import pygame, sys, os, logging
from func.sendGreeting import *
from func.updateTitle import updateTitle
from constants import *
from sprites.circleShape import *
from sprites.player import *
from sprites.asteroid import *
from sprites.asteroidField import *
from sprites.shot import Shot

def main():

    # logging
    logging.basicConfig(level=logging.DEBUG)

    # pygame initialization
    pygame.init()
    gameClock, deltaTime, lives, score, gamemode = pygame.time.Clock(), 0, 3, 0, 'START'
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), display=DISPLAY)

    # console init message
    os.system('clear')
    sendGreeting('startprogram')

    # background
    backgroundImage = pygame.image.load('assets/bg.jpg').convert()
    backgroundRect = backgroundImage.get_rect()
    backgroundRect.center = SCREEN_WIDTH/2, SCREEN_HEIGHT/2
    
    # containers for processing (BEFORE any objects are defined)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # start instances & containers
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = (updatable)
    asteroidfield = AsteroidField()

    # set window title
    updateTitle(gamemode, lives, score)

    # game loop
    while True:
        try:
            while gamemode == 'RUNNING':
                # X button fix & pause controls
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        os.system('clear')
                        sendGreeting('quickexit')
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p: 
                            gamemode = 'PAUSED'
                            updateTitle(gamemode, lives, score)

                # update all in container
                for item in updatable:
                    item.update(deltaTime)

                # asteroid collision checks (with player and shots)
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

                # draw background
                screen.fill('black')
                screen.blit(backgroundImage, backgroundRect)
                pygame.draw.rect(screen, 'black', backgroundRect, 1)
                
                for item in drawable:
                    item.draw(screen)

                pygame.display.flip()

                deltaTime = gameClock.tick(60) / 1000

            # pause gamemode
            while gamemode == 'PAUSED':
                gameClock.tick(0)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        os.system('clear')
                        sendGreeting('quickexit')
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_p: 
                            gamemode = 'RUNNING'
                            gameClock.tick(60)
                            updateTitle(gamemode, lives, score)
            
            # start gamemode
            while gamemode == 'START':
                pygame.display.flip()
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        os.system('clear')
                        sendGreeting('quickexit')
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s: 
                            player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
                            gamemode = 'RUNNING'
                            updateTitle(gamemode, lives, score)
                        if event.key == pygame.K_o:
                            print(
'''     You can modify different constants used by the game in the 
     constants.py file. On the next restart the game will load them.
     Close the window to quit now or 's' to start the game as normal.''')

        # catch and exit if ctrl-c
        except KeyboardInterrupt:
            os.system('clear')
            sendGreeting('quickexit')
            sys.exit()

# run main only if file is run directly
if __name__ == '__main__':
    main()