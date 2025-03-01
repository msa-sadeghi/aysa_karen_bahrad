import pygame

from button import Button

WIDTH = 800
HEIGHT = 640
FPS = 60
SIDE_MARGIN = 300
LOWER_MARGIN = 150
MAX_COLS = 150
ROWS = 16

TILE_SIZE = HEIGHT // ROWS
scroll = 0
scroll_speed = 1
scroll_left, scroll_right = (False,False)
# load bg images
mountain_image = pygame.image.load("./assets/images/background/mountain.png")
pine1_image = pygame.image.load("./assets/images/background/pine1.png")
pine2_image = pygame.image.load("./assets/images/background/pine2.png")
sky_cloud_image = pygame.image.load("./assets/images/background/sky_cloud.png")
current_tile = 0
def draw_grid():
    for i in range(ROWS + 1):
        pygame.draw.line(screen, "white", (0, i * TILE_SIZE), (WIDTH, i * TILE_SIZE))
    for i in range(MAX_COLS + 1):
        pygame.draw.line(screen, "white", (i * TILE_SIZE - scroll, 0), (i * TILE_SIZE - scroll, HEIGHT))


def draw_background():
    screen.fill("green")
    sky_width = sky_cloud_image.get_width()
    for i in range(4):
        screen.blit(sky_cloud_image, (i * sky_width - scroll * 0.3,0))
        screen.blit(mountain_image, (i * sky_width - scroll * 0.4,HEIGHT - mountain_image.get_height() - 300))
        screen.blit(pine1_image, (i * sky_width - scroll * 0.5,HEIGHT - pine1_image.get_height() - 150))
        screen.blit(pine2_image, (i * sky_width - scroll * 0.6,HEIGHT - pine2_image.get_height()))

images_list = list()
for i in range(21):
    img = pygame.image.load(f"./assets/images/tile/{i}.png")
    img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
    images_list.append(img)
buttons_list = []
row_number = 0
col_number = 0
for i in range(21):
    btn = Button(
        images_list[i],
        WIDTH + col_number * 60 + 60,
        row_number * 60 + 60,
        )
    buttons_list.append(btn)
    col_number += 1
    if col_number == 3:
        row_number += 1
        col_number = 0

world_data = []
for i in range(ROWS):
    row = [-1] * MAX_COLS
    world_data.append(row)

def draw_world():
    for i in range(len(world_data)):
        for j in range(len(world_data[i])):
            if world_data[i][j] >= 0:
                screen.blit(buttons_list[world_data[i][j]].image, (j * TILE_SIZE - scroll, i * TILE_SIZE))


screen = pygame.display.set_mode((WIDTH + SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
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
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                scroll_left = False
            if event.key == pygame.K_RIGHT:
                scroll_right = False
            if event.key == pygame.K_LSHIFT:
                scroll_speed = 1
    if scroll_left and scroll >0:
        scroll -= 5 * scroll_speed           
    if scroll_right:
        scroll += 5  * scroll_speed



    draw_background() 
    draw_grid()
    pygame.draw.rect(screen, "lightgreen", (WIDTH, 0, SIDE_MARGIN, HEIGHT + LOWER_MARGIN))
    for i in range(len(buttons_list)):
        if buttons_list[i].draw(screen) :
            current_tile=  i 

    pygame.draw.rect(screen, "red", buttons_list[current_tile].rect, 3)   
    draw_world()
    mouse_pos = pygame.mouse.get_pos()
    col = (mouse_pos[0] + scroll)//TILE_SIZE
    row = mouse_pos[1] // TILE_SIZE
    if pygame.mouse.get_pressed()[0] and mouse_pos[0] < WIDTH and mouse_pos[1] < HEIGHT:
        if world_data[row][col] != current_tile:
            world_data[row][col] = current_tile
    if pygame.mouse.get_pressed()[2]:
        world_data[row][col] = -1

    pygame.display.update()
    clock.tick(FPS)