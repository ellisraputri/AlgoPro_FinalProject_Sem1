import pygame
import sys
from fighter import Fighter
from button import Button
from healthbar import HealthBar
from img_text_display import Displaying, FadeTransition
from game_function1 import GameFunctions1, GameFunctions2
from running_text import DialogText
from finding_object_thing import Things, ThingsInList

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
    while True:
        pygame.mouse.set_visible(True)

        #draw the background image and logo
        displays.draw_bg(screen, displays.bg_main)
        displays.draw_buttons(screen, displays.main_logo, 500, 150)

        #initializing each button
        new_game = Button(screen, 520, 320, displays.new_game_img, 300, 100)
        continue_game = Button(screen, 520, 440, displays.continue_game_img, 300, 100)
        exit_game = Button(screen, 520,560, displays.exit_img, 300, 100)

        #each button click
        if new_game.draw():
            game_last()
        elif continue_game.draw():
            pass
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
        dialog1.scene_1_function(displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, displays.object_scroll, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition1.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog1.checking_message_done()
                    if(dialog1.active_message == 18):
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
                    if(dialog1.active_message == 18):
                        scene_done = True
        
        pygame.display.update()


def game_instruction():
    scene_done = False
    all=["Game Instructions:", "1. Click on the enemies to attack them.", "2. Click on the potion button to heal.",
            "3. Choose between attack or heal in each turn.", "4. Be careful and good luck!", " ", "Press space to continue"]
    transition2 = FadeTransition(game_one, displays.screen_width, displays.screen_height)

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
            transition2.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        
        pygame.display.update()
    

def game_one():
    #game function
    game1 = GameFunctions1(3)

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
                    game_two()

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


def game_two():
    #game function
    game2 = GameFunctions1(3)

    #create fighter
    knight = Fighter(270, 300, 'Boy', 30, 10, 3)
    wolf2_1 = Fighter(650, 310, 'Wolf2', 15, 4, 1)
    wolf2_2 = Fighter(800, 310, 'Wolf2', 15, 4, 1)

    wolf2_list = []
    wolf2_list.append(wolf2_1)
    wolf2_list.append(wolf2_2)

    knight_health_bar = HealthBar(70, displays.screen_height - displays.bottom_panel + 40, knight.hp, knight.max_hp)
    wolf2_1_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 40, wolf2_1.hp, wolf2_1.max_hp)
    wolf2_2_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 100, wolf2_2.hp, wolf2_2.max_hp)

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
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, knight, wolf2_list)
        displays.draw_buttons(screen, displays.fight2, 870, 50)

        #draw healthbar 
        knight_health_bar.draw(knight.hp, screen)
        wolf2_1_health_bar.draw(wolf2_1.hp, screen)
        wolf2_2_health_bar.draw(wolf2_2.hp, screen)

        #draw knight
        knight.draw(screen)
        knight.update()

        #draw enemy
        for wolf2 in wolf2_list:
            wolf2.draw(screen)
            wolf2.update()

        #draw damage text
        game2.damage_text_group.update()
        game2.damage_text_group.draw(screen)

        #control player action
        #reset action variable
        game2.reset_state()

        game2.attack_enemy(wolf2_list)
        for wolf2 in wolf2_list:
            if wolf2.rect.collidepoint(game2.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game2.pos)

        #displaying potion button
        #button click 
        if potion_button.draw():
            game2.potion = True
        #show number potion remaining
        displays.draw_text(str(knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        

        if game2.game_over == 0:
            #player action 
            game2.player_action(knight)

            #enemy action 
            game2.enemy_action(wolf2_list, knight)

            #check all action
            game2.check_turn()
        
        
        #check if all enemies are death
        game2.check_enemy_alive(wolf2_list)


        #check if game is over
        if game2.game_over != 0:
            if game2.game_over == 1:
                displays.draw_buttons(screen, displays.victory_img, 500, 60)
                if next_stage_button.draw():
                    game_three()

            elif game2.game_over == -1:
                displays.draw_buttons(screen, displays.defeat_img, 500, 60)
                if restart_button.draw():
                    knight.reset()
                    for wolf2 in wolf2_list:
                        wolf2.reset()
                    game2.current_fighter =1
                    game2.action_cooldown = 0
                    game2.game_over = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game2.click = True
            else:
                game2.click = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


def game_three():
    #game function
    game3 = GameFunctions1(3)

    #create fighter
    knight = Fighter(270, 300, 'Boy', 30, 11, 3)
    wolf3_1 = Fighter(650, 310, 'Wolf3', 20, 5, 2)
    wolf3_2 = Fighter(800, 310, 'Wolf3', 20, 5, 1)

    wolf3_list = []
    wolf3_list.append(wolf3_1)
    wolf3_list.append(wolf3_2)

    knight_health_bar = HealthBar(70, displays.screen_height - displays.bottom_panel + 40, knight.hp, knight.max_hp)
    wolf3_1_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 40, wolf3_1.hp, wolf3_1.max_hp)
    wolf3_2_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 100, wolf3_2.hp, wolf3_2.max_hp)

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
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, knight, wolf3_list)
        displays.draw_buttons(screen, displays.fight3, 870, 50)

        #draw healthbar 
        knight_health_bar.draw(knight.hp, screen)
        wolf3_1_health_bar.draw(wolf3_1.hp, screen)
        wolf3_2_health_bar.draw(wolf3_2.hp, screen)

        #draw knight
        knight.draw(screen)
        knight.update()

        #draw enemy
        for wolf3 in wolf3_list:
            wolf3.draw(screen)
            wolf3.update()

        #draw damage text
        game3.damage_text_group.update()
        game3.damage_text_group.draw(screen)

        #control player action
        #reset action variable
        game3.reset_state()

        game3.attack_enemy(wolf3_list)
        for wolf3 in wolf3_list:
            if wolf3.rect.collidepoint(game3.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game3.pos)

        #displaying potion button
        #button click 
        if potion_button.draw():
            game3.potion = True
        #show number potion remaining
        displays.draw_text(str(knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        

        if game3.game_over == 0:
            #player action 
            game3.player_action(knight)

            #enemy action 
            game3.enemy_action(wolf3_list, knight)

            #check all action
            game3.check_turn()
        
        
        #check if all enemies are death
        game3.check_enemy_alive(wolf3_list)


        #check if game is over
        if game3.game_over != 0:
            if game3.game_over == 1:
                displays.draw_buttons(screen, displays.victory_img, 500, 60)
                if next_stage_button.draw():
                    scene_two()

            elif game3.game_over == -1:
                displays.draw_buttons(screen, displays.defeat_img, 500, 60)
                if restart_button.draw():
                    knight.reset()
                    for wolf3 in wolf3_list:
                        wolf3.reset()
                    game3.current_fighter =1
                    game3.action_cooldown = 0
                    game3.game_over = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game3.click = True
            else:
                game3.click = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


def scene_two():
    skip = False
    scene_done = False
    myfile=open('dialog2_text.txt','rt')
    all=myfile.readlines()

    dialog2 = DialogText(displays.font, all)
    transition3 = FadeTransition(scene_three, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene2_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #run the message
        dialog2.running_message(screen)

        #show character in corresponding part of story
        dialog2.scene_2_function(displays.boy_icon, displays.boy_text_icon, displays.castle, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition3.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog2.checking_message_done()
                    if(dialog2.active_message == 12):
                        scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    skip=True
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog2.checking_message_done()
                    if(dialog2.active_message == 12):
                        scene_done = True
        
        pygame.display.update()


def scene_three():
    skip = False
    scene_done = False
    myfile=open('dialog3_text.txt','rt')
    all=myfile.readlines()

    dialog3 = DialogText(displays.font, all)
    transition4 = FadeTransition(game_four, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene3_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #run the message
        dialog3.running_message(screen)

        #show character in corresponding part of story
        dialog3.scene_3_function(displays.boy_icon, displays.boy_text_icon, displays.man_icon, displays.man_text_icon, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition4.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog3.checking_message_done()
                    if(dialog3.active_message == 16):
                        scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    skip=True
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog3.checking_message_done()
                    if(dialog3.active_message == 16):
                        scene_done = True
        
        pygame.display.update()


def game_four():
    #game function
    game4 = GameFunctions1(2)

    #create fighter
    knight = Fighter(240, 320, 'Boy', 30, 11, 3)
    man = Fighter(700, 320, 'Man', 30, 5, 3)

    man_list = []
    man_list.append(man)

    knight_health_bar = HealthBar(70, displays.screen_height - displays.bottom_panel + 40, knight.hp, knight.max_hp)
    man_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 40, man.hp, man.max_hp)
    
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
        displays.draw_bg(screen, displays.scene3_bg)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, knight, man_list)
        displays.draw_buttons(screen, displays.fight4, 870, 50)

        #draw healthbar 
        knight_health_bar.draw(knight.hp, screen)
        man_health_bar.draw(man.hp, screen)

        #draw knight
        knight.draw(screen)
        knight.update()

        #draw enemy
        for mann in man_list:
            mann.draw(screen)
            mann.update()

        #draw damage text
        game4.damage_text_group.update()
        game4.damage_text_group.draw(screen)

        #control player action
        #reset action variable
        game4.reset_state()

        game4.attack_enemy(man_list)
        for mann in man_list:
            if mann.rect.collidepoint(game4.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game4.pos)

        #displaying potion button
        #button click 
        if potion_button.draw():
            game4.potion = True
        #show number potion remaining
        displays.draw_text(str(knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        

        if game4.game_over == 0:
            #player action 
            game4.player_action(knight)

            #enemy action 
            game4.enemy_action(man_list, knight)

            #check all action
            game4.check_turn()
        
        
        #check if all enemies are death
        game4.check_enemy_alive(man_list)


        #check if game is over
        if game4.game_over != 0:
            if game4.game_over == 1:
                displays.draw_buttons(screen, displays.victory_img, 500, 60)
                if next_stage_button.draw():
                    scene_four()

            elif game4.game_over == -1:
                displays.draw_buttons(screen, displays.defeat_img, 500, 60)
                if restart_button.draw():
                    knight.reset()
                    for mann in man_list:
                        mann.reset()
                    game4.current_fighter =1
                    game4.action_cooldown = 0
                    game4.game_over = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game4.click = True
            else:
                game4.click = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


def scene_four():
    skip = False
    scene_done = False
    myfile=open('dialog4_text.txt','rt')
    all=myfile.readlines()

    dialog4 = DialogText(displays.font, all)
    transition5 = FadeTransition(game_instruction2, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene3_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #run the message
        dialog4.running_message(screen)

        #show character in corresponding part of story
        dialog4.scene_4_function(displays.boy_icon, displays.boy_text_icon, displays.man_icon, displays.man_text_icon, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition5.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog4.checking_message_done()
                    if(dialog4.active_message == 14):
                        scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    skip=True
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog4.checking_message_done()
                    if(dialog4.active_message == 14):
                        scene_done = True
        
        pygame.display.update()


def game_instruction2():
    scene_done = False
    all=["Game Instructions:", "Find the object based on the scroll."," ", "Press space to continue"]
    transition6 = FadeTransition(find_obj, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene1_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 0, 1000, 650])

        height = 220
        for i in all:
            displays.draw_text(i, displays.font, (255,255,255), 500, height, screen, 60)
            height+=60

        if scene_done:
            transition6.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
        
        pygame.display.update()


def find_obj():
    scene_done = False
    transition7 = FadeTransition(scene_five, displays.screen_width, displays.screen_height)
    run = True
    gamef = GameFunctions2(displays.object_images_in_bg, displays.object_images)

    while run:
        clock.tick(fps)

        #draw background and text
        screen.fill((159,118,61))
        displays.draw_buttons(screen, displays.find_obj_bg, 325, 310)
        displays.draw_text(f"Object: {gamef.found}/9", displays.font, 'black', 850, 130, screen, 50)
        
        #draw object in background and object in scroll list
        gamef.objects_in_bg.draw(screen)
        gamef.objects_in_list.draw(screen)

        #when all of the objects have been found
        text_y = 280
        if gamef.found == 9:
            for text in gamef.text_complete:
                displays.draw_text(text, displays.font, 'black', 850, text_y, screen, 60)
                text_y += 40

        if scene_done:
            transition7.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    gamef.check_clicked(event)
                        
        pygame.display.update()


def scene_five():
    skip = False
    scene_done = False
    myfile=open('dialog5_text.txt','rt')
    all=myfile.readlines()

    dialog5 = DialogText(displays.font, all)
    transition8 = FadeTransition(game_last, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene2_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #run the message
        dialog5.running_message(screen)

        #show character in corresponding part of story
        dialog5.scene_5_function(displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition8.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog5.checking_message_done()
                    if(dialog5.active_message == 23):
                        scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    skip=True
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog5.checking_message_done()
                    if(dialog5.active_message == 23):
                        scene_done = True
        
        pygame.display.update()


def game_last():
    #game function
    game_last = GameFunctions1(2)

    #create fighter
    knight = Fighter(280, 240, 'Boy', 30, 14, 3)
    vamp = Fighter(790, 180, 'Vampire', 50, 10, 5)

    vamp_list = []
    vamp_list.append(vamp)

    knight_health_bar = HealthBar(70, displays.screen_height - displays.bottom_panel + 40, knight.hp, knight.max_hp)
    vamp_health_bar = HealthBar(550, displays.screen_height - displays.bottom_panel + 40, vamp.hp, vamp.max_hp)
    
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
        displays.draw_bg(screen, displays.last_fight_bg)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, knight, vamp_list)
        displays.draw_buttons(screen, displays.fight5, 870, 50)

        #draw healthbar 
        knight_health_bar.draw(knight.hp, screen)
        vamp_health_bar.draw(vamp.hp, screen)

        #draw knight
        knight.draw(screen)
        knight.update()

        #draw enemy
        for vampire in vamp_list:
            vampire.draw(screen)
            vampire.update()

        #draw damage text
        game_last.damage_text_group.update()
        game_last.damage_text_group.draw(screen)

        #control player action
        #reset action variable
        game_last.reset_state()

        game_last.attack_enemy(vamp_list)
        for vampire in vamp_list:
            if vampire.rect.collidepoint(game_last.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game_last.pos)

        #displaying potion button
        #button click 
        if potion_button.draw():
            game_last.potion = True
        #show number potion remaining
        displays.draw_text(str(knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        

        if game_last.game_over == 0:
            #player action 
            game_last.player_action(knight)

            #enemy action 
            game_last.enemy_action(vamp_list, knight)

            #check all action
            game_last.check_turn()
        
        
        #check if all enemies are death
        game_last.check_enemy_alive(vamp_list)


        #check if game is over
        if game_last.game_over != 0:
            if game_last.game_over == 1:
                displays.draw_buttons(screen, displays.victory_img, 500, 60)
                if next_stage_button.draw():
                    scene_last()

            elif game_last.game_over == -1:
                displays.draw_buttons(screen, displays.defeat_img, 500, 60)
                if restart_button.draw():
                    knight.reset()
                    for vampire in vamp_list:
                        vampire.reset()
                    game_last.current_fighter =1
                    game_last.action_cooldown = 0
                    game_last.game_over = 0


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                game_last.click = True
            else:
                game_last.click = False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    main_menu()

        pygame.display.update()


def scene_last():
    skip = False
    scene_done = False
    myfile=open('dialog5_text.txt','rt')
    all=myfile.readlines()

    dialog5 = DialogText(displays.font, all)
    transition8 = FadeTransition(game_last, displays.screen_width, displays.screen_height)

    run = True
    while run:
        displays.draw_bg(screen, displays.scene2_bg)
        clock.tick(fps)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #run the message
        dialog5.running_message(screen)

        #show character in corresponding part of story
        dialog5.scene_5_function(displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, screen)
        
        skip_button = Button(screen, 820, 50, displays.skip_button, 330, 50)
        skip_button.draw()

        #when user skips or user have done the scene, then run transition
        if skip or scene_done:
            transition8.running()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()
            
            #press enter or space to move on to next dialog
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN or event.key == pygame.K_SPACE:
                    dialog5.checking_message_done()
                    if(dialog5.active_message == 23):
                        scene_done = True
                if event.key == pygame.K_ESCAPE:
                    main_menu()
                
                #press s to skip
                if event.key == pygame.K_s:
                    skip=True
            
            #click to move on to next dialog
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    dialog5.checking_message_done()
                    if(dialog5.active_message == 23):
                        scene_done = True
        
        pygame.display.update()


main_menu()

pygame.quit()
