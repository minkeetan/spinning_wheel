import pygame
# wrapper to OS interface
import os
import random
import pandas as pd

pygame.font.init()

WIDTH, HEIGHT = 1200, 600
BG_WIDTH, BG_HEIGHT = 300, 50

FPS = 60 

# RGB in a tuple
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
BLUE = (0, 0 , 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)

NAME_FONT = pygame.font.SysFont('comicsans', 80)
CLASS_FONT = pygame.font.SysFont('comicsans', 40)
GAME_FONT = pygame.font.SysFont('comicsans', 80)
TIPS_FONT = pygame.font.SysFont('comicsans', 25)
TIME_FONT = pygame.font.SysFont('comicsans', 60)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pick me please")

def draw_window(person, time_counter, start_spinning, class_selected):

    # order of drawing does matter, as the screen that drew later will cover up the screen earlier
    WIN.fill(BLACK)

    game_title = GAME_FONT.render("Pick me please!", 1, BLACK)
    text_background = pygame.Rect(
        WIDTH // 2 - game_title.get_width() // 2, 50, game_title.get_width(), game_title.get_height())
    
    class_title = CLASS_FONT.render(class_selected, 1, GREEN)
    WIN.blit(class_title, (10, 10))

    pygame.draw.rect(WIN, YELLOW, text_background)
    WIN.blit(game_title, (WIDTH // 2 - game_title.get_width() // 2, 50))

    name_bg = pygame.Rect(WIDTH // 2 - BG_WIDTH // 2, HEIGHT // 4 * 3, BG_WIDTH, BG_HEIGHT)
    # pygame.draw.rect(WIN, YELLOW, name_bg)
    if start_spinning == False or time_counter == 0:
        tips = TIPS_FONT.render("Press Space bar to start", 1, YELLOW)
    else:
        tips = TIPS_FONT.render("Good Luck !", 1, YELLOW)

    WIN.blit(tips, (WIDTH // 2 - tips.get_width() // 2, HEIGHT // 4 * 3 - 20))

    if person != "" and time_counter >= 0:
        if time_counter > 0:
            timer = TIME_FONT.render(str(time_counter), 1, GREEN)
        else:
            timer = TIME_FONT.render("Congratulations!", 1, GREEN)

        # WIN.blit(timer, (WIDTH // 2 - timer.get_width() // 2, HEIGHT // 2 - 50))
        WIN.blit(timer, (WIDTH // 2 - timer.get_width() // 2, name_bg.y + timer.get_height() // 2))
        
        lucky_person = NAME_FONT.render(person, 1, ORANGE)

        # WIN.blit(lucky_person, (WIDTH // 2 - lucky_person.get_width() // 2, name_bg.y + lucky_person.get_height() // 2))
        WIN.blit(lucky_person, (WIDTH // 2 - lucky_person.get_width() // 2, HEIGHT // 2 - 50))
    
    pygame.display.update()

def draw_timer(time_counter):
    timer = TIME_FONT.render(str(time_counter), 1, BLUE)

    WIN.blit(timer, (WIDTH // 2 - timer.get_width() // 2, HEIGHT // 4 * 3 - 100))
    pygame.display.update()

def main():
    pygame.init()
    ONE_SEC_TIMER = pygame.USEREVENT + 1
    HUNDRED_MILE_TIMER = pygame.USEREVENT + 2
    pygame.time.set_timer(ONE_SEC_TIMER, 1000)
    pygame.time.set_timer(HUNDRED_MILE_TIMER, 100)

    clock = pygame.time.Clock()
    run = True
    start_spinning = False

    # load_name_list
    name_list = []
    class_list = ["2ST1", "2SK1", "2TA1", "2TB1", "2TC1"]
    class_index = 0
    person = ""
    person_index = 0
    time_counter = 5

    while run:
        # control the speed of the while loop, update 60 times per second`
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                start_spinning = False
                pygame.quit()
            
            if event.type == ONE_SEC_TIMER and time_counter > 0 and start_spinning == True:
                time_counter -= 1
            if event.type == HUNDRED_MILE_TIMER and time_counter > 0 and start_spinning == True:
                person = name_list[person_index]
                person_index += 1
                if person_index >= len(name_list):
                    person_index = 0
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and class_index + 1 < len(class_list) and start_spinning == False:
                    class_index += 1
                elif event.key == pygame.K_DOWN and class_index - 1 >= 0 and start_spinning == False:
                    class_index -= 1

        class_selected = class_list[class_index]
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and start_spinning == False:
            start_spinning = True
            time_counter = 5
            person_index = 0
            name_list = pd.read_csv("name_list.csv")
            name_list = name_list[name_list["class"] == class_selected]["name"].to_list()
            random.shuffle(name_list)
            print(name_list)
        
        # if len(name_list) > time_counter:
        #     person = name_list[time_counter]
        if time_counter == 0:
            start_spinning = False
            
        draw_window(person, time_counter, start_spinning, class_selected)

    main()

# To prevent the function being called when the file is imported instead of being called directly.
if __name__ == "__main__":
    main()
