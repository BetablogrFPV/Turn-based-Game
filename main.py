import pygame
import sys
from modules import button_module
from modules import spritesheet_module

import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


pygame.init()
WIDTH, HEIGHT = 1920, 1080
screen = pygame.display.set_mode((1920, 1080), pygame.SCALED | pygame.FULLSCREEN)
pygame.display.set_caption("turn based game")
clock = pygame.time.Clock()
FPS = 60

def on_play():
    global choosing_screen
    choosing_screen = True
    choosing_screen()

def choosing_screen():
    while choosing_screen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    choosing_screen = False
        screen.fill((30, 30, 30))
        screen.blit(background, (0, 0))#
        screen.blit(darken, (0,0))

play_button = button_module.image_button(
    idle_image=spritesheet_module.get_tile("images/ui_images/button_spritesheet.png", (1,6), (1,1)),
    pressed_image=spritesheet_module.get_tile("images/ui_images/button_spritesheet.png",(2,6), (1,1)),
    pos=(810, 630),
    size=(-1, 300),
    action=on_play
)

quit_button = button_module.image_button(
    idle_image=spritesheet_module.get_tile("images/ui_images/button_spritesheet.png", (1,6), (1,1)),
    pressed_image=spritesheet_module.get_tile("images/ui_images/button_spritesheet.png",(2,6), (1,1)),
    pos=(810, 830),
    size=(-1, 300),
    action = lambda: sys.exit()
)

background = pygame.image.load("images/background_images/background_deafult.png")#bg load
background = pygame.transform.scale(background, (1920, 1080))#bg scale

darken = pygame.Surface((WIDTH, HEIGHT))
darken.fill((0, 0, 0, 120))

heart_player = spritesheet_module.get_tile("images/ui_images/heart_spritesheet.png", (0,0), (5,2))
heart_player = pygame.transform.scale(heart_player, (350, 140)) 

heart_enemy = spritesheet_module.get_tile("images/ui_images/heart_spritesheet.png", (5,0), (5,2))
heart_enemy = pygame.transform.scale(heart_enemy, (350, 140)) 

text_play = pygame.font.Font('Fonts/minecraft/Minecraft/Minecraft-Regular.otf', 50).render('Play', False, 'White')
play_rect = text_play.get_rect(center=(play_button.rect.centerx, play_button.rect.centery - 95))

text_quit = pygame.font.Font('Fonts/minecraft/Minecraft/Minecraft-Regular.otf', 50).render('Quit', False, 'White')
quit_rect = text_quit.get_rect(center=(quit_button.rect.centerx, quit_button.rect.centery - 95))

title_text = pygame.font.Font('Fonts/blox/Blox2.ttf', 125).render('Our Turnbased Game', False, 'Black')

running = True
while running or choosing_screen or playing_screen:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        
        play_button.handle_event(event)
        quit_button.handle_event(event)

    screen.fill((30, 30, 30))
    screen.blit(background, (0, 0))#bg

    play_button.draw(screen)
    quit_button.draw(screen)

    screen.blit(text_play, play_rect)
    screen.blit(text_quit, quit_rect)
    screen.blit(title_text, (WIDTH//2 - title_text.get_width()//2, 180))
    screen.blit(heart_player, (30, 5))
    screen.blit(heart_enemy, (1550, 5))

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
