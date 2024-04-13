from pygame.sprite import Sprite
import pygame
class Coin(Sprite):
    def __init__(self, x,y, group):
        super().__init__()
        self.image = pygame.image.load("assets/coin.png")
        self.rect = self.image.get_rect(topleft=(x,y))
        self.direction = 1
        self.counter = 0
        group.add(self)
        
    def update(self):
        self.counter += 1
        self.rect.y += self.direction
        if self.counter >= 50:
            self.direction *= -1
            self.counter *= -1