import pygame
from pygame.sprite import Sprite
from constants import *


class Player(Sprite):
    def __init__(self):
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH/2
        self.rect.bottom = WINDOW_HEIGHT
        self.catch_sound = pygame.mixer.Sound("assets/catch.wav")
        self.die_sound = pygame.mixer.Sound("assets/die.wav")

        self.lives = 3
        self.speed = 5
        self.alive = True

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT- 100:
            self.rect.y += self.speed
    def reset(self):
        self.rect.centerx = WINDOW_WIDTH/2
        self.rect.bottom = WINDOW_HEIGHT