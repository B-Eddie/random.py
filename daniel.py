#Name: Daniel Lin
#Course Code: ICS3U1
#Code Description: Treasure hunt game(Cops and Robbers edition)
#Due Date: December 6th 2024
from pygame import *
import random

init()

#Character sprites
char_forward = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (1).png")
char_left = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (3) (1) (1).png")
char_right = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (3) (1) (1) (1).png")
char_back = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (1) (1).png")

robber_forward = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\robber_forward.png")
robber_left = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\robber_left.png")
robber_right = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\robber_right.png")
robber_back = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\robber_backward.png")

#Character sprites
#char_forward = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (1).png")
#char_left = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (3) (1) (1).png")
#char_right = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (3) (1) (1) (1).png")
#char_back = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (1) (1).png")

#Doubling character size
char_forward = transform.scale(char_forward, (char_forward.get_width() * 2, char_forward.get_height() * 2))
char_left = transform.scale(char_left, (char_left.get_width() * 2, char_left.get_height() * 2))
char_right = transform.scale(char_right, (char_right.get_width() * 2, char_right.get_height() * 2))
char_back = transform.scale(char_back, (char_back.get_width() * 2, char_back.get_height() * 2))

robber_forward = transform.scale(robber_forward, (robber_forward.get_width() * 2, robber_forward.get_height() * 2))
robber_left = transform.scale(robber_left, (robber_left.get_width() * 2, robber_left.get_height() * 2))
robber_right = transform.scale(robber_right, (robber_right.get_width() * 2, robber_right.get_height() * 2))
robber_back = transform.scale(robber_back, (robber_back.get_width() * 2, robber_back.get_height() * 2))

#Backgrounds
outdoor = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Outdoor.png")
hallway = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Hallway.png")
living_room = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Living room.png")
kitchen = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Kitchen.png")
dining_room = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Dining room.png")
bathroom = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Bathroom.png")
dark_bathroom = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Dark bathroom.png")
Room1 = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Room1.png")
Room2 = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Room2.png")
win_screen = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\win screen.png")
lose_screen = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\lose screen.png")
menu = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Menu.png")
player_selection = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\player selection.png")
difficulty = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\difficulty.png")

#Backgrounds
#outdoor = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Outdoor.png")
#hallway = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\hallway.png")
#living_room = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Living room.png")
#kitchen = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Kitchen.png")
#dining_room = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Dining room.png")
#bathroom = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Bathroom.png")
#dark_bathroom = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Dark bathroom.png")
#Room1 = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Room1.png")
#Room2 = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Room2.png")

#Inventory Items
living_room_key_sprite = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Living_room_key.png")
kitchen_key_sprite = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\kitchen_key.png")
dining_room_key_sprite = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\dining_key.png")
flashlight_sprite = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\flashlight.png")
room1_key_sprite = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\room1_key.png")

#Inventory
open("Inventory", "w").close()
open("Clues", "w").close()
current_inventory = []

info = display.Info()

#Screen size
width = 800
height = 500
SIZE = (width, height)
screen = display.set_mode(SIZE)

#Initializing state
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False

#Character Sprites
player_sprites = [char_forward, char_left, char_right, char_back, robber_forward, robber_left, robber_right, robber_back]

#Initializing starting sprite
player = player_sprites[0]
#Initializing robber sprite
player2 = player_sprites[4]

#Initializing starting location
player_x = 360
player_y = 400

#Player speed
player_speed = 5

#Collision
player_collision = Rect(player_x, player_y, 64, 64)

#Background list
backgrounds = [menu, player_selection, difficulty, outdoor, hallway, living_room, kitchen, dining_room, bathroom, dark_bathroom, Room1, Room2]

backgrounds = backgrounds[0]


#Door hit boxes
house_door = Rect(320, 100, 120, 20)
house_door_H = Rect(320, 470, 120, 20)
hallway_L = Rect(230, 290, 20, 100)
living_room_door_H = Rect(785, 340, 10, 80)
living_room_door_K = Rect(100, 0, 100, 20)
kitchen_L = Rect(100, 464, 120, 20)
kitchen_D = Rect(140, 20, 100, 20)
dining_room_K = Rect(70, 480, 95, 20)
hallway_R2 = Rect(230, 200, 20, 80)
hallway_R1 = Rect(230, 90, 20, 80)
Room2_H = Rect(775, 190, 25, 110)
Room1_H = Rect(775, 190, 25, 110)
hallway_B = Rect(310, 0, 80, 25)
bathroom_H = Rect(360, 475, 100, 20)

