from pygame.sprite import Sprite
import pygame
from explosion import Explosion
class Grenade(Sprite):
    def __init__(self, x,y, group, direction):
        super().__init__()
        self.image = pygame.image.load("./assets/images/icons/grenade.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        group.add(self)
        self.direction = direction
        self.xspeed = 4
        self.yspeed = -13
        self.timer = 100
        
        
    def update(self):
        self.rect.x += self.xspeed * self.direction
        if self.rect.bottom + self.yspeed >= 300:
            self.yspeed = 0
            self.xspeed = 0
        self.rect.y += self.yspeed
        self.yspeed += 1
        
        self.timer -= 1
        if self.timer <= 0:
            
        