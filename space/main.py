from constants import *
from player import Player
from enemy import Enemy

my_player = Player(player_image)
enemy_group = pygame.sprite.Group()
level = 0

def check_if_on_edge():
    on_edge = False
    for enemy in enemy_group:
        if enemy.rect.left <= 0 or enemy.rect.right>=SCREEN_WIDTH:
            on_edge = True
    if on_edge == True:
        breach = False
        for enemy in enemy_group:
            enemy.rect.y += 5 * level
            enemy.direction *= -1
            if enemy.rect.bottom >= SCREEN_HEIGHT - 100:
                breach = True
                
        if breach == True:
            pass


def start_new_level():
    global level
    level += 1
    for i in range(5):
        for j in range(10):
            Enemy(martin_image, j * 96, i * 96, enemy_group)
start_new_level()   
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill((0,0,0))
    my_player.draw()
    my_player.move()
    enemy_group.update()
    enemy_group.draw(screen)
    check_if_on_edge()
    pygame.display.update()
    clock.tick(FPS)