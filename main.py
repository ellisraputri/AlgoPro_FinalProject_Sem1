import pygame
import game_function2
from game_function2 import Scene, GameInstruction, Game, FindObject
from img_text_display import Displaying
from continue_game import ContinueGame

pygame.init()

#setting the frame rate
clock = pygame.time.Clock()
fps = 60

#display
screen = pygame.display.set_mode((1000, 650))
displays = Displaying()

#the game title
pygame.display.set_caption('Game')

#to track current state
current_state_list = []

def main_menu():
    #if player press continue before starting a new game, automatically starts into new game
    current_state = continue_game.getPosition(0)
    current_state_list.append(current_state)

    #game loop
    while True:
        #draw the background image and logo
        displays.draw_bg(screen, displays.bg_main)
        displays.draw_buttons(screen, displays.main_logo, 500, 150)

        #if player press continue after starting a new game
        if len(current_state_list) > 1:
            game_function2.main_menu(screen, scene_one, clock, fps, displays.new_game_img, displays.continue_game_img, displays.exit_img, current_state_list[-2])
        
        #if player press continue before starting a new game
        else:
            game_function2.main_menu(screen, scene_one, clock, fps, displays.new_game_img, displays.continue_game_img, displays.exit_img, current_state_list[-1])


def scene_one():
    current_state = continue_game.getPosition(1)
    current_state_list.append(current_state)

    scene_1 = Scene("Assets/story/dialog1_text.txt", 1, displays.font, game_instruction, displays.screen_width, displays.screen_height)

    while scene_1.run:
        #draw background and black panel
        displays.draw_bg(screen, displays.scene1_bg)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #dialog functions and event key
        scene_1.running(clock, fps, screen, displays.skip_button, displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, displays.object_scroll)


def game_instruction():
    current_state = continue_game.getPosition(2)
    current_state_list.append(current_state)

    game_instruction_1 = GameInstruction(game_one, displays.screen_width, displays.screen_height)

    while game_instruction_1.run:
        #draw background
        pygame.draw.rect(screen, 'black', [0, 0, 1000, 650])

        #draw text
        height = 120
        for i in game_instruction_1.all1:
            displays.draw_text(i, displays.font, (255,255,255), 500, height, screen, 60)
            height+=60
        
        #event checker and functions
        game_instruction_1.running(clock, fps)


