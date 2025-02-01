import pygame
from config import *
from character import Character
player_bullet_group = pygame.sprite.Group()
player_grenade_group = pygame.sprite.Group()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

player = Character("player", 100, 300, 0, 10)
clock = pygame.time.Clock()
moving_left, moving_right = (False, False)
bullet_shoot = False
grenade_shoot = False
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
            if event.key == pygame.K_SPACE:
                bullet_shoot = True
            if event.key == pygame.K_g:
                grenade_shoot = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moving_left = False
            if event.key == pygame.K_RIGHT:
                moving_right = False
            if event.key == pygame.K_UP:
                jumped = False
            if event.key == pygame.K_SPACE:
                bullet_shoot = False
            if event.key == pygame.K_g:
                grenade_shoot = False
    
    if moving_left or moving_right:
        player.change_animation("Run")
    else:
        player.change_animation("Idle")
        
    if jumped and player.in_air == False:
        player.in_air = True
        player.gravity = -15
    if player.in_air:
        player.change_animation("Jump") 
    if bullet_shoot:
        player.shoot("bullet", player_bullet_group) 
    if grenade_shoot:
        player.shoot("grenade", player_grenade_group)  
    player.move(moving_left, moving_right)   
    screen.fill("black")    
    player.draw(screen)  
    player_bullet_group.draw(screen)
    player_bullet_group.update()      
    player_grenade_group.draw(screen)
    player_grenade_group.update()      
    pygame.display.update()
    clock.tick(FPS)