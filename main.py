import pygame
from constants import *


def main():
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init() # initalizing pygame
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT)) # set display size for screen

    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('Black')
        pygame.display.flip()
        
        dt = clock.tick(60) / 1000



if __name__ == "__main__":
    main()
