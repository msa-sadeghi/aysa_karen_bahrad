import pygame

WIDTH = 800
HEIGHT = 640
FPS = 60
scroll = 0

scroll_left, scroll_right = (False,False)
# load bg images
mountain_image = pygame.image.load("./assets/images/background/mountain.png")
pine1_image = pygame.image.load("./assets/images/background/pine1.png")
pine2_image = pygame.image.load("./assets/images/background/pine2.png")
sky_cloud_image = pygame.image.load("./assets/images/background/sky_cloud.png")

def draw_background():
    screen.fill("green")
    sky_width = sky_cloud_image.get_width()
    for i in range(4):
        screen.blit(sky_cloud_image, (i * sky_width - scroll * 0.3,0))
        screen.blit(mountain_image, (i * sky_width - scroll * 0.4,HEIGHT - mountain_image.get_height() - 300))
        screen.blit(pine1_image, (i * sky_width - scroll * 0.5,HEIGHT - pine1_image.get_height() - 150))
        screen.blit(pine2_image, (i * sky_width - scroll * 0.6,HEIGHT - pine2_image.get_height()))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                scroll_left = True
            if event.key == pygame.K_RIGHT:
                scroll_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
    if scroll_left and scroll >0:
        scroll -= 5            
    if scroll_right:
        scroll += 5  
                  
    draw_background()       
    pygame.display.update()
    clock.tick(FPS)