#this file is used to simplify the game function used in the main file

import pygame
from button import Button
import sys
import img_text_display
from running_text import DialogText
from img_text_display import FadeTransition
from game_function1 import GameFunctions1, GameFunctions2
from damage_and_healthbar import HealthBar
from fighter import Fighter

def play_bgm(music_now):
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.fadeout(500)
        pygame.mixer.music.unload()

    pygame.mixer.music.load(music_now)
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(loops = -1)


def mainmenu(screen, scene_one, clock, fps, new_game_img, continue_game_img, exit_img, current_state):
    pygame.mouse.set_visible(True)

    #initializing each button
    new_game = Button(screen, 520, 320, new_game_img, 300, 100)
    continue_game = Button(screen, 520, 440, continue_game_img, 300, 100)
    exit_game = Button(screen, 520,560, exit_img, 300, 100)

    #each button click
    if new_game.draw():
        scene_one()

    elif continue_game.draw():
        current_state()

    elif exit_game.draw():
        pygame.quit()
        sys.exit()

    #event checker 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(fps)


class Scene():
    def __init__(self, file_path, index, font, next_state, screen_width, screen_height):
        self.skip = False
        self.scene_done = False
        myfile=open(file_path,'rt')
        all=myfile.readlines()

        self.dialog = DialogText(font, all)
        self.transition = FadeTransition(next_state, screen_width, screen_height)

        self.run = True
        self.index = index
        self.end_msg_index = [18, 12, 16, 14, 23, 13]
    
    def running(self, clock, fps, screen, skip_image, icon1, icon1_text, icon2, icon2_text, main_menu, additional_icon):
        clock.tick(fps)

        #run the message
        self.dialog.running_message(screen)

        #show character in corresponding part of story
        if self.index == 1:
            self.dialog.scene_1_function(icon1, icon1_text, icon2, icon2_text, additional_icon, screen)
        elif self.index == 2:
            self.dialog.scene_2_function(icon1, icon1_text, additional_icon, screen)
        elif self.index == 3:
            self.dialog.scene_3_function(icon1, icon1_text, icon2, icon2_text, screen)
        elif self.index ==4:
            self.dialog.scene_4_function(icon1, icon1_text, icon2, icon2_text, screen)
        elif self.index ==5:
            self.dialog.scene_5_function(icon1, icon1_text, icon2, icon2_text, screen)
        elif self.index == 6:
            self.dialog.scene_6_function(icon1, icon1_text, screen)
        
        #draw skip button
        skip_button = Button(screen, 820, 50, skip_image, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if self.skip or self.scene_done:
            self.transition.running()

        #event checker
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    self.dialog.checking_message_done(self.index)
                    if(self.dialog.active_message == self.end_msg_index[self.index-1]):
                        self.scene_done = True
                        self.dialog.type_sound.stop()
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    self.skip=True
                    self.dialog.type_sound.stop()
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.dialog.checking_message_done(self.index)
                    if(self.dialog.active_message == self.end_msg_index[self.index-1]):
                        self.scene_done = True
                        self.dialog.type_sound.stop()
        
        pygame.display.update()


class GameInstruction():
    def __init__(self, next_state, screen_width, screen_height):
        self.scene_done = False
        self.all1=["Game Instructions:", "1. Click on the enemies to attack them.", "2. Click on the potion button to heal.",
            "3. Choose between attack or heal in each turn.", "4. Be careful and good luck!", " ", "Press space to continue"]
        self.all2 = ["Game Instructions:", "Find the object based on the scroll."," ", "Press space to continue"]
        self.all3 = ["Thank you for playing!", "", "Press space to return to the main menu"]
        self.transition = FadeTransition(next_state, screen_width, screen_height)
        self.run = True
    
    def running(self, clock, fps, main_menu):
        clock.tick(fps)

        if self.scene_done:
            self.transition.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                sys.exit()
            
            #press space to move on 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        
        pygame.display.update()


class Game():
    def __init__(self, screen, boy_x, boy_y, enemy1_x, enemy1_y, enemy_name, enemy_hp, enemy_strength, enemy_potions, enemy_number, screen_height, bottom_panel, potion_img, restart_img, next_stage_img):
        #game function
        self.game = GameFunctions1(enemy_number + 1)

        #create boy
        self.knight = Fighter(boy_x, boy_y, 'Boy', 30, 12, 3)

        #create enemy
        self.enemy_list = []
        for i in range (enemy_number):
            enemy = Fighter(enemy1_x, enemy1_y, enemy_name, enemy_hp, enemy_strength, enemy_potions)
            self.enemy_list.append(enemy)
            enemy1_x += 150

        #create health bar for boy
        self.knight_health_bar = HealthBar(70, screen_height - bottom_panel + 40, self.knight.hp, self.knight.max_hp)

        #create health bar for enemy
        self.enemy_healthbar_list = []
        for j in range (enemy_number):
            enemy_healthbar = HealthBar(550, (screen_height - bottom_panel + 40 + 60*j), self.enemy_list[j].hp, self.enemy_list[j].max_hp)
            self.enemy_healthbar_list.append(enemy_healthbar)

        #create button
        self.potion_button = Button(screen, 100, screen_height-bottom_panel+105, potion_img, 64,64)
        self.restart_button = Button(screen, 500, 110, restart_img, 120, 30)
        self.next_stage_button = Button(screen, 500, 122, next_stage_img, 160, 40)

        #game loop
        self.run = True

        #sound effects
        self.victory_sfx = pygame.mixer.Sound("Assets/audio/sfx/victory.wav")
        self.victory_sfx.set_volume(0.7)
        self.defeat_sfx = pygame.mixer.Sound("Assets/audio/sfx/defeat.wav")
        self.defeat_sfx.set_volume(0.7)
        self.play_sound = False     #to ensure the sound only play once


    def running(self, clock, fps, screen):
        #frame rate
        clock.tick(fps)

        #draw healthbar for boy
        self.knight_health_bar.draw(self.knight.hp, screen)

        #draw healthbar for enemy
        index = 0
        for enemy_healthbar in self.enemy_healthbar_list:
            enemy_healthbar.draw(self.enemy_list[index].hp, screen)
            index += 1

        #draw knight
        self.knight.draw(screen)
        self.knight.update()

        #draw enemy
        for enemy in self.enemy_list:
            enemy.draw(screen)
            enemy.update()

        #draw damage text
        self.game.damage_text_group.update()
        self.game.damage_text_group.draw(screen)
        

    def check_game_state(self,screen, victory_img, defeat_img, next_state, main_menu):
        #displaying potion button
        #button click 
        if self.potion_button.draw():
            self.game.potion = True

        #each player action
        if self.game.game_over == 0:
            #player action 
            self.game.player_action(self.knight)

            #enemy action 
            self.game.enemy_action(self.enemy_list, self.knight)

            #check all action
            self.game.check_turn()
        
        
        #check if all enemies are death
        self.game.check_enemy_alive(self.enemy_list)


        #check if game is over
        if self.game.game_over != 0:
            #if player wins
            if self.game.game_over == 1:
                #draw victory image and show next stage button
                img_text_display.draw_victory_defeat(screen, victory_img, 500, 60)
                if self.next_stage_button.draw():
                    next_state()
                
                #play victory music
                if self.play_sound == False:
                    self.victory_sfx.play()
                    self.play_sound = True
                

            #if enemy wins
            elif self.game.game_over == -1:
                #play defeat music
                if self.play_sound == False:
                    self.defeat_sfx.play()
                    self.play_sound = True

                #draw defeat image, show restart button, and reset all the stats
                img_text_display.draw_victory_defeat(screen, defeat_img, 500, 60)
                if self.restart_button.draw():
                    self.knight.reset()
                    for enemy in self.enemy_list:
                        enemy.reset()
                    self.game.current_fighter =1
                    self.game.action_cooldown = 0
                    self.game.game_over = 0
                    self.play_sound = False
                

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.game.click = True
            else:
                self.game.click = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()
    

class FindObject():
    def __init__(self, next_state, screen_width, screen_height, object_images_in_bg, object_images):
        self.scene_done = False
        self.transition = FadeTransition(next_state, screen_width, screen_height)
        self.run = True
        self.gamef = GameFunctions2(object_images_in_bg, object_images)

        #sound effects
        self.success_sfx = pygame.mixer.Sound("Assets/audio/sfx/findobj_success.wav")
        self.success_sfx.set_volume(0.4)
        self.play_sound = False     #ensure the sfx only play once
    
    def running(self, clock, fps, screen, main_menu):
        #frame rate
        clock.tick(fps)

        #draw object in background and object in scroll list
        self.gamef.objects_in_bg.draw(screen)
        self.gamef.objects_in_list.draw(screen)

        #when all of the objects have been found
        text_y = 280
        if self.gamef.found == 9:
            for text in self.gamef.text_complete:
                img_text_display.draw_text_complete(text, 'black', 850, text_y, screen, 60)
                text_y += 40

                #play success sound
                if self.play_sound == False:
                    self.success_sfx.play()
                    self.play_sound = True

        if self.scene_done:
            self.transition.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run = False
                sys.exit()
            
            #press space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.gamef.check_clicked(event)
                        
        pygame.display.update()
        
