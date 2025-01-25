from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    def __init__(self, x,y, direction, group):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/bullet.png")
        self.rect = self.image.get_rect(center = (x,y))
        self.direction = direction
        group.add(self)
        
    def update(self):
        self.rect.x += self.direction * 4
        if self.rect.x <= 0 or self.rect.right >= 800:
            self.kill()