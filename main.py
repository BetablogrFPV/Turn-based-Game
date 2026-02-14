import pygame
import sys
from modules import button_module
from modules import spritesheet_module

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()
SCREEN_WIDTH, SCREEN_HEIGHT = 1920, 1080
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("turnBasedGame")
clock = pygame.time.Clock()
FPS = 10

current_screen = "launch_screen"


########################################################################### launch_screen:

launch_background = pygame.image.load("images/background_images/background_launch.png")
launch_background = pygame.transform.scale(launch_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

title_text = pygame.font.Font('Fonts/blox/Blox2.ttf', 125).render('Our Turnbased Game', False, 'Black')

def start_game():
    global current_screen
    current_screen = "selection_screen"

play_button = button_module.image_button(
    idle_image=spritesheet_module.get_tile("images/ui_images/control_button_spritesheet.png", (1,2), (1,1)),
    pressed_image=spritesheet_module.get_tile("images/ui_images/control_button_spritesheet.png",(2,2), (1,1)),
    pos=(SCREEN_WIDTH/2+20, 630),
    size=(100, -1),
    action=start_game,
    timing="delayed"
)

def quit_game():
    global running
    running = False

quit_button = button_module.image_button(
    idle_image=spritesheet_module.get_tile("images/ui_images/control_button_spritesheet.png", (1,1), (1,1)),
    pressed_image=spritesheet_module.get_tile("images/ui_images/control_button_spritesheet.png",(2,1), (1,1)),
    pos=(SCREEN_WIDTH/2-120, 630),
    size=(100, -1),
    action=quit_game,
    timing="delayed"
)

def launch_screen(events):
    for event in events:
        play_button.handle_event(event)
        quit_button.handle_event(event)

    screen.fill((0, 0, 0))
    screen.blit(launch_background, (0, 0))

    play_button.draw(screen)
    quit_button.draw(screen)


########################################################################### selection_screen:


def selection_screen(events):
    screen.fill((80, 80, 20))

   

########################################################################### game_screen:

default_background = pygame.image.load("images/background_images/background_default.png")
default_background = pygame.transform.scale(default_background, (SCREEN_WIDTH, SCREEN_HEIGHT))

heart_player = spritesheet_module.get_tile("images/ui_images/heart_spritesheet.png", (0,0), (5,2))
heart_player = pygame.transform.scale(heart_player, (350, 140)) 

heart_enemy = spritesheet_module.get_tile("images/ui_images/heart_spritesheet.png", (5,0), (5,2))
heart_enemy = pygame.transform.scale(heart_enemy, (350, 140)) 


def game_screen(events):

    screen.fill((0, 0, 0))
    screen.blit(default_background, (0, 0))

    screen.blit(heart_player, (30, 5))
    screen.blit(heart_enemy, (1550, 5))

########################################################################### loop:


running = True
while running:

    current_events = pygame.event.get()

    for event in current_events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False

    if current_screen == "launch_screen":
        launch_screen(current_events)
    elif current_screen == "selection_screen":
        selection_screen(current_events)
    elif current_screen == "game_screen":
        game_screen(current_events)

    pygame.display.set_caption(f"turnBasedGame - FPS: {clock.get_fps():.1f}")


    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
