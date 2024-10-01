import pygame
from .fileManagement import getVersion

def updateTitle(type, lives, score):
    if type == "RUNNING":
        pygame.display.set_caption(f"Asteroids v{getVersion()} | Lives {lives} | Score {score}")
    elif type == "PAUSED":
        pygame.display.set_caption(f"Asteroids v{getVersion()} | Paused (tap P again to resume)")
    elif type == "START":
        pygame.display.set_caption(f"Asteroids v{getVersion()} | Welcome! Check the console to start.")