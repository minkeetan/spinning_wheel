import pygame
# wrapper to OS interface
import os
pygame.font.init()

WIDTH, HEIGHT = 900, 500

FPS = 60

# RGB in a tuple
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Wheel")

def draw_window():
    # order of drawing does matter, as the screen that drew later will cover up the screen earlier
    WIN.fill(WHITE)
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