#Object hit boxes
menu_play = Rect(300, 75, 190, 95)
menu_player_selection = Rect(300, 180, 190, 110)
difficulty_normal_request = Rect(170, 112, 160, 116)
difficulty_hard_request = Rect(460, 112, 160, 116)
player_selection_police = Rect(170, 112, 160, 116)
player_selection_robber = Rect(460,112, 160, 116)
house_rect = Rect(145, 0, 495, 95)
tree1 = Rect(110, 175, 80, 80)
tree2 = Rect(568, 155, 60, 78)
drawer_H = Rect(520, 200, 50, 68)
bookshelf_L = Rect(750, 50, 80, 150)
couch = Rect(320, 255, 160, 25)
chip_table = Rect(230, 320, 30, 40)
TV = Rect(350, 460, 115, 20)
kitchen_table_1 = Rect(0, 0, 70, 335)
kitchen_table_2 = Rect(280, 180, 260, 140)
kitchen_table_3_1 = Rect(385, 0, 800, 90)
kitchen_table_3_2 = Rect(700, 0, 800, 335)
garbage = Rect(650, 100, 50, 50)
dining_table = Rect(260, 150, 330, 180)
room2_table = Rect(375, 435, 110, 50)
room2_drawer = Rect(530, 0, 100, 60)
room2_bookshelf = Rect(0, 0, 70, 200)
room1_table = Rect(375, 435, 110, 50)
room1_drawer = Rect(530, 0, 100, 60)
treasure = Rect(0, 165, 100, 130)
sink = Rect(180, 250, 35, 95)
bathtub = Rect(580, 130, 90, 190)
toilet = Rect(380, 0, 60, 40)

#Clue hit boxes
carpet_H = Rect(430, 0, 100, 60)
couch_cushion = Rect(320, 275, 120, 30)
drawer_H_H = Rect(510, 190, 60, 86)
bookshelf_L_L = Rect(740, 40, 80, 180)
chip_table_Key = Rect(220, 310, 50, 70)
carpet_L = Rect(300, 170, 200, 70)
paper_K = Rect(100, 380, 50, 20)
pipe_door = Rect(400, 80, 80, 50)
fruits = Rect(300, 320, 60, 60)
painting = Rect(0, 200, 20, 150)
food = Rect(250, 180, 50, 50)
dog_food = Rect(0, 0, 50, 50)
bath_tub = Rect(550, 130, 250, 200)
toilet_B = Rect(330, 0, 140, 90)
toilet_paper = Rect(330, 390, 60, 40)

#Font
my_font = font.Font(None, 20)
big_font = font.Font(None, 40)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Timers
message_duration = 2000
clue_time = 3000
entrance_start_duration = 3000
message_time = 0
clue_start_time = 0
entrance_2_start = 0
key_time_H = 0
key_time_L = 0
key_time_K = 0
flash_time = 0
key_time_B = 0
time_till_win = 0
game_start_time = 0
time_reset = 0

#Interact text
start_text = my_font.render("There's been some suspicious activity around the Howard house, best to investigate", True, WHITE)
start_text_robber = my_font.render("The Howard's are on vacation, I heard they have some treasure, nows a better time than any", True, WHITE)
my_text = my_font.render("Press E to interact", True, WHITE)
entrance_text = my_font.render("Why is the front door unlocked?", True, WHITE)
entrance_text_2 = my_font.render("All the doors are locked except for the second room to the left.", True, WHITE)
room2_text = my_font.render("Everything looks rummaged through, there must be an intruder!", True, WHITE)
room2_text_robber = my_font.render("Someone has already rummaged through this room, I hope they haven't gotten the treasure yet", True, WHITE)
key_L = my_font.render("YOU FOUND THE KEY TO THE LIVING ROOM!", True, WHITE)
key_H = my_font.render("YOU FOUND THE KEY TO THE KITCHEN!", True, WHITE)
key_K = my_font.render("YOU FOUND THE KEY TO THE DINING ROOM!", True, WHITE)
flashlight = my_font.render("YOU FOUND THE FLASHLIGHT, USE IT IN THE BATHROOM!", True, WHITE)
key_B = my_font.render("YOU FOUND THE KEY TO THE ROOM!", True, WHITE)
dark = big_font.render("IT IS TOO DARK TO SEE ANYTHING", True, WHITE)
arrest = my_font.render("FREEZE, YOU ARE UNDER ARREST", True, WHITE)
find_treasure = big_font.render("I'M GONNA BE RICH", True, WHITE)
play_request = big_font.render("PLAY", True, BLACK)
player_request = big_font.render("PLAYER", True, BLACK)
normal_difficulty = big_font.render("NORMAL", True, BLACK)
hard_difficulty = big_font.render("HARD", True, BLACK)
police_request = big_font.render("POLICE", True, BLACK)
robber_request = big_font.render("ROBBER", True, BLACK)

#Random clue
entrance_random = random.randint(1, 2)
living_random = random.randint(2,4)
kitchen_random = random.randint(5, 6)
dining_random = random.randint(7, 8)
bathroom_random = random.randint(9, 10)

