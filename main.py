import pygame
from constants import *
from circleshape import *
from player import *

def main():

    # Pygame initialization
    pygame.init()
    pygame.display.set_caption("Radu SAVE ME, pleae")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    gameClock = pygame.time.Clock()
    deltaTime = 0
    
    # Player instance
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game loop
    while True:
        # X button fix
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player.draw(screen)

        pygame.display.flip()

        # 60fps tickrate. maybe add option for this later?
        deltaTime = gameClock.tick(60) / 1000

# Run main only if file is run directly
if __name__ == "__main__":
    main()