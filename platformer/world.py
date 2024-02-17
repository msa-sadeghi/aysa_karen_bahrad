from constants import *
class World:
    def __init__(self, world_data):
        img = pygame.image.load("assets/sky.png")
        self.image = pygame.transform.scale(img, (1024,704))
        self.tile_map = []
        
        for i in range(len(world_data)):
            for j in range(len(world_data[i])):
                if world_data[i][j] == 1:
                    img = pygame.image.load("assets/dirt.png")
                    img = pygame.transform.scale(img, (32,32))
                    rect = img.get_rect(topleft=(j * 32, i * 32))
                    self.tile_map.append((img, rect))
                if world_data[i][j] == 2:
                    img = pygame.image.load("assets/grass.png")
                    img = pygame.transform.scale(img, (32,32))
                    rect = img.get_rect(topleft=(j * 32, i * 32))
                    self.tile_map.append((img, rect))
                    
    def draw(self):
        screen.blit(self.image, (0,0))
        for i in range(len(self.tile_map)):
            screen.blit(self.tile_map[i][0], self.tile_map[i][1])
        
        
    