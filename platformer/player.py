from pygame.sprite import Sprite
import pygame
from constants import *
class Player(Sprite):
    def __init__(self, x,y):
        super().__init__()
        
        self.right_images = []
        self.left_images = []
        for i in range(1, 5):
            img = pygame.image.load(f"assets/guy{i}.png")
            img = pygame.transform.scale(img, (64, 64))
            self.right_images.append(img)
            img = pygame.transform.flip(img, True, False)
            self.left_images.append(img)
            
       
        self.frame_index = 0
        self.counter = 0
        self.image = self.right_images[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        self.vel_y = 0
        self.jumped = False
        self.direction = 1
        self.idle = True
        self.inair = False
        self.dead_image = pygame.image.load("assets/ghost.png")
        self.alive = True
        self.score = 0
        self.coin_sound = pygame.mixer.Sound("assets/coin.wav")

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    
    def update(self, tiles, enemy_group, coin_group):
        dx = 0
        dy = 0
        if self.alive:
            COOL_DOWN = 3
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and not self.jumped and not self.inair:
                self.vel_y = -15
                self.jumped = True
                self.inair = True
            if not key[pygame.K_SPACE]:
                self.jumped = False
            if key[pygame.K_LEFT]:
                self.idle = False
                dx -= 5
                self.direction = -1
                self.counter += 1
            if key[pygame.K_RIGHT]:
                self.idle = False
                dx += 5
                self.direction = 1
                self.counter += 1
            
            if not key[pygame.K_LEFT] and not key[pygame.K_RIGHT]:
                self.counter += 1
                self.idle = True
            if self.counter > COOL_DOWN:
                self.counter = 0
                self.frame_index += 1
            if self.frame_index >= len(self.right_images):
                self.frame_index = 0
            if not self.idle:
                if self.direction == 1:
                    self.image = self.right_images[self.frame_index]
                if self.direction == -1:
                    self.image = self.left_images[self.frame_index]
            
            else:
                if self.direction == 1:
                    self.image = self.right_images[1]
                if self.direction == -1:
                    self.image = self.left_images[1]

            #add gravity
            dy += self.vel_y
            self.vel_y += 1
            
            
            for t in tiles:
                if t[1].colliderect(self.rect.x + dx, self.rect.y, self.rect.width, self.rect.height):
                    dx = 0
                if t[1].colliderect(self.rect.x, self.rect.y + dy, self.rect.width, self.rect.height):
                    self.vel_y = 0
                    dy = 0
                    self.inair = False
            
            if pygame.sprite.spritecollide(self, enemy_group, True):
                self.alive = False
            if pygame.sprite.spritecollide(self, coin_group, True):
                self.score += 1
                self.coin_sound.play()
        
            self.rect.x += dx
            self.rect.y += dy
        else:
            self.image = self.dead_image






        