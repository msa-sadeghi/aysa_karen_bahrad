from constants import *
from world import World
from levels.level1 import word_data
from player import Player
game_world = World(word_data)


my_player = Player()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False
    game_world.draw()
    my_player.draw()  
    my_player.update() 
    pygame.display.update()
    clock.tick(FPS)