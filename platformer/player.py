from constants import *
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self):
        super().__init__()
        self.right_images = []
        self.left_images = []
        for i in range(1,5):
            img = pygame.image.load(f"assets/guy{i}.png")
            self.right_images.append(img)
            left_img = pygame.transform.flip(img, True, False)
            self.left_images.append(left_img)
            
        self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (100, 500)
        self.last_update_time = pygame.time.get_ticks()
        self.moving = False
        
    def draw(self):
        screen.blit(self.image, self.rect)
    
    def update(self):
        self.animation()
        self.move()
        
    def move(self):
        dx = 0
        dy = 0
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.moving = True
        
    def animation(self):
        if pygame.time.get_ticks() - self.last_update_time > 200:
            self.last_update_time = pygame.time.get_ticks()
            self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
        if not self.moving:    
            self.frame_index = 0
        self.image = self.right_images[self.frame_index]
        