import pygame
from DamageText import DamageText
from finding_object_thing import Things, ThingsInList

class GameFunctions1():
    def __init__(self, total_fighters):
        #game variable
        self.current_fighter = 1
        self.total_fighters = total_fighters
        self.action_cooldown = 0
        self.action_waittime = 90
        self.attack = False
        self.potion = False
        self.potion_effect =15
        self.click = False
        self.game_over = 0
        self.damage_text_group = pygame.sprite.Group()
        self.game_over = 0
    
    def reset_state(self):
        self.attack = False
        self.potion = False
        self.target = None
        pygame.mouse.set_visible(True)
        self.pos = pygame.mouse.get_pos()
    
    def attack_enemy(self, enemy_list):
        for count, enemy in enumerate(enemy_list):
            if enemy.rect.collidepoint(self.pos):
                if self.click == True and enemy.alive==True:
                    self.attack = True
                    self.target = enemy_list[count]
    
    def player_action(self, knight):
        if knight.alive == True:
            if self.current_fighter == 1:
                self.action_cooldown +=1
                if self.action_cooldown >= self.action_waittime:
                    if self.attack ==True and self.target != None:
                        damage = knight.attack(self.target)

                        #create damage text
                        damage_text = DamageText(self.target.rect.centerx, self.target.rect.centery-40, str(damage), (255,0,0))
                        self.damage_text_group.add(damage_text)

                        #go to next turn
                        self.current_fighter += 1
                        self.action_cooldown=0

                    if self.potion == True:
                        if knight.potions >0:
                            if knight.max_hp > knight.hp + self.potion_effect:
                                self.heal_amount = self.potion_effect
                            else:
                                self.heal_amount = knight.max_hp - knight.hp
                        knight.hp += self.heal_amount
                        knight.potions -=1
                        damage_text = DamageText(knight.rect.centerx, knight.rect.centery-40, str(self.heal_amount), (0,255,0))
                        self.damage_text_group.add(damage_text)
                        self.current_fighter += 1
                        self.action_cooldown=0
        else:
            self.game_over = -1
        

    def enemy_action(self, enemy_list, knight):
        for count,enemy in enumerate(enemy_list):
            #enemy 1 = current fighter 2, enemy 2 = current fighter 3
            if self.current_fighter == 2 + count:
                if enemy.alive ==True:
                    self.action_cooldown +=1
                    if self.action_cooldown >= self.action_waittime:
                        #check if enemy need heal
                        if(enemy.hp / enemy.max_hp < 0.5 and enemy.potions>0):
                            if enemy.max_hp > enemy.hp + self.potion_effect:
                                self.heal_amount = self.potion_effect
                            else:
                                self.heal_amount = enemy.max_hp - enemy.hp
                            enemy.hp += self.heal_amount
                            enemy.potions -=1
                            damage_text = DamageText(enemy.rect.centerx, enemy.rect.centery -40, str(self.heal_amount), (0,255,0))
                            self.damage_text_group.add(damage_text)
                            self.current_fighter += 1
                            self.action_cooldown=0

                        #attack
                        else:
                            damage = enemy.attack(knight)

                            #create damage text
                            damage_text = DamageText(knight.rect.centerx, knight.rect.centery -40, str(damage), (255,0,0))
                            self.damage_text_group.add(damage_text)

                            self.current_fighter += 1
                            self.action_cooldown = 0
                else:
                    self.current_fighter += 1
    
    def check_turn(self):
        #if all fighter have had turn, then reset
        if self.current_fighter > self.total_fighters:
            self.current_fighter = 1
    
    def check_enemy_alive(self, enemy_list):
        self.alive_enemies =0
        for enemy in enemy_list:
            if enemy.alive == True:
                self.alive_enemies+=1
        if self.alive_enemies == 0:
            self.game_over = 1
    

class GameFunctions2():
    def __init__(self, images_bg, images_scroll_list):
        #dealing with objects in the background
        self.position_dict = {1: (187,100), 2:(660, 180), 3:(60,40), 4:(430,400), 5:(370,380), 6:(600,540), 7:(20,610), 8:(430, 80), 9:(360,600)}
        self.objects_in_bg = pygame.sprite.Group()
        for count,object_image in enumerate(images_bg):
            image = Things(self.position_dict[count+1][0], self.position_dict[count+1][1], object_image, count)
            self.objects_in_bg.add(image)

        #dealing with objects in the scroll list
        self.objects_in_list = pygame.sprite.Group()
        self.tracker = 0     #to track the index of the images
        self.y_pos = 220
        for i in range(3):
            self.x_pos = 750
            #for every three image, enter to a new line (have a new y-position)
            for j in range(3):
                image = ThingsInList(self.x_pos, self.y_pos, images_scroll_list[self.tracker], self.tracker)
                self.objects_in_list.add(image)
                self.x_pos += 100
                self.tracker += 1
            self.y_pos += 120

        #keep track of number of object being found
        self.found = 0

        #if all things have been found
        self.text_complete = ["NICE!", " ", "Press space", "to continue"]


    def check_clicked(self, event):
        #check if the object in the background is being clicked or not  
        for obj_in_bg in self.objects_in_bg:
            if obj_in_bg.rect.collidepoint(event.pos):
                obj_in_bg.kill()

                #if object in the background is clicked, then remove the same object from the scroll list
                for obj_in_list in self.objects_in_list:
                    if obj_in_bg.index == obj_in_list.index:
                        obj_in_list.kill()

                #increase number of object being found
                self.found += 1