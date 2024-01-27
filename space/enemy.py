from constants import *
from pygame.sprite import Sprite

class Enemy(Sprite):
    def __init__(self, image, x,y, enemy_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        enemy_group.add(self)
        self.direction = 1
        self.speed = 5
        
    def update(self):
        self.rect.x += self.direction * self.speed
        
                
        
        