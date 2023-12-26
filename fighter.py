import pygame
import random

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

        if self.name == 'Boy':
            #idle images
            temp_list = []
            for i in range(6):
                img = pygame.image.load(f"Assets/images/{self.name}/Idle/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4.5, img.get_height()*4.5))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #attack images
            temp_list = []
            for i in range(8):
                img = pygame.image.load(f"Assets/images/{self.name}/Attack/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4.5, img.get_height()*4.5))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #hurt images
            temp_list = []
            for i in range(4):
                img = pygame.image.load(f"Assets/images/{self.name}/Hurt/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4.5, img.get_height()*4.5))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #death images
            temp_list = []
            for i in range(12):
                img = pygame.image.load(f"Assets/images/{self.name}/Death/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4.5, img.get_height()*4.5))
                temp_list.append(img)
            self.animation_list.append(temp_list)


        elif self.name == 'Wolf1' or self.name =='Wolf2' or self.name =='Wolf3':
            #idle images
            temp_list = []
            for i in range(8):
                img = pygame.image.load(f"Assets/images/{self.name}/Idle/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*1.7, img.get_height()*1.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #attack images
            temp_list = []
            for i in range(6):
                img = pygame.image.load(f"Assets/images/{self.name}/Attack/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*1.7, img.get_height()*1.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #hurt images
            temp_list = []
            for i in range(2):
                img = pygame.image.load(f"Assets/images/{self.name}/Hurt/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*1.7, img.get_height()*1.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #death images
            temp_list = []
            for i in range(2):
                img = pygame.image.load(f"Assets/images/{self.name}/Death/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*1.7, img.get_height()*1.7))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        

        elif self.name == 'Man':
            #idle images
            temp_list = []
            for i in range(5):
                img = pygame.image.load(f"Assets/images/{self.name}/Idle/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*2, img.get_height()*2))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #attack images
            temp_list = []
            for i in range(5):
                img = pygame.image.load(f"Assets/images/{self.name}/Attack/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*2, img.get_height()*2))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #hurt images
            temp_list = []
            for i in range(2):
                img = pygame.image.load(f"Assets/images/{self.name}/Hurt/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*2, img.get_height()*2))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #death images
            temp_list = []
            for i in range(8):
                img = pygame.image.load(f"Assets/images/{self.name}/Death/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*2, img.get_height()*2))
                temp_list.append(img)
            self.animation_list.append(temp_list)
        

        elif self.name == 'Vampire':
            #idle images
            temp_list = []
            for i in range(5):
                img = pygame.image.load(f"Assets/images/{self.name}/Idle/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4, img.get_height()*4))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #attack images
            temp_list = []
            for i in range(6):
                img = pygame.image.load(f"Assets/images/{self.name}/Attack/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4, img.get_height()*4))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #hurt images
            temp_list = []
            for i in range(2):
                img = pygame.image.load(f"Assets/images/{self.name}/Hurt/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4, img.get_height()*4))
                temp_list.append(img)
            self.animation_list.append(temp_list)

            #death images
            temp_list = []
            for i in range(8):
                img = pygame.image.load(f"Assets/images/{self.name}/Death/{i}.png").convert_alpha()
                img = pygame.transform.scale(img, (img.get_width()*4, img.get_height()*4))
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
        damage = abs(self.strength + rand)
        target.hp -= damage
        target.hurt()

        #target die or not
        if target.hp <1:
            target.hp = 0
            target.alive = False
            target.death()


        #attack animations
        self.action =1
        self.frame_index =0
        self.update_time = pygame.time.get_ticks()

        return damage


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