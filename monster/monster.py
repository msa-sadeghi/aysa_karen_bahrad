from pygame.sprite import Sprite
import pygame
import random
from constants import *
class Monster(Sprite):
    def __init__(self, x, y, image, monster_group, monster_type):
        super().__init__()
        self.image = image
        self.type = monster_type
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.velocity = random.randint(1,5)
        self.dirx = random.choice([-1,1])
        self.diry = random.choice([-1,1])
        monster_group.add(self)

    def update(self):
        self.rect.x += self.dirx * self.velocity
        self.rect.y += self.diry * self.velocity
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dirx *= -1

        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.diry *= -1

