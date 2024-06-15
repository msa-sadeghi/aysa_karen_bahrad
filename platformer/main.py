import pygame

from constants import *
from world import World


from player import Player
from button import Button
import pickle

level = 1
f = open("levels/level1", "rb") 
world_data = pickle.load(f)
f.close()
restart_btn = Button(screen_width/2, screen_height/2)

pygame.init()
enemy_group = pygame.sprite.Group()
coin_group = pygame.sprite.Group()
door_group = pygame.sprite.Group()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player(100,screen_height-600)



world = World(world_data, enemy_group, coin_group, door_group)

bg_img = pygame.image.load("assets/sky.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    world.draw(screen)
    player.draw(screen)
    player.update(world.tile_list, enemy_group, coin_group)
    enemy_group.update()
    enemy_group.draw(screen)
    coin_group.update()
    coin_group.draw(screen)
    door_group.draw(screen)
    if not player.alive:
        if restart_btn.draw(screen):
            player.__init__(100,screen_height-600)
            enemy_group.empty()
            coin_group.empty()
            world = World(world_data, enemy_group, coin_group, door_group)

    pygame.display.update()
    clock.tick(FPS)

