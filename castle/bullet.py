from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/bullet.png")
        self.image = pygame.transform.scale(self.image, (28,28))
        self.rect = self.image.get_rect()
        self.rect.midright = (x,y)
        group.add(self) 
    def update(self):
        self.rect.x -= 5