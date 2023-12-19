import pygame
import random
import button

pygame.init()

#setting the frame rate
clock = pygame.time.Clock()
fps = 60

#creating screen display
bottom_panel = 150
screen_width = 800
screen_height = 400 + bottom_panel
screen = pygame.display.set_mode((screen_width, screen_height))


#the game title
pygame.display.set_caption('Game')


#game variable
current_fighter = 1
total_fighters = 3
action_cooldown = 0
action_waittime = 90
attack = False
potion = False
potion_effect =15
click = False
game_over = 0



#images
bg_image = pygame.image.load("Assets/images/background/background.png").convert_alpha()
panel_image = pygame.image.load("Assets/images/icon/panel.png").convert_alpha()
sword_image = pygame.image.load("Assets/images/icon/sword.png").convert_alpha()
potion_img = pygame.image.load("Assets/images/icon/potion.png").convert_alpha()
victory_img = pygame.image.load("Assets/images/icon/victory.png").convert_alpha()
defeat_img = pygame.image.load("Assets/images/icon/defeat.png").convert_alpha()
restart_img = pygame.image.load("Assets/images/icon/restart.png").convert_alpha()

#text
font = pygame.font.SysFont('Times New Roman', 26)
red = (255,0,0)
green = (0,255,0)


def draw_bg():
    screen.blit(bg_image,(0,0))

def draw_panel():
    #draw panel rectangle
    screen.blit(panel_image, (0, screen_height - bottom_panel))
    #show knight stats
    draw_text(f'{knight.name} HP: {knight.hp}', font, red, 100, screen_height-bottom_panel+10)
    #show bandit stats
    for count, i in enumerate(bandit_list):
        draw_text(f'{i.name} HP: {i.hp}', font, red, 550, screen_height-bottom_panel+10 + count*60)

def draw_text (text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))



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
        if (pygame.time.get_ticks() - self.update_time > 100):
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
        damage_text = DamageText(target.rect.centerx, target.rect.y, str(damage), red)
        damage_text_group.add(damage_text)


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
    
    def draw(self):
        screen.blit(self.image, self.rect)



class HealthBar():
    def __init__(self, x, y, hp, max_hp):
        self.x = x 
        self.y = y
        self.hp = hp
        self.max_hp = max_hp
    
    def draw (self, hp):
        #update hp as game progress
        self.hp = hp
        #calculate health ratio
        ratio = self.hp / self.max_hp

        pygame.draw.rect(screen, red, (self.x, self.y, 150, 20))
        pygame.draw.rect(screen, green, (self.x, self.y, 150*ratio, 20))


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(damage, True, colour)
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.counter=0

    def update(self):
        #move damage text up
        self.rect.y -= 1
        #delete text after few seconds
        self.counter +=1
        if self.counter > 30:
            self.kill()

damage_text_group = pygame.sprite.Group()


knight = Fighter(200, 260, 'Warrior', 30, 10, 3)
bandit1 = Fighter(550, 270, 'Bandit', 2, 6, 1)
bandit2 = Fighter(700, 270, 'Bandit', 2, 6, 1)

bandit_list = []
bandit_list.append(bandit1)
bandit_list.append(bandit2)


knight_health_bar = HealthBar(100, screen_height - bottom_panel + 40, knight.hp, knight.max_hp)
bandit1_health_bar = HealthBar(550, screen_height - bottom_panel + 40, bandit1.hp, bandit1.max_hp)
bandit2_health_bar = HealthBar(550, screen_height - bottom_panel + 100, bandit2.hp, bandit2.max_hp)


#create button
potion_button = button.Button(screen, 100, screen_height-bottom_panel+70, potion_img, 64,64)
restart_button = button.Button(screen, 330, 120, restart_img, 120, 30)

#game loop
run = True
while run:

    #setting up the frame rate
    clock.tick(fps)

    draw_bg()
    draw_panel()
    knight_health_bar.draw(knight.hp)
    bandit1_health_bar.draw(bandit1.hp)
    bandit2_health_bar.draw(bandit2.hp)


    knight.draw()
    knight.update()
    for bandit in bandit_list:
        bandit.draw()
        bandit.update()


    #draw damage text
    damage_text_group.update()
    damage_text_group.draw(screen)

    
    #control player action
    #reset action variable
    attack = False
    potion = False
    target = None
    pygame.mouse.set_visible(True)
    pos = pygame.mouse.get_pos()

    for count, bandit in enumerate(bandit_list):
        if bandit.rect.collidepoint(pos):
            #hide mouse
            pygame.mouse.set_visible(False)
            #show sword
            screen.blit(sword_image, pos)

            if click == True and bandit.alive==True:
                attack = True
                target = bandit_list[count]


    #button click 
    if potion_button.draw():
        potion = True
    #show number potion remaining
    draw_text(str(knight.potions), font, red, 150, screen_height -bottom_panel+70)
    

    if game_over == 0:
        #player action 
        if knight.alive == True:
            if current_fighter == 1:
                action_cooldown +=1
                if action_cooldown >= action_waittime:
                    if attack ==True and target != None:
                        knight.attack(target)
                        current_fighter += 1
                        action_cooldown=0

                    if potion == True:
                        if knight.potions >0:
                            if knight.max_hp > knight.hp + potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = knight.max_hp - knight.hp
                        knight.hp += heal_amount
                        knight.potions -=1
                        damage_text = DamageText(knight.rect.centerx, knight.rect.y, str(heal_amount), green)
                        damage_text_group.add(damage_text)
                        current_fighter += 1
                        action_cooldown=0
        else:
            game_over = -1


        #enemy action 
        for count,bandit in enumerate(bandit_list):
            #bandit 1 = current fighter 2, bandit 2 = current fighter 3
            if current_fighter == 2 + count:
                if bandit.alive ==True:
                    action_cooldown +=1
                    if action_cooldown >= action_waittime:
                        #check if bandit need heal
                        if(bandit.hp / bandit.max_hp < 0.5 and bandit.potions>0):
                            if bandit.max_hp > bandit.hp + potion_effect:
                                heal_amount = potion_effect
                            else:
                                heal_amount = bandit.max_hp - bandit.hp
                            bandit.hp += heal_amount
                            bandit.potions -=1
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(heal_amount), green)
                            damage_text_group.add(damage_text)
                            current_fighter += 1
                            action_cooldown=0

                        #attack
                        else:
                            bandit.attack(knight)
                            current_fighter += 1
                            action_cooldown = 0
                else:
                    current_fighter += 1


        #if all fighter have had turn, then reset
        if current_fighter > total_fighters:
            current_fighter = 1
    
    
    #check if all bandits are death
    alive_bandits =0
    for bandit in bandit_list:
        if bandit.alive == True:
            alive_bandits+=1
    if alive_bandits == 0:
        game_over = 1
    

    #check if game is over
    if game_over != 0:
        if game_over == 1:
            screen.blit(victory_img, (250,50))
        elif game_over == -1:
            screen.blit(defeat_img, (290,50))
        if restart_button.draw():
            knight.reset()
            for bandit in bandit_list:
                bandit.reset()
            current_fighter =1
            action_cooldown = 0
            game_over = 0


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            click = True
        else:
            click = False

    pygame.display.update()


pygame.quit()
