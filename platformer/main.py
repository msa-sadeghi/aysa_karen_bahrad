from constants import *
from world import World
from levels.level1 import word_data

game_world = World(word_data)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    game_world.draw()   
    pygame.display.update()
    clock.tick(FPS)