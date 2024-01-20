import pygame


pygame.init()


screen = pygame.display.set_mode()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()
martin_image = pygame.image.load("assets/martin.png")
player_image = pygame.image.load("assets/ship.png")
clock = pygame.time.Clock()
FPS = 60
# اضافه کردن فونت
# پیدا کردن تصویر پس زمینه مناسب برای بازی
# لود کردن تصویر پس زمینه در بازی
# قراردادن سفینه در پایین صفحه
# 