import pygame
import random
from DamageText import DamageText

class Fighter():
    def __init__(self, x, y, name, max_hp, strength, potions):
        self.name = name
        self.max_hp = max_hp
        self.hp = max_hp
        self.strength = strength
        self.start_potions = potions
        self.potions = potions
        self.alive = True
        self.animation_list = []
        self.frame_index = 0 
        self.action = 0     # 0 is idle, 1 is attack, 2 is hurt, 3 is death
        self.update_time = pygame.time.get_ticks()
        self.damage_text_group = pygame.sprite.Group()

        #idle images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"Assets/images/{self.name}/idle/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            temp_list.append(img)
        self.animation_list.append(temp_list)


        #attack images
        temp_list = []
        for i in range(8):
            img = pygame.image.load(f"Assets/images/{self.name}/attack/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #hurt images
        temp_list = []
        for i in range(3):
            img = pygame.image.load(f"Assets/images/{self.name}/hurt/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            temp_list.append(img)
        self.animation_list.append(temp_list)

        #death images
        temp_list = []
        for i in range(10):
            img = pygame.image.load(f"Assets/images/{self.name}/death/{i}.png").convert_alpha()
            img = pygame.transform.scale(img, (img.get_width()*3, img.get_height()*3))
            temp_list.append(img)
        self.animation_list.append(temp_list)


        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    
    def update(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]

        #check if enough time has passed since last update
        if (pygame.time.get_ticks() - self.update_time > animation_cooldown):
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1

        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action ==3:
                self.frame_index = len(self.animation_list[self.action])-1
            else:
                self.idle()


    def idle(self):
        self.action =0
        self.frame_index =0
        self.update_time = pygame.time.get_ticks()

    
    def attack (self, target):
        #deal damage to enemy
        rand = random.randint(-5, 5)
        damage = self.strength + rand
        target.hp -= damage
        target.hurt()

        #target die or not
        if target.hp <1:
            target.hp = 0
            target.alive = False
            target.death()

        
        #create damage text
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), (255,0,0))
        self.damage_text_group.add(damage_text)


        #attack animations
        self.action =1
        self.frame_index =0
        self.update_time = pygame.time.get_ticks()


    def hurt(self):
        self.action =2
        self.frame_index =0
        self.update_time = pygame.time.get_ticks()
    
    def death(self):
        self.action =3
        self.frame_index =0
        self.update_time = pygame.time.get_ticks()
    
    def reset(self):
        self.alive = True
        self.potions = self.start_potions
        self.hp = self.max_hp
        self.frame_index =0
        self.action = 0
        self.update_time = pygame.time.get_ticks()
    
    def draw(self, surf):
        surf.blit(self.image, self.rect)