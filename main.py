import pygame
import sys
from modules import button_module
from modules import spritesheet_module

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Button Beispiel")
clock = pygame.time.Clock()
FPS = 60

def on_play():
    print("Play Button gedrückt!")

play_button = button_module.image_button(
    idle_image=spritesheet_module.get_tile("images/UI_images/ui_spritesheet.png", (0,3), (1,1)),
    pressed_image=spritesheet_module.get_tile("images/UI_images/ui_spritesheet.png",(1,3), (1,1)),
    pos=(300, 630),
    size=(-1, 80),
    action=on_play
)

background = pygame.image.load("images/background_images/background_deafult.png")#bg load
background = pygame.transform.scale(background, (1920, 1080))#bg scale

heart_player = spritesheet_module.get_tile("images/ui_images/heart_spritesheet.png", (0,0), (5,2))
heart_player = pygame.transform.scale(heart_player, (350, 140)) 

heart_enemy = spritesheet_module.get_tile("images/ui_images/heart_spritesheet.png", (5,0), (5,2))
heart_enemy = pygame.transform.scale(heart_enemy, (350, 140)) 


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        play_button.handle_event(event)

    screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))#bg


    play_button.draw(screen)
    screen.blit(heart_player, (30, 5))
    screen.blit(heart_enemy, (1550, 5))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