#Clues
entrance_clue_1= my_font.render("Hmm, the welcome mat is suspicious, why is it near the bathroom?", True, WHITE)
entrance_clue_2 = my_font.render("Ah, the drawer looks tampered with!", True, WHITE)
living_clue_1 = my_font.render("The paper says \"Not again, the key got stuff between the couch cushions again\"", True, WHITE)
living_clue_2 = my_font.render("The paper says \"I left the kitchen key under the carpet\"", True, WHITE)
living_clue_3 = my_font.render("The paper says \"I may have lost the kitchen key while eating chips, sorry\"", True, WHITE)
kitchen_clue_1 = my_font.render("The paper says \"I was grocery shopping, I lost the dining room key, could be in all the food\"", True, WHITE)
kitchen_clue_2 = my_font.render("The paper says \"The key disappeared while I was cleaning out the pipes\"", True, WHITE)
dining_clue_1 = my_font.render("Why does the painting say \"The dog got the flashlight\"?", True, WHITE)
dining_clue_2 = my_font.render("Why does the painting say \"The flashlight is now yellow I guess\"?", True, WHITE)
bathroom_clue_1 = my_font.render("The toilet paper says \"Room keys are under towels\"", True, WHITE)
bathroom_clue_2 = my_font.render("The toilet paper says \"Room keys are in the human waste receptacle\"", True, WHITE)
#Clues as strings for adding to Clues file
Clue_texts = ["Hmm, the welcome mat is suspicious, why is it near the bathroom?", "Ah, the drawer looks tampered with!", "The paper says \"Not again, the key got stuff between the couch cushions again\"", "The paper says \"I left the kitchen key under the carpet\"", "The paper says \"I may have lost the kitchen key while eating chips, sorry\"", "The paper says \"I was grocery shopping, I lost the dining room key, could be in all the food\"", "The paper says \"The key disappeared while I was cleaning out the pipes\"", "Why does the painting say \"The dog got the flashlight\"?", "Why does the painting say \"The flashlight is now yellow I guess\"?", "The toilet paper says \"Room keys are under towels\"", "The toilet paper says \"Room keys are in the human waste receptacle\""]
Clue_list = [entrance_clue_1, entrance_clue_2, living_clue_1, living_clue_2, living_clue_3, kitchen_clue_1, kitchen_clue_2, dining_clue_1, dining_clue_2, bathroom_clue_1, bathroom_clue_2]
            #  0                1                  2             3                  4           5              6                 7             8              9                 10

#Win screen text
win_text = big_font.render("YOU WIN", True, WHITE)
score_text = big_font.render("SCORE", True, WHITE)

#Lose screen text
lose_text = big_font.render("YOU LOSE", True, WHITE)

#Text states
display_text = False
display_text_2 = False
show_clue_L = False
show_clue_K = False
show_clue_D = False
show_clue_B = False

#Inventory states
inv_key_L = False
inv_key_K = False
inv_key_D = False
inv_flash = False
inv_key_R = False

#Win state
win = False

#Difficulty
normal = False
hard = False

#Character
police = False
robber = False

#Score initialization
keep_score = 5000

#Initializing mouse position
mx, my = 0, 0

#Buffer between difficulty and player selection
buffer = False

high_score = 0
high_score_w = open("Highscore", "w")
high_score_w.write(str(high_score))
high_score_w.close()

