import pygame

screen=pygame.display.set_mode((600,400))


rect=pygame.Rect(10,10,200,130)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,"red",rect)

    pygame.display.update()
