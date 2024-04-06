import pygame

from constants import *
from world import World
from levels.level_creator import world_data

from player import Player

pygame.init()
enemy_group = pygame.sprite.Group()
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()

player = Player(100,screen_height-600)
world = World(world_data, enemy_group)

bg_img = pygame.image.load("assets/sky.png")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.blit(bg_img, (0,0))
    world.draw(screen)
    player.draw(screen)
    player.update(world.tile_list, enemy_group)
    enemy_group.update()
    enemy_group.draw(screen)

    pygame.display.update()
    clock.tick(FPS)

