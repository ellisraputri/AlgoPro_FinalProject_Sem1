import pygame
from DamageText import DamageText

class GameFunctions1():
    def __init__(self):
        #game variable
        self.current_fighter = 1
        self.total_fighters = 3
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
    
    def attack_bandit(self, bandit_list):
        for count, bandit in enumerate(bandit_list):
            if bandit.rect.collidepoint(self.pos):
                if self.click == True and bandit.alive==True:
                    self.attack = True
                    self.target = bandit_list[count]
    
    def player_action(self, knight):
        if knight.alive == True:
            if self.current_fighter == 1:
                self.action_cooldown +=1
                if self.action_cooldown >= self.action_waittime:
                    if self.attack ==True and self.target != None:
                        knight.attack(self.target)
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
                        damage_text = DamageText(knight.rect.centerx, knight.rect.y, str(self.heal_amount), (0,255,0))
                        self.damage_text_group.add(damage_text)
                        self.current_fighter += 1
                        self.action_cooldown=0
        else:
            self.game_over = -1
        

    def bandit_action(self, bandit_list, knight):
        for count,bandit in enumerate(bandit_list):
            #bandit 1 = current fighter 2, bandit 2 = current fighter 3
            if self.current_fighter == 2 + count:
                if bandit.alive ==True:
                    self.action_cooldown +=1
                    if self.action_cooldown >= self.action_waittime:
                        #check if bandit need heal
                        if(bandit.hp / bandit.max_hp < 0.5 and bandit.potions>0):
                            if bandit.max_hp > bandit.hp + self.potion_effect:
                                self.heal_amount = self.potion_effect
                            else:
                                self.heal_amount = bandit.max_hp - bandit.hp
                            bandit.hp += self.heal_amount
                            bandit.potions -=1
                            damage_text = DamageText(bandit.rect.centerx, bandit.rect.y, str(self.heal_amount), (0,255,0))
                            self.damage_text_group.add(damage_text)
                            self.current_fighter += 1
                            self.action_cooldown=0

                        #attack
                        else:
                            bandit.attack(knight)
                            self.current_fighter += 1
                            self.action_cooldown = 0
                else:
                    self.current_fighter += 1
    
    def check_turn(self):
        #if all fighter have had turn, then reset
        if self.current_fighter > self.total_fighters:
            self.current_fighter = 1
    
    def check_bandit_alive(self, bandit_list):
        self.alive_bandits =0
        for bandit in bandit_list:
            if bandit.alive == True:
                self.alive_bandits+=1
        if self.alive_bandits == 0:
            self.game_over = 1
    
    