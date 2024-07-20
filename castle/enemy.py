from pygame.sprite import Sprite
import pygame

class Enemy(Sprite):
    def __init__(self, type, x,y, group, speed):
        super().__init__()
        self.type = type
        self.animation_type = ("walk", "attack", "death")
        for animation in self.animation_type:
            images = []
            for i in range(20):
                img = pygame.image.load(f"assets/enemies/{self.type}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
            
        
        