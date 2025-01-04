import pygame
from config import *
from character import Character

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Character("player", 100, 300, 0, 10)
clock = pygame.time.Clock()


running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)