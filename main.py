import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() # initalizing pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # set display size for screen

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('Black')
        pygame.display.flip()


if __name__ == "__main__":
    main()
