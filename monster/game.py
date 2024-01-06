import pygame
from monster import Monster
import random
from constants import *
class Game:
    def __init__(self, player, monster_group):
        self.score = 0
        self.player = player
        self.monster_group = monster_group
        self.level_number = 0
        self.font = pygame.font.Font("assets/Abrushow.ttf", 28)
        self.all_images = []
        blue_monster = pygame.image.load("assets/blue_monster.png")
        green_monster = pygame.image.load("assets/green_monster.png")
        orange_monster = pygame.image.load("assets/orange_monster.png")
        purple_monster = pygame.image.load("assets/purple_monster.png")
        self.all_images = [blue_monster, green_monster, orange_monster,
                    purple_monster]
        
        self.target_monster_type = random.randint(0,3)
        self.target_monster_image = self.all_images[self.target_monster_type]
        self.target_monster_rect = self.target_monster_image.get_rect(centerx = WINDOW_WIDTH/2, bottom = 100)
    def start_new_level(self):
        self.level_number += 1
        for i in range(self.level_number):
            for i in range(4):
                Monster(random.randint(0, WINDOW_WIDTH-64), 
                        random.randint(100, WINDOW_HEIGHT-164),
                        self.all_images[i],
                        self.monster_group,
                        i
                        )
    
    
    
    def check_collisions(self):
        collided_monster = pygame.sprite.spritecollideany(self.player, self.monster_group)
        if collided_monster:
            if collided_monster.type == self.target_monster_type:
                self.score += 1
                collided_monster.remove(self.monster_group)
                self.player.catch_sound.play()
                if len(self.monster_group):
                    self.change_target()
                else:
                    self.player.reset()
                    self.start_new_level()

            else:
                self.player.lives -= 1
                self.player.reset()
                self.set_dead()              
    def set_dead(self):
        if self.player.lives <= 0:
            self.player.alive = False
    def game_over(self, screen, running):
        game_over_text = self.font.render("Game Over, Press Enter to play again", True, (190,10,230))
        game_over_rect = game_over_text.get_rect()
        game_over_rect.center = (WINDOW_WIDTH/2, WINDOW_HEIGHT/2)
        screen.fill((0,0,0))
        self.draw(screen)
        screen.blit(game_over_text, game_over_rect)
        pygame.display.update()
        paused = True
        while paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        paused = False
                        self.score = 0
                        self.player.lives = 3
                        self.player.alive = True
                        self.monster_group.empty()
                        self.level_number = 0
                        self.start_new_level()
                if event.type == pygame.QUIT:
                    paused = False
                    running = False
        return running




    def change_target(self):
        new_target = random.choice(self.monster_group.sprites())
        self.target_monster_image = new_target.image
        self.target_monster_type = new_target.type

    
    def draw(self,screen):
        score_text = self.font.render(f'Score:{self.score}', True, (247, 13,168))
        score_rect = score_text.get_rect(topleft = (10, 10))
        screen.blit(score_text, score_rect)
        screen.blit(self.target_monster_image, self.target_monster_rect)

        lives_text = self.font.render(f"Lives {self.player.lives}", True, (247, 13,168))
        lives_rect = lives_text.get_rect(topright=(WINDOW_WIDTH, 10))
        screen.blit(lives_text, lives_rect)
        #TODO  نمایش شماره مرحله بازیکن در صفحه
        # TODO   اضافه کردن gameover  به بازی
   



        pygame.draw.rect(screen, (247, 13,168), (0,100,WINDOW_WIDTH, WINDOW_HEIGHT-200),4)
