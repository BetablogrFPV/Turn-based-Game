import pygame
import sys
from modules.button_module import butten_image  # Hier importieren

pygame.init()
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Button Beispiel")
clock = pygame.time.Clock()
FPS = 60

def on_play():
    print("Play Button gedrückt!")

play_button = ImageButton(
    "assets/button_play.png",
    pos=(300, 250),
    size=(-1, 100),
    action=on_play
)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        play_button.handle_event(event)

    screen.fill((30, 30, 30))

    play_button.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
