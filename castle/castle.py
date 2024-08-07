from pygame.sprite import Sprite
import pygame
from bullet import Bullet
import math
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
        self.bullet_shot = False
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def shoot(self, group):
        if pygame.mouse.get_pressed()[0] and not self.bullet_shot:
            mouse_pos = pygame.mouse.get_pos()
            y_dist = -(mouse_pos[1] - self.rect.midleft[1])
            x_dist = mouse_pos[0] - self.rect.midleft[0]
            direction = math.atan2(y_dist, x_dist)
            Bullet(self.rect.midleft[0], self.rect.midleft[1], group, direction)
            self.bullet_shot = True
        if not pygame.mouse.get_pressed()[0]:
            self.bullet_shot = False
            