def drawScreen():
    global message_time, display_text, display_text_2, clue_start_time, key_time_B, key_time_H, key_time_L, key_time_K, flash_time, entrance_2_start, entrance_start_duration, win, time_till_win, keep_score, game_start_time
    screen.blit(backgrounds, (0, 0))
    #Current time
    if backgrounds != menu and backgrounds != win_screen and backgrounds != player_selection and backgrounds != difficulty and backgrounds != lose_screen:
        screen.blit(current_time, (10, 20))
    #Show inventory
    if backgrounds != win_screen and backgrounds != menu and backgrounds != difficulty and backgrounds != player_selection and backgrounds != lose_screen:
        if inv_key_L:
            keep_score += 100
            screen.blit(living_room_key_sprite, (678, 5))
        if inv_key_K:
            keep_score += 100
            screen.blit(kitchen_key_sprite, (724, 5))
        if inv_key_D:
            keep_score += 100
            screen.blit(dining_room_key_sprite, (764, 5))
        if inv_flash:
            keep_score += 100
            screen.blit(flashlight_sprite, (678, 50))
        if inv_key_R:
            keep_score += 100
            screen.blit(room1_key_sprite, (724, 50))

    #Menu
    if backgrounds == menu:
        screen.blit(play_request, (365, 105))
    if backgrounds == difficulty:
        screen.blit(normal_difficulty, (193, 160))
        screen.blit(hard_difficulty, (496, 160))
    if backgrounds == player_selection:
        screen.blit(police_request, (201, 160))
        screen.blit(robber_request, (479, 160))

    #Outdoor
    if backgrounds == outdoor:
        if game_start_time == 0:
            game_start_time = time.get_ticks()
        if police:
            screen.blit(start_text, (130, 470))
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(start_text_robber, (120, 470))
            screen.blit(player2, (player_x, player_y))
        if player_collision.colliderect(house_door):
            screen.blit(my_text, (340, 100))

    # Hallway
    if backgrounds == hallway:
        if message_time == 0:
            message_time = time.get_ticks()
        if time.get_ticks() - message_time < message_duration:
            screen.blit(entrance_text, (290, 460))
        else:
            if not display_text:
                display_text = True
                clue_start_time = time.get_ticks()

        if display_text:
            #Clue 1
            if entrance_random == 1:
                if time.get_ticks() - clue_start_time < clue_time:
                    if normal:
                        screen.blit(Clue_list[0], (190, 460))
                        clue_r = open("Clues", "r")
                        found_clue_H = False
                        for line in clue_r:
                            if line.strip() == Clue_texts[0]:
                                found_clue_H = True
                                break
                        if not found_clue_H:
                            clue_a = open("Clues", "a")
                            clue_a.write(str(Clue_texts[0]) + "\n")
                            clue_a.close()
                        clue_r.close()

            #Clue 2
            if entrance_random == 2:
                if time.get_ticks() - clue_start_time < clue_time:
                    if normal:
                        screen.blit(Clue_list[1], (285, 460))
                        clue_r = open("Clues", "r")
                        found_clue_H = False
                        for line in clue_r:
                            if line.strip() == Clue_texts[1]:
                                found_clue_H = True
                                break
                        if not found_clue_H:
                            clue_a = open("Clues", "a")
                            clue_a.write(str(Clue_texts[1]) + "\n")
                            clue_a.close()
                        clue_r.close()

        if display_text and not display_text_2:
            if time.get_ticks() - clue_start_time > clue_time:
                display_text_2 = True
                entrance_2_start = time.get_ticks()

        if display_text_2:
            if time.get_ticks() - entrance_2_start < entrance_start_duration:
                screen.blit(entrance_text_2, (210, 460))

        content = open("Inventory", "r")
        for line in content:
            if "living_room_key" in line:
                if key_time_H == 0:
                    key_time_H = time.get_ticks()
                    content.close()
                    break
                if time.get_ticks() - key_time_H < message_duration:
                    screen.blit(key_L, (255, 180))
        if police:
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(player2, (player_x, player_y))
        if player_collision.colliderect(hallway_L):
            screen.blit(my_text, (185, 300))
        elif player_collision.colliderect(house_door_H):
            screen.blit(my_text, (336, 480))
        elif player_collision.colliderect(hallway_R2):
            screen.blit(my_text, (190, 155))
        elif player_collision.colliderect(hallway_R1):
            screen.blit(my_text, (185, 30))
        elif player_collision.colliderect(hallway_B):
            screen.blit(my_text, (280, 20))
        elif predicted_collision.colliderect(carpet_H):
            screen.blit(my_text, (433, 2))
        elif player_collision.colliderect(drawer_H_H):
            screen.blit(my_text, (435, 185))

    #Living Room
    if backgrounds == living_room:
        if police:
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(player2, (player_x, player_y))
        if player_collision.colliderect(living_room_door_H):
            screen.blit(my_text, (660, 315))
        if player_collision.colliderect(living_room_door_K):
            screen.blit(my_text, (86, 30))
        if player_collision.colliderect(bookshelf_L_L):
            screen.blit(my_text, (680, 30))
        if player_collision.colliderect(chip_table_Key):
            screen.blit(my_text, (180, 290))
        if player_collision.colliderect(couch_cushion):
            screen.blit(my_text, (350, 260))
        if player_collision.colliderect(carpet_L):
            screen.blit(my_text, (350, 200))
        if normal:
            if show_clue_L:
                screen.blit(Clue_list[living_random], (250, 150))
                clue_r = open("Clues", "r")
                found_clue_L = False
                for line in clue_r:
                    if line.strip() == Clue_texts[living_random]:
                        found_clue_L = True
                        break
                if not found_clue_L:
                    clue_a = open("Clues", "a")
                    clue_a.write(Clue_texts[living_random] + "\n")
                    clue_a.close()
                clue_r.close()
        content = open("Inventory", "r")
        for line in content:
            if "kitchen_key" in line:
                if key_time_L == 0:
                    key_time_L = time.get_ticks()
                    content.close()
                    break
                if time.get_ticks() - key_time_L < message_duration:
                    screen.blit(key_H, (280, 180))
    #Kitchen
    if backgrounds == kitchen:
        if police:
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(player2, (player_x, player_y))
        if player_collision.colliderect(kitchen_L):
            screen.blit(my_text, (100, 470))
        if player_collision.colliderect(kitchen_D):
            screen.blit(my_text, (124, 20))
        if player_collision.colliderect(paper_K):
            screen.blit(my_text, (100, 330))
        if player_collision.colliderect(pipe_door):
            screen.blit(my_text, (360, 100))
        if player_collision.colliderect(fruits):
            screen.blit(my_text, (270, 360))
        if normal:
            if show_clue_K:
                screen.blit(Clue_list[kitchen_random], (95, 130))
                clue_r = open("Clues", "r")
                found_clue_K = False
                for line in clue_r:
                    if line.strip() == Clue_texts[kitchen_random]:
                        found_clue_K = True
                        break
                if not found_clue_K:
                    clue_a = open("Clues", "a")
                    clue_a.write(Clue_texts[kitchen_random] + "\n")
                    clue_a.close()
                clue_r.close()
        content = open("Inventory", "r")
        for line in content:
            if "dining_key" in line:
                if key_time_K == 0:
                    key_time_K = time.get_ticks()
                    content.close()
                    break
                if time.get_ticks() - key_time_K < message_duration:
                    screen.blit(key_K, (180, 130))

    #Dining Room
    if backgrounds == dining_room:
        if police:
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(player2, (player_x, player_y))
        if player_collision.colliderect(dining_room_K):
            screen.blit(my_text, (75, 460))
        if player_collision.colliderect(painting):
            screen.blit(my_text, (10, 200))
        if player_collision.colliderect(dog_food):
            screen.blit(my_text, (5, 10))
        if player_collision.colliderect(food):
            screen.blit(my_text, (200, 200))
        if normal:
            if show_clue_D:
                screen.blit(Clue_list[dining_random], (10, 250))
                clue_r = open("Clues", "r")
                found_clue_D = False
                for line in clue_r:
                    if line.strip() == Clue_texts[dining_random]:
                        found_clue_D = True
                        break
                if not found_clue_D:
                    clue_a = open("Clues", "a")
                    clue_a.write(Clue_texts[dining_random] + "\n")
                    clue_a.close()
                clue_r.close()
        content = open("Inventory", "r")
        for line in content:
            if "flashlight" in line:
                if flash_time == 0:
                    flash_time = time.get_ticks()
                    content.close()
                    break
                if time.get_ticks() - flash_time < message_duration:
                    screen.blit(flashlight, (170, 140))

    #Room2
    if backgrounds == Room2:
        if police:
            screen.blit(player, (player_x, player_y))
            screen.blit(room2_text, (250, 300))
        if robber:
            screen.blit(player2, (player_x, player_y))
            screen.blit(room2_text_robber, (230, 300))
        if player_collision.colliderect(Room2_H):
            screen.blit(my_text, (680, 150))

    #Room1
    if backgrounds == Room1:
        if police:
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(player2, (player_x, player_y))
        if police:
            screen.blit(player_sprites[5], (110, 200))
        if time_till_win == 0:
            time_till_win = time.get_ticks()
        if police:
            if time.get_ticks() - time_till_win < message_duration:
                screen.blit(arrest, (320, 225))
            else:
                win = True
        if robber:
            if time.get_ticks() - time_till_win < message_duration:
                screen.blit(find_treasure, (220, 250))
            else:
                win = True
        if player_collision.colliderect(Room1_H):
            screen.blit(my_text, (680, 150))

    #Bathroom
    if backgrounds == bathroom:
        if police:
            screen.blit(player, (player_x, player_y))
        if robber:
            screen.blit(player2, (player_x, player_y))
        if player_collision.colliderect(bathroom_H):
            screen.blit(my_text, (330, 460))
        if player_collision.colliderect(toilet_B):
            screen.blit(my_text, (360, 130))
        if player_collision.colliderect(bath_tub):
            screen.blit(my_text, (440, 200))
        if player_collision.colliderect(toilet_paper):
            screen.blit(my_text, (360, 380))
        if normal:
            if show_clue_B:
                screen.blit(Clue_list[bathroom_random], (300, 360))
                clue_r = open("Clues", "r")
                found_clue_B = False
                for line in clue_r:
                    if line.strip() == Clue_texts[bathroom_random]:
                        found_clue_B = True
                        break
                if not found_clue_B:
                    clue_a = open("Clues", "a")
                    clue_a.write(Clue_texts[bathroom_random] + "\n")
                    clue_a.close()
                clue_r.close()

        content = open("Inventory", "r")
        for line in content:
            if "room1_key" in line:
                if key_time_B == 0:
                    key_time_B = time.get_ticks()
                    content.close()
                    break
                if time.get_ticks() - key_time_B < message_duration:
                    screen.blit(key_B, (270, 140))

    #Dark Bathroom
    if backgrounds == dark_bathroom:
        screen.blit(dark, (180, 220))
        screen.blit(my_text, (340, 400))

    #Win Screen
    if backgrounds == win_screen:
        screen.blit(win_text, (360, 40))
        screen.blit(score_text, (370, 140))
        screen.blit(score_num, (400, 188))
        screen.blit(my_text, (367, 360))
    display.flip()

    #Lose Screen
    if backgrounds == lose_screen:
        screen.blit(lose_text, (350, 40))
        screen.blit(my_text, (367, 360))

