import pygame
from cat import Cat

my_cat = Cat()

screen_width = 480
screen_height = 360
white_color = (255,255,255)

FPS = 60
clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))

running = True
while running == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(white_color) 
    my_cat.draw(screen)       
    pygame.display.update()
    clock.tick(FPS)