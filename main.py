import pygame
# wrapper to OS interface
import os

WIDTH, HEIGHT = 900, 500

# RGB in a tuple
PURPLE = (255, 0, 255)
GREY = (150, 150, 150)
BLACK = (0, 0, 0)

# 60 frame per second
FPS = 60

SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55, 40

#Velocity
VEL = 5
BULLET_VEL = 7

#Number of bullets
MAX_BULLETS = 3

# Rect(x, y, width, height)
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

#bullets
red_bullets = []
yellow_bullets = []

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Spinning Wheel")

# use os.path so that it can handle the path in different OS, to get rid of different slashes
# Image is known as surface in pygame, to show the surface onto the screen, use blit
YELLOW_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_yellow.png"))
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)
RED_SPACESHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(RED_SPACESHIP_IMAGE, (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 270)


def draw_window(yellow, red):
    # order of drawing does matter, as the screen that drew later will cover up the screen earlier
    WIN.fill(GREY)    
    pygame.draw.rect(WIN, BLACK, BORDER)
    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SPACESHIP, (red.x, red.y))
    pygame.display.update()

def yellow_handle_movement(key_pressed, yellow):
    if key_pressed[pygame.K_a] and yellow.x - VEL > 0: # Left
        yellow.x -= VEL
    if key_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x: # Right
        yellow.x += VEL
    if key_pressed[pygame.K_w] and yellow.y - VEL > 0: # Up
        yellow.y -= VEL
    if key_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT: # Down
        yellow.y += VEL

def red_handle_movement(key_pressed, red):
    if key_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width: # Left
        red.x -= VEL
    if key_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH: # Right
        red.x += VEL
    if key_pressed[pygame.K_UP] and red.y - VEL > 0: # Up
        red.y -= VEL
    if key_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT: # Down
        red.y += VEL

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True

    while run:
        # control the speed of the while loop, update 60 times per second
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LCTRL and len(yellow_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height / 2 - 2, 10, 5)
                    yellow_bullets.append(bullet)
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height / 2 - 2, 10, 5)
                    red_bullets.append(bullet)
        
        print(yellow_bullets, red_bullets)

        key_pressed = pygame.key.get_pressed()
        yellow_handle_movement(key_pressed, yellow)        
        red_handle_movement(key_pressed, red)

        draw_window(yellow, red)

    pygame.quit()

# To prevent the function being called when the file is imported instead of being called directly.
if __name__ == "__main__":
    main()