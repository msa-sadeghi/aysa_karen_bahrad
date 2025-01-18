import pygame
from config import *
from character import Character

screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Character("player", 100, 300, 0, 10)
clock = pygame.time.Clock()
moving_left, moving_right = (False, False)
jumped = False
running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moving_left = True
            if event.key == pygame.K_RIGHT:
                moving_right = True
            if event.key == pygame.K_UP:
                jumped = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
    
    if moving_left or moving_right:
        player.change_animation("Run")
    else:
        player.change_animation("Idle")
        
    if jumped:
        pass
        
    player.move(moving_left, moving_right)   
    screen.fill("black")    
    player.draw(screen)        
    pygame.display.update()
    clock.tick(FPS)