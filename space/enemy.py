from constants import *
from pygame.sprite import Sprite
from egg import Egg
import random
class Enemy(Sprite):
    def __init__(self, image, x,y, enemy_group,egg_group):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        enemy_group.add(self)
        self.direction = 1
        self.speed = 5
        self.egg_group = egg_group
        
    def update(self):
        self.rect.x += self.direction * self.speed
        self.fire()
        
    def fire(self):
        if random.randint(1,1000) > 999:
            Egg(self.rect.centerx, self.rect.bottom, self.egg_group)
        
                
        
        