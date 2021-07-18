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
GREY = (150, 150, 150)
BLUE = (0, 0 , 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 102, 0)

NAME_FONT = pygame.font.SysFont('comicsans', 40)
GAME_FONT = pygame.font.SysFont('comicsans', 80)
TIPS_FONT = pygame.font.SysFont('comicsans', 25)
TIME_FONT = pygame.font.SysFont('comicsans', 80)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pick me please")

def draw_window(person, time_counter, start_spinning):

    # order of drawing does matter, as the screen that drew later will cover up the screen earlier
    WIN.fill(BLACK)

    game_title = GAME_FONT.render("Pick me please!", 1, BLACK)
    text_background = pygame.Rect(
        WIDTH // 2 - game_title.get_width() // 2, 50, game_title.get_width(), game_title.get_height())

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
            timer = TIME_FONT.render(str(time_counter), 1, BLUE)
        else:
            timer = TIME_FONT.render("Congratulations!", 1, BLUE)

        WIN.blit(timer, (WIDTH // 2 - timer.get_width() // 2, HEIGHT // 2 - 50))
        
        lucky_person = NAME_FONT.render(person, 1, ORANGE)

        WIN.blit(lucky_person, (WIDTH // 2 - lucky_person.get_width() // 2, name_bg.y + lucky_person.get_height() // 2))
    
    pygame.display.update()

def draw_timer(time_counter):
    timer = TIME_FONT.render(str(time_counter), 1, BLUE)

    WIN.blit(timer, (WIDTH // 2 - timer.get_width() // 2, HEIGHT // 4 * 3 - 100))
    pygame.display.update()

def main():
    pygame.init()
    ONE_SEC_TIMER = pygame.USEREVENT + 1
    pygame.time.set_timer(ONE_SEC_TIMER, 1000)

    clock = pygame.time.Clock()
    run = True
    start_spinning = False

    # load_name_list
    name_list = []
    person = ""
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
                print("One sec timer tick!")
                time_counter -= 1

        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_SPACE] and start_spinning == False:
            start_spinning = True
            name_list = pd.read_csv("name_list.csv")
            # name_list = ["Alex Leo 1", "Alex Leo 2", "Alex Leo 3", "Alex Leo 4", "Alex Leo 5", "Alex Leo 6",
            # "Alex Leo 7", "Alex Leo 8", "Alex Leo 9", "Alex Leo 10", "Alex Leo 11", "Alex Leo 12"]
            name_list = name_list[name_list["class"] == "2ST1"]["name"].to_list()
            for x in range(random.randint(0,3)):
                random.shuffle(name_list)
            print(name_list)
        elif key_pressed[pygame.K_SPACE] and start_spinning == True and time_counter == 0:
            start_spinning = False
            break
        
        if len(name_list) > time_counter:
            person = name_list[time_counter].strip()
            
        draw_window(person, time_counter, start_spinning)

    main()

# To prevent the function being called when the file is imported instead of being called directly.
if __name__ == "__main__":
    main()
