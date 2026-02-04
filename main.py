import pygame
import sys

WIDTH, HEIGHT = 800, 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mein erstes Pygame-Fenster")
clock = pygame.time.Clock()

#gameloop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((30, 200, 30))

 
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
