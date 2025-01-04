from pygame.sprite import Sprite
import os
import pygame

class Character(Sprite):
    def __init__(self, type_, x,y, ammo, grenades):
        super().__init__()
        self.type_ = type_
        self.ammo = ammo
        self.grenades = grenades
        self.health = 100
        self.max_health = 100
        self.alive = True
        self.animation_types = os.listdir(f"assets/images/{type_}")
        self.all_images = {}
        for animation in self.animation_types:
            temp = []
            num_of_images = os.listdir(f"assets/images/{type_}/{animation}")
            for i in range(num_of_images):
                img = pygame.image.load(f"assets/images/{type_}/{animation}/{i}.png")
                img_w = img.get_width()
                img_h = img.get_height()
                img = pygame.transform.scale(img, (img_w * 2, img_h * 2))
                temp.append(img)
            self.all_images[animation] = temp
            
        self.image_number = 0
        self.action = "Idle"
        self.image = self.all_images[self.action][0]
        self.rect = self.image.get_rect(topleft=(x,y))
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
            
            
            
        
        