def game_one():
    current_state = continue_game.getPosition(3)
    current_state_list.append(current_state)

    game_1 = Game(screen, 270, 300, 650, 310, 'Wolf1', 15, 3, 0, 2, displays.screen_height, displays.bottom_panel, displays.potion_img, displays.restart_img, displays.next_stage_img)

    while game_1.run:
        #draw background and panel
        displays.draw_bg(screen, displays.bg_image)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, game_1.knight, game_1.enemy_list)
        displays.draw_buttons(screen, displays.fight1, 870, 50)

        game_1.running(clock, fps, screen)

        #control player action
        #reset action variable
        game_1.game.reset_state()

        #attacking enemy
        game_1.game.attack_enemy(game_1.enemy_list)
        for enemy in game_1.enemy_list:
            if enemy.rect.collidepoint(game_1.game.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game_1.game.pos)

        #show number potion remaining
        displays.draw_text(str(game_1.knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        
        #check if game over or not and check click
        game_1.check_game_state(screen, displays.victory_img, displays.defeat_img, game_two)
        

def game_two():
    current_state = continue_game.getPosition(4)
    current_state_list.append(current_state)

    game_2 = Game(screen, 270, 300, 650, 310, 'Wolf2', 15, 4, 1, 2, displays.screen_height, displays.bottom_panel, displays.potion_img, displays.restart_img, displays.next_stage_img)

    while game_2.run:
        #draw background and panel
        displays.draw_bg(screen, displays.bg_image)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, game_2.knight, game_2.enemy_list)
        displays.draw_buttons(screen, displays.fight2, 870, 50)

        game_2.running(clock, fps, screen)

        #control player action
        #reset action variable
        game_2.game.reset_state()

        #attacking enemy
        game_2.game.attack_enemy(game_2.enemy_list)
        for enemy in game_2.enemy_list:
            if enemy.rect.collidepoint(game_2.game.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game_2.game.pos)

        #show number potion remaining
        displays.draw_text(str(game_2.knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        
        #check if game over or not and check click
        game_2.check_game_state(screen, displays.victory_img, displays.defeat_img, game_three)


def game_three():
    current_state = continue_game.getPosition(5)
    current_state_list.append(current_state)

    game_3 = Game(screen, 270, 300, 650, 310, 'Wolf3', 20, 5, 2, 2, displays.screen_height, displays.bottom_panel, displays.potion_img, displays.restart_img, displays.next_stage_img)

    while game_3.run:
        #draw background and panel
        displays.draw_bg(screen, displays.bg_image)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, game_3.knight, game_3.enemy_list)
        displays.draw_buttons(screen, displays.fight3, 870, 50)

        game_3.running(clock, fps, screen)

        #control player action
        #reset action variable
        game_3.game.reset_state()

        #attacking enemy
        game_3.game.attack_enemy(game_3.enemy_list)
        for enemy in game_3.enemy_list:
            if enemy.rect.collidepoint(game_3.game.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game_3.game.pos)

        #show number potion remaining
        displays.draw_text(str(game_3.knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        
        #check if game over or not, check click
        game_3.check_game_state(screen, displays.victory_img, displays.defeat_img, scene_two)


def scene_two():
    current_state = continue_game.getPosition(6)
    current_state_list.append(current_state)

    scene_2 = Scene("Assets/story/dialog2_text.txt", 2, displays.font, scene_three, displays.screen_width, displays.screen_height)

    while scene_2.run:
        #draw background and black panel
        displays.draw_bg(screen, displays.scene2_bg)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #dialog functions and event key
        scene_2.running(clock, fps, screen, displays.skip_button, displays.boy_icon, displays.boy_text_icon, "", "", displays.castle)


def scene_three():
    current_state = continue_game.getPosition(7)
    current_state_list.append(current_state)

    scene_3 = Scene("Assets/story/dialog3_text.txt", 3, displays.font, game_four, displays.screen_width, displays.screen_height)

    while scene_3.run:
        #draw background and black panel
        displays.draw_bg(screen, displays.scene3_bg)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #dialog functions and event key
        scene_3.running(clock, fps, screen, displays.skip_button, displays.boy_icon, displays.boy_text_icon, displays.man_icon, displays.man_text_icon, "")


def game_four():
    current_state = continue_game.getPosition(8)
    current_state_list.append(current_state)

    game_4 = Game(screen, 240, 320, 700, 320, 'Man', 30, 8, 3, 1, displays.screen_height, displays.bottom_panel, displays.potion_img, displays.restart_img, displays.next_stage_img)

    while game_4.run:
        #draw background and panel
        displays.draw_bg(screen, displays.scene3_bg)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, game_4.knight, game_4.enemy_list)
        displays.draw_buttons(screen, displays.fight4, 870, 50)

        game_4.running(clock, fps, screen)

        #control player action
        #reset action variable
        game_4.game.reset_state()

        #attacking enemy
        game_4.game.attack_enemy(game_4.enemy_list)
        for enemy in game_4.enemy_list:
            if enemy.rect.collidepoint(game_4.game.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game_4.game.pos)

        #show number potion remaining
        displays.draw_text(str(game_4.knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        
        #check if game over or not, check click
        game_4.check_game_state(screen, displays.victory_img, displays.defeat_img, scene_four)


def scene_four():
    current_state = continue_game.getPosition(9)
    current_state_list.append(current_state)

    scene_4 = Scene("Assets/story/dialog4_text.txt", 4, displays.font, game_instruction2, displays.screen_width, displays.screen_height)

    while scene_4.run:
        #draw background and black panel
        displays.draw_bg(screen, displays.scene3_bg)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #dialog functions and event key
        scene_4.running(clock, fps, screen, displays.skip_button, displays.boy_icon, displays.boy_text_icon, displays.man_icon, displays.man_text_icon, "")


def game_instruction2():
    current_state = continue_game.getPosition(10)
    current_state_list.append(current_state)

    game_instruction_2 = GameInstruction(find_obj, displays.screen_width, displays.screen_height)

    while game_instruction_2.run:
        #draw background
        pygame.draw.rect(screen, 'black', [0, 0, 1000, 650])

        #draw text
        height = 220
        for i in game_instruction_2.all2:
            displays.draw_text(i, displays.font, (255,255,255), 500, height, screen, 60)
            height+=60
        
        #event checker and functions
        game_instruction_2.running(clock, fps)


def find_obj():
    current_state = continue_game.getPosition(11)
    current_state_list.append(current_state)

    find_object = FindObject(scene_five, displays.screen_width, displays.screen_height, displays.object_images_in_bg, displays.object_images)

    while find_object.run:
        #draw background and text
        screen.fill((159,118,61))
        displays.draw_buttons(screen, displays.find_obj_bg, 325, 310)
        displays.draw_text(f"Object: {find_object.gamef.found}/9", displays.font, 'black', 850, 130, screen, 50)
        
        #run game functions
        find_object.running(clock, fps, screen)


def scene_five():
    current_state = continue_game.getPosition(12)
    current_state_list.append(current_state)

    scene_5 = Scene("Assets/story/dialog5_text.txt", 5, displays.font, game_five, displays.screen_width, displays.screen_height)

    while scene_5.run:
        #draw background and black panel
        displays.draw_bg(screen, displays.scene2_bg)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #dialog functions and event key
        scene_5.running(clock, fps, screen, displays.skip_button, displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, "")


def game_five():
    current_state = continue_game.getPosition(13)
    current_state_list.append(current_state)

    game_5 = Game(screen, 280, 240, 790, 180, 'Vampire', 50, 9, 5, 1, displays.screen_height, displays.bottom_panel, displays.potion_img, displays.restart_img, displays.next_stage_img)

    while game_5.run:
        #draw background and panel
        displays.draw_bg(screen, displays.last_fight_bg)
        displays.draw_panel(screen, displays.screen_height, displays.bottom_panel, game_5.knight, game_5.enemy_list)
        displays.draw_buttons(screen, displays.fight5, 870, 50)

        game_5.running(clock, fps, screen)

        #control player action
        #reset action variable
        game_5.game.reset_state()

        #attacking enemy
        game_5.game.attack_enemy(game_5.enemy_list)
        for enemy in game_5.enemy_list:
            if enemy.rect.collidepoint(game_5.game.pos):
                #hide mouse
                pygame.mouse.set_visible(False)
                #show sword
                displays.draw_sword(screen, game_5.game.pos)

        #show number potion remaining
        displays.draw_text(str(game_5.knight.potions), displays.font, (255,0,0), 145, displays.screen_height -displays.bottom_panel+85, screen, 40)
        
        #check if game over or not, check click
        game_5.check_game_state(screen, displays.victory_img, displays.defeat_img, scene_six)


def scene_six():
    current_state = continue_game.getPosition(14)
    current_state_list.append(current_state)

    scene_6 = Scene("Assets/story/dialog6_text.txt", 6, displays.font, end_scene, displays.screen_width, displays.screen_height)

    while scene_6.run:
        #draw background and black panel
        displays.draw_bg(screen, displays.scene2_bg)
        pygame.draw.rect(screen, 'black', [0, 450, 1000, 300])

        #dialog functions and event key
        scene_6.running(clock, fps, screen, displays.skip_button, displays.boy_icon, displays.boy_text_icon, displays.vampire_icon, displays.vampire_text_icon, "")


def end_scene():
    current_state = continue_game.getPosition(14)
    current_state_list.append(current_state)

    game_end = GameInstruction(main_menu, displays.screen_width, displays.screen_height)

    while game_end.run:
        #draw background
        pygame.draw.rect(screen, 'black', [0, 0, 1000, 650])

        #draw text
        height = 250
        for i in game_end.all3:
            displays.draw_text(i, displays.font, (255,255,255), 500, height, screen, 60)
            height+=60
        
        #event checker and functions
        game_end.running(clock, fps)


#list of all scene and game
all_function = [scene_one, scene_one, game_instruction, game_one, game_two, game_three, scene_two, scene_three, game_four, scene_four, game_instruction2, find_obj, scene_five, game_five, scene_six, end_scene]
#enable continue function
continue_game = ContinueGame(all_function)

main_menu()

pygame.quit()
