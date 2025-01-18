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
            num_of_images = len(os.listdir(f"assets/images/{type_}/{animation}"))
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
        self.last_image_change_time = 0
        self.flip = False
        self.gravity = 0
        
    def draw(self, screen):
        self.animation()
        img = self.all_images[self.action][self.image_number]
        img = pygame.transform.flip(img, self.flip, False)
        screen.blit(img, self.rect)
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_image_change_time > 100:
            self.last_image_change_time = pygame.time.get_ticks()
            self.image_number += 1
            if self.image_number >= len(self.all_images[self.action]):
                self.image_number = 0
                
                
    def move(self, moving_left, moving_right):
        dx = 0
        dy = 0
        if moving_right:
            dx += 5
            self.flip = False
        if moving_left:
            dx -= 5
            self.flip = True
        dy += self.gravity
        self.gravity += 1
        if self.rect.bottom + dy > 300:
            dy = 300 - self.rect.bottom
            self.gravity = 0
        self.rect.y += dy    
        self.rect.x += dx
        
        
    def change_animation(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.image_number = 0
            self.last_image_change_time = pygame.time.get_ticks()
        
            
            
            
        
        