import pygame
import sys
from fighter import Fighter
from button import Button
from healthbar import HealthBar
from img_text_display import Displaying
from game_function1 import GameFunctions1
from running_text import DialogText

pygame.init()

#setting the frame rate
clock = pygame.time.Clock()
fps = 60

#display
screen = pygame.display.set_mode((1000, 650))
displays = Displaying()

#the game title
pygame.display.set_caption('Game')

#click function
clickk = False

def main_menu():
    click = False
    while True:
        pygame.mouse.set_visible(True)

        #draw the background image and logo
        displays.draw_bg(screen, displays.bg_main)
        displays.draw_buttons(screen, displays.main_logo, 500, 150)

        #get position of mouse
        mx, my = pygame.mouse.get_pos()

        #making the images become rect
        new_game_rect = displays.new_game_img.get_rect(center= (520, 320))
        continue_game_rect = displays.continue_game_img.get_rect(center= (520,440))
        exit_game_rect = displays.exit_img.get_rect(center =(520,560))

        #checking mouse collisions
        if new_game_rect.collidepoint((mx, my)):
            if click:
                scene_one()
        if continue_game_rect.collidepoint((mx, my)):
            if click:
                pass
        if exit_game_rect.collidepoint((mx, my)):
            if click:
                pygame.quit()
                sys.exit()

        #drawing the buttons
        pygame.draw.rect(screen, (89,66,40), new_game_rect)
        screen.blit(displays.new_game_img, new_game_rect)
        pygame.draw.rect(screen, (89,66,40), continue_game_rect)
        screen.blit(displays.continue_game_img, continue_game_rect)
        pygame.draw.rect(screen, (89,66,40), exit_game_rect)
        screen.blit(displays.exit_img, exit_game_rect)

        #event checker 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(fps)


def scene_one():
    myfile=open('dialog1_text.txt','rt')
    all=myfile.readlines()

    dialog1 = DialogText(displays.font, all)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene1_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        dialog1.running_message(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog1.checking_message_done()
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog1.checking_message_done()
        
        
        
        pygame.display.update()
    pygame.quit()




def game_one():
    #game function
    game1 = GameFunctions1()


    #create fighter
    knight = Fighter(200, 260, 'Warrior', 30, 10, 3)
    bandit1 = Fighter(550, 270, 'Bandit', 20, 6, 1)
    bandit2 = Fighter(700, 270, 'Bandit', 20, 6, 1)

    bandit_list = []
    bandit_list.append(bandit1)
    bandit_list.append(bandit2)

    knight_health_bar = HealthBar(100, displays.screen_height - displays.bottom_panel + 40, knight.hp, knight.max_hp)
    bandit1_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 40, bandit1.hp, bandit1.max_hp)
    bandit2_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 100, bandit2.hp, bandit2.max_hp)


    #create button
    potion_button = Button(screen, 100, displays.screen_height-displays.bottom_panel+70, displays.potion_img, 64,64)
    restart_button = Button(screen, 330, 120, displays.restart_img, 120, 30)

    #game loop
    run = True
    while run:
        #setting up the frame rate
        clock.tick(fps)

        #draw background and panel
        displays.draw_bg(screen, displays.bg_image)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, knight, bandit_list)

        #draw healthbar 
        knight_health_bar.draw(knight.hp, screen)
        bandit1_health_bar.draw(bandit1.hp, screen)
        bandit2_health_bar.draw(bandit2.hp, screen)

        #draw knight
        knight.draw(screen)
        knight.update()

        #draw bandit
        for bandit in bandit_list:
            bandit.draw(screen)
            bandit.update()


        #draw damage text
        game1.damage_text_group.update()
        game1.damage_text_group.draw(screen)

        
        #control player action
        #reset action variable
        game1.reset_state()

        game1.attack_bandit(bandit_list)
        for bandit in bandit_list:
            if bandit.rect.collidepoint(game1.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game1.pos)

    
        #displaying potion button
        #button click 
        if potion_button.draw():
            game1.potion = True
        #show number potion remaining
        displays.draw_text(str(knight.potions), displays.font, (255,0,0), 150, displays.screen_height -displays.bottom_panel+70, screen, 40)
        

        if game1.game_over == 0:
            #player action 
            game1.player_action(knight)

            #enemy action 
            game1.bandit_action(bandit_list, knight)

            #check all action
            game1.check_turn()
        
        
        #check if all bandits are death
        game1.check_bandit_alive(bandit_list)


        #check if game is over
        if game1.game_over != 0:
            if game1.game_over == 1:
                displays.draw_victory(screen)
            elif game1.game_over == -1:
                displays.draw_defeat(screen)
            if restart_button.draw():
                knight.reset()
                for bandit in bandit_list:
                    bandit.reset()
                game1.current_fighter =1
                game1.action_cooldown = 0
                game1.game_over = 0



        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game1.click = True
            else:
                game1.click = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


main_menu()

pygame.quit()
