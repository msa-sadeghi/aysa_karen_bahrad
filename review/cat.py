import pygame

class Cat:
    def __init__(self):
        
        self.images = []
        for i in range(1,3):
            im = pygame.image.load(f"cat{i}.svg")
            self.images.append(im)
            
        self.image = self.images[0]
        self.image_number = 0
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 200)
        self.last_update_time = 0
        
    def draw(self, screen):
        if pygame.time.get_ticks() - self.last_update_time > 200:
            self.last_update_time = pygame.time.get_ticks()
            self.image_number += 1
        if self.image_number >=2:
            self.image_number = 0
        self.image = self.images[self.image_number]
        screen.blit(self.image, self.rect)