import pygame

class Button:
    def __init__(self, img, x,y):
        self.image = img
        self.rect = self.image.get_rect(topleft = (x,y))
    def draw(self, screen):
        clicked = False
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            if self.rect.collidepoint(mouse_pos):
                clicked = True
        screen.blit(self.image, self.rect)
        return clicked