#Initializing clock
myClock = time.Clock()

running = True

while running:
    #Time tracker
    if backgrounds != win_screen:
        timer = (time.get_ticks() - game_start_time) / 1000
        current_time = my_font.render(str(timer), True, WHITE)
    # Win screen
    if win:
        backgrounds = win_screen
    #Score keeping
    elapsed_time = (time.get_ticks() - game_start_time) // 1000
    if normal:
        if elapsed_time >= 90:
            backgrounds = lose_screen
    if hard:
        if elapsed_time >= 60:
            backgrounds = lose_screen

    if backgrounds != win_screen:
        keep_score = 5000 - (elapsed_time * 10)
    if keep_score < 0:
        keep_score = 0
    if backgrounds == win_screen:
        score_w = open("Score", "w")
        score_w.write(str(keep_score))
        score_w.close()
        score_file = open("Score", "r")
        score = score_file.read().strip()
        new_high_score = int(score)
        high_score_r = open("Highscore", "r")
        if new_high_score > int(high_score_r.read()):
            high_score = new_high_score
        high_score_r.close()
        score_num = my_font.render(str(score), True, WHITE)
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False
        # Mouse location
        if evnt.type == MOUSEBUTTONDOWN:
            mx, my = evnt.pos
            #Menu
            if backgrounds == menu:
                if menu_play.collidepoint(mx, my):
                    backgrounds = difficulty
            #Difficulty selection
            if backgrounds == difficulty:
                if difficulty_normal_request.collidepoint(mx, my):
                    normal = True
                    backgrounds = player_selection
                    buffer = True
                if difficulty_hard_request.collidepoint(mx, my):
                    hard = True
                    backgrounds = player_selection
                    buffer = True

            if backgrounds == player_selection:
                if buffer:
                    buffer = False
                else:
                    if player_selection_police.collidepoint(mx, my):
                        police = True
                        backgrounds = outdoor
                    elif player_selection_robber.collidepoint(mx, my):
                        robber = True
                        backgrounds = outdoor

        if evnt.type == MOUSEMOTION:
            mx, my = evnt.pos
        #Initializing key down
        if evnt.type == KEYDOWN:
            if evnt.key == K_LEFT:
                KEY_LEFT = True
            if evnt.key == K_RIGHT:
                KEY_RIGHT = True
            if evnt.key == K_UP:
                KEY_UP = True
            if evnt.key == K_DOWN:
                KEY_DOWN = True
            if evnt.key == K_e:
                # Room changing and interaction
                #Outdoor
                if backgrounds == outdoor and player_collision.colliderect(house_door):
                    player_x = 360
                    player_y = 430
                    if police:
                        player = player_sprites[3]
                    if robber:
                        player2 = player_sprites[7]
                    backgrounds = hallway
                #Hallway
                elif backgrounds == hallway and player_collision.colliderect(house_door_H):
                    player_x = 360
                    player_y = 120
                    if police:
                        player = player_sprites[0]
                    if robber:
                        player2 = player_sprites[4]
                    backgrounds = outdoor
                elif entrance_random == 1 and backgrounds == hallway and player_collision.colliderect(carpet_H):
                    if "living_room_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("living_room_key" + "\n")
                        inventory.close()
                        current_inventory.append("living_room_key")
                elif entrance_random == 2 and backgrounds == hallway and player_collision.colliderect(drawer_H_H):
                    if "living_room_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("living_room_key" + "\n")
                        inventory.close()
                        current_inventory.append("living_room_key")
                elif backgrounds == hallway and player_collision.colliderect(hallway_L):
                    content = open("Inventory", "r")
                    for line in content:
                        if "living_room_key" in line:
                            player_x = 740
                            player_y = 340
                            if police:
                                player = player_sprites[1]
                            if robber:
                                player2 = player_sprites[5]
                            backgrounds = living_room
                            content.close()
                            break

                elif backgrounds == hallway and player_collision.colliderect(hallway_R2):
                    player_x = 735
                    player_y = 210
                    if police:
                        player = player_sprites[1]
                    if robber:
                        player2 = player_sprites[5]
                    backgrounds = Room2
                elif "room1_key" in current_inventory and backgrounds == hallway and player_collision.colliderect(hallway_R1):
                    player_x = 735
                    player_y = 210
                    if police:
                        player = player_sprites[1]
                    if robber:
                        player2 = player_sprites[5]
                    backgrounds = Room1
                elif backgrounds == hallway and player_collision.colliderect(hallway_B) and "flashlight" in current_inventory:
                    player_x = 380
                    player_y = 426
                    if police:
                        player = player_sprites[3]
                    if robber:
                        player2 = player_sprites[7]
                    backgrounds = bathroom
                elif backgrounds == hallway and player_collision.colliderect(hallway_B) and "flashlight" not in current_inventory:
                    backgrounds = dark_bathroom

                #Living Room
                elif backgrounds == living_room and player_collision.colliderect(living_room_door_H):
                    player_x = 235
                    player_y = 340
                    if police:
                        player = player_sprites[2]
                    if robber:
                        player2 = player_sprites[6]
                    backgrounds = hallway
                elif backgrounds == living_room and player_collision.colliderect(living_room_door_K):
                    content = open("Inventory", "r")
                    for line in content:
                        if "kitchen_key" in line:
                            player_x = 125
                            player_y = 430
                            if police:
                                player = player_sprites[3]
                            if robber:
                                player2 = player_sprites[7]
                            backgrounds = kitchen
                            content.close()
                            break
                elif living_random == 2 and backgrounds == living_room and player_collision.colliderect(couch_cushion):
                    if "kitchen_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("kitchen_key" + "\n")
                        inventory.close()
                        current_inventory.append("kitchen_key")
                elif living_random == 3 and backgrounds == living_room and player_collision.colliderect(carpet_L):
                    if "kitchen_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("kitchen_key" + "\n")
                        inventory.close()
                        current_inventory.append("kitchen_key")
                elif living_random == 4 and backgrounds == living_room and player_collision.colliderect(chip_table_Key):
                    if "kitchen_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("kitchen_key" + "\n")
                        inventory.close()
                        current_inventory.append("kitchen_key")

                #Kitchen
                elif backgrounds == kitchen and player_collision.colliderect(kitchen_L):
                    player_x = 110
                    player_y = 10
                    if police:
                        player = player_sprites[0]
                    if robber:
                        player2 = player_sprites[4]
                    backgrounds = living_room
                elif backgrounds == kitchen and player_collision.colliderect(kitchen_D):
                    content = open("Inventory", "r")
                    for line in content:
                        if "dining_key" in line:
                            player_x = 110
                            player_y = 432
                            if police:
                                player = player_sprites[3]
                            if robber:
                                player2 = player_sprites[7]
                            backgrounds = dining_room
                            content.close()
                            break
                elif kitchen_random == 5 and backgrounds == kitchen and player_collision.colliderect(fruits):
                    if "dining_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("dining_key" + "\n")
                        inventory.close()
                        current_inventory.append("dining_key")
                elif kitchen_random == 6 and backgrounds == kitchen and player_collision.colliderect(pipe_door):
                    if "dining_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("dining_key" + "\n")
                        inventory.close()
                        current_inventory.append("dining_key")

                #Dining Room
                elif backgrounds == dining_room and player_collision.colliderect(dining_room_K):
                    player_x = 140
                    player_y = 10
                    if police:
                        player = player_sprites[0]
                    if robber:
                        player = player_sprites[4]
                    backgrounds = kitchen
                elif dining_random == 7 and backgrounds == dining_room and player_collision.colliderect(dog_food):
                    if "flashlight" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("flashlight" + "\n")
                        inventory.close()
                        current_inventory.append("flashlight")
                elif dining_random == 8 and backgrounds == dining_room and player_collision.colliderect(food):
                    if "flashlight" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("flashlight" + "\n")
                        inventory.close()
                        current_inventory.append("flashlight")

                #Room2
                elif backgrounds == Room2 and player_collision.colliderect(Room2_H):
                    player_x = 232
                    player_y = 190
                    if police:
                        player = player_sprites[2]
                    if robber:
                        player2 = player_sprites[6]
                    backgrounds = hallway

                #Room1
                elif backgrounds == Room1 and player_collision.colliderect(Room1_H):
                    player_x = 232
                    player_y = 75
                    if police:
                        player = player_sprites[2]
                    if robber:
                        player2 = player_sprites[6]
                    backgrounds = hallway

                #Bathroom
                elif backgrounds == bathroom and player_collision.colliderect(bathroom_H):
                    player_x = 305
                    player_y = 15
                    if police:
                        player = player_sprites[0]
                    if robber:
                        player2 = [4]
                    backgrounds = hallway

                elif bathroom_random == 9 and backgrounds == bathroom and player_collision.colliderect(bath_tub):
                    if "room1_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("room1_key")
                        inventory.close()
                        current_inventory.append("room1_key")
                elif bathroom_random == 10 and backgrounds == bathroom and player_collision.colliderect(toilet_B):
                    if "room1_key" not in current_inventory:
                        inventory = open("Inventory", "a")
                        inventory.write("room1_key")
                        inventory.close()
                        current_inventory.append("room1_key")

                #Dark bathroom
                elif backgrounds == dark_bathroom:
                    player_x = 305
                    player_y = 15
                    if police:
                        player = player_sprites[0]
                    if robber:
                        player2 = player_sprites[4]
                    backgrounds = hallway

                elif backgrounds == win_screen:
                    open("Inventory", "w").close()
                    open("Score", "w").close()
                    buffer = False
                    win = False
                    message_time = 0
                    clue_start_time = 0
                    entrance_2_start = 0
                    key_time_H = 0
                    key_time_L = 0
                    key_time_K = 0
                    flash_time = 0
                    key_time_B = 0
                    time_till_win = 0
                    game_start_time = 0
                    time_reset = 0
                    player_x = 360
                    player_y = 400
                    normal = False
                    hard = False
                    police = False
                    robber = False
                    inv_key_L = False
                    inv_key_K = False
                    inv_key_D = False
                    inv_flash = False
                    inv_key_R = False
                    current_inventory = []
                    backgrounds = menu

                elif backgrounds == lose_screen:
                    open("Inventory", "w").close()
                    open("Score", "w").close()
                    buffer = False
                    win = False
                    message_time = 0
                    clue_start_time = 0
                    entrance_2_start = 0
                    key_time_H = 0
                    key_time_L = 0
                    key_time_K = 0
                    flash_time = 0
                    key_time_B = 0
                    time_till_win = 0
                    game_start_time = 0
                    time_reset = 0
                    player_x = 360
                    player_y = 400
                    normal = False
                    hard = False
                    police = False
                    robber = False
                    inv_key_L = False
                    inv_key_K = False
                    inv_key_D = False
                    inv_flash = False
                    inv_key_R = False
                    current_inventory = []
                    backgrounds = menu


        #Initializing key up
        if evnt.type == KEYUP:
            if evnt.key == K_LEFT:
                KEY_LEFT = False
            if evnt.key == K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == K_UP:
                KEY_UP = False
            if evnt.key == K_DOWN:
                KEY_DOWN = False

        #Clue appearance
        #Living Room
        if backgrounds == living_room:
            if player_collision.colliderect(bookshelf_L_L):
                if evnt.type == KEYDOWN:
                    if evnt.key == K_e:
                        show_clue_L = True
                    else:
                        show_clue_L = False
        if backgrounds == kitchen:
            if player_collision.colliderect(paper_K):
                if evnt.type == KEYDOWN:
                    if evnt.key == K_e:
                        show_clue_K = True
                    else:
                        show_clue_K = False
        if backgrounds == dining_room:
            if player_collision.colliderect(painting):
                if evnt.type == KEYDOWN:
                    if evnt.key == K_e:
                        show_clue_D = True
                    else:
                        show_clue_D = False
        if backgrounds == bathroom:
            if player_collision.colliderect(toilet_paper):
                if evnt.type == KEYDOWN:
                    if evnt.key == K_e:
                        show_clue_B = True
                    else:
                        show_clue_B = False

        #Inventory state change
        content = open("Inventory", "r")
        for line in content:
            if "living_room_key" in line:
                inv_key_L = True
            if "kitchen_key" in line:
                inv_key_K = True
            if "dining_key" in line:
                inv_key_D = True
            if "flashlight" in line:
                inv_flash = True
            if "room1_key" in line:
                inv_key_R = True
        content.close()

    # Updating player collision
    player_collision = Rect(player_x, player_y, 64, 64)

    if KEY_LEFT:
        if police:
            player = player_sprites[1]
        if robber:
            player2 = player_sprites[5]
        predicted_collision = player_collision.move(-player_speed * 1.5, 0)

        #Outdoor
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_x >= -10:
                player_x -= player_speed

        #Hallway
        elif backgrounds == hallway:
            if not predicted_collision.colliderect(drawer_H) and player_x >= 230:
                player_x -= player_speed

        #Living Room
        elif backgrounds == living_room:
            if not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_x >= -10:
                player_x -= player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_x >= -10:
            player_x -= player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_x >= -10:
            player_x -= player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_x >= -10:
            player_x -= player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_x >= -10:
            player_x -= player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_x >= 173:
            player_x -= player_speed

    if KEY_RIGHT:
        if police:
            player = player_sprites[2]
        if robber:
            player2 = player_sprites[6]
        predicted_collision = player_collision.move(player_speed, 0)

        #Outdoor
        if backgrounds == outdoor and not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_x <= 745:
                player_x += player_speed

        #Hallway
        elif backgrounds == hallway and not predicted_collision.colliderect(drawer_H) and player_x <= 500:
                player_x += player_speed

        #Living Room
        elif backgrounds == living_room and not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_x <= 740:
                player_x += player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_x <= 740:
            player_x += player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_x <= 740:
            player_x += player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_x <= 740:
            player_x += player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_x <= 740:
            player_x += player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_x <= 585:
            player_x += player_speed

    if KEY_UP:
        if police:
            player = player_sprites[3]
        if robber:
            player2 = player_sprites[7]
        predicted_collision = player_collision.move(0, -player_speed * 1.7)

        #Outdoor
        if backgrounds == outdoor and not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_y >= 0:
                player_y -= player_speed

        #Hallway
        elif backgrounds == hallway and not predicted_collision.colliderect(drawer_H) and player_y >= 5:
            player_y -= player_speed

        #Living Room
        elif backgrounds == living_room and not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_y >= 5:
            player_y -= player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_y >= 5:
            player_y -= player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_y >= 5:
            player_y -= player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_y >= 5:
            player_y -= player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_y >= 5:
            player_y -= player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_y >= 5:
            player_y -= player_speed

    if KEY_DOWN:
        if police:
            player = player_sprites[0]
        if robber:
            player2 = player_sprites[4]
        predicted_collision = player_collision.move(0, player_speed)

        #Outdoor
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_y <= 430:
                player_y += player_speed

        #Hallway
        elif backgrounds == hallway and player_y <= 426:
            if not predicted_collision.colliderect(drawer_H) and player_y <= 426:
                player_y += player_speed

        #Living Room
        elif backgrounds == living_room and player_y <= 426:
            if not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_y <= 426:
                player_y += player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_y <= 426:
            player_y += player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_y <= 426:
            player_y += player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_y <= 426:
            player_y += player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_y <= 426:
            player_y += player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_y <= 426:
            player_y += player_speed

    drawScreen()
    display.flip()
    myClock.tick(60)
score = open("Score", "w").close()
quit()
