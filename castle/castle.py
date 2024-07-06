from pygame.sprite import Sprite
import pygame

class Castle(Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image_100 = pygame.image.load("assets/castle/castle_100.png")
        image_100_w = self.image_100.get_width()
        image_100_h = self.image_100.get_height()
        self.image_100 = pygame.transform.scale(self.image_100, (image_100_w * 0.2, image_100_h * 0.2))
        self.image_50 = pygame.image.load("assets/castle/castle_50.png")
        image_50_w = self.image_50.get_width()
        image_50_h = self.image_50.get_height()
        self.image_50 = pygame.transform.scale(self.image_50, (image_50_w * 0.2, image_50_h * 0.2))
        self.image_25 = pygame.image.load("assets/castle/castle_25.png")
        image_25_w = self.image_25.get_width()
        image_25_h = self.image_25.get_height()
        self.image_25 = pygame.transform.scale(self.image_25, (image_25_w * 0.2, image_25_h * 0.2))
        self.image = self.image_100
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        
        self.health = 100
        self.max_health = 100
        self.money = 0
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)