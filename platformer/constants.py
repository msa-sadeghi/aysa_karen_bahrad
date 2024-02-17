import pygame
pygame.init()
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 704
ROWS = SCREEN_HEIGHT // 32
COLS = SCREEN_WIDTH // 32
print(COLS, ROWS)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60