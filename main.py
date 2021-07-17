import pygame
# wrapper to OS interface
import os

WIDTH, HEIGHT = 900, 500

# RGB in a tuple
PURPLE = (255, 0, 255)
WHITE = (255, 255, 255)

# 60 frame per second
FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Wheel")

# use os.path so that it can handle the path in different OS, to get rid of different slashes
# Image is known as surface in pygame, to show the surface onto the screen, use blit
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT))


def draw_window():
    # order of drawing does matter, as the screen that drew later will cover up the screen earlier
    WIN.fill(WHITE)
    WIN.blit(YELLOW_SPACESHIP, (300, 100))
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True

    while run:
        # control the speed of the while loop, update 60 times per second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        draw_window()

    pygame.quit()

# To prevent the function being called when the file is imported instead of being called directly.
if __name__ == "__main__":
    main()