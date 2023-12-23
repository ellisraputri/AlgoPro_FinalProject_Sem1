import pygame
import sys
from fighter import Fighter
from button import Button
from healthbar import HealthBar
from img_text_display import Displaying, FadeTransition
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
                game_one()
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        clock.tick(fps)


def scene_one():
    skip = False
    scene_done = False
    myfile=open('dialog1_text.txt','rt')
    all=myfile.readlines()

    dialog1 = DialogText(displays.font, all)
    transition1 = FadeTransition(game_instruction, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene1_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #run the message
        dialog1.running_message(screen)

        #show character in corresponding part of story
        dialog1.scene_1_function(displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition1.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog1.checking_message_done()
                    if(dialog1.active_message == 17):
                        scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    skip=True
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog1.checking_message_done()
        
        pygame.display.update()
    pygame.quit()


def game_instruction():
    scene_done = False
    all=["Game Instructions:", "1. Click on the enemies to attack them.", "2. Click on the potion button to heal.",
            "3. Be careful not to die.", "4. Good luck!", " ", "Press space to continue"]
    transition1 = FadeTransition(game_one, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene1_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 0, 1000, 650])

        height = 120
        for i in all:
            displays.draw_text(i, displays.font, (255,255,255), 500, height, screen, 60)
            height+=60

        if scene_done:
            transition1.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        
        pygame.display.update()
    pygame.quit()


def game_one():
    #game function
    game1 = GameFunctions1()

    #create fighter
    knight = Fighter(270, 300, 'Boy', 30, 10, 3)
    wolf1_1 = Fighter(650, 310, 'Wolf1', 15, 3, 0)
    wolf1_2 = Fighter(800, 310, 'Wolf1', 15, 3, 0)

    wolf1_list = []
    wolf1_list.append(wolf1_1)
    wolf1_list.append(wolf1_2)

    knight_health_bar = HealthBar(70, displays.screen_height - displays.bottom_panel + 40, knight.hp, knight.max_hp)
    wolf1_1_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 40, wolf1_1.hp, wolf1_1.max_hp)
    wolf1_2_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 100, wolf1_2.hp, wolf1_2.max_hp)

    #create button
    potion_button = Button(screen, 100, displays.screen_height-displays.bottom_panel+105, displays.potion_img, 64,64)
    restart_button = Button(screen, 500, 110, displays.restart_img, 120, 30)
    next_stage_button = Button(screen, 500, 122, displays.next_stage_img, 160, 40)

    #game loop
    run = True
    while run:
        #setting up the frame rate
        clock.tick(fps)

        #draw background and panel
        displays.draw_bg(screen, displays.bg_image)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, knight, wolf1_list)
        displays.draw_buttons(screen, displays.fight1, 870, 50)

        #draw healthbar 
        knight_health_bar.draw(knight.hp, screen)
        wolf1_1_health_bar.draw(wolf1_1.hp, screen)
        wolf1_2_health_bar.draw(wolf1_2.hp, screen)

        #draw knight
        knight.draw(screen)
        knight.update()

        #draw enemy
        for wolf1 in wolf1_list:
            wolf1.draw(screen)
            wolf1.update()

        #draw damage text
        game1.damage_text_group.update()
        game1.damage_text_group.draw(screen)

        #control player action
        #reset action variable
        game1.reset_state()

        game1.attack_enemy(wolf1_list)
        for wolf1 in wolf1_list:
            if wolf1.rect.collidepoint(game1.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game1.pos)

        #displaying potion button
        #button click 
        if potion_button.draw():
            game1.potion = True
        #show number potion remaining
        displays.draw_text(str(knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        

        if game1.game_over == 0:
            #player action 
            game1.player_action(knight)

            #enemy action 
            game1.enemy_action(wolf1_list, knight)

            #check all action
            game1.check_turn()
        
        
        #check if all enemies are death
        game1.check_enemy_alive(wolf1_list)


        #check if game is over
        if game1.game_over != 0:
            if game1.game_over == 1:
                displays.draw_buttons(screen, displays.victory_img, 500, 60)
                if next_stage_button.draw():
                    pass

            elif game1.game_over == -1:
                displays.draw_buttons(screen, displays.defeat_img, 500, 60)
                if restart_button.draw():
                    knight.reset()
                    for wolf1 in wolf1_list:
                        wolf1.reset()
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
