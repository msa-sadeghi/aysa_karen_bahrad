import pygame

screen_width = 800
screen_height = 600


screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
FPS = 60

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
            
    pygame.display.update()
    clock.tick(FPS)