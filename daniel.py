#Name: Daniel Lin
#Course Code: ICS3U1
#Code Description: Treasure hunt game
#Due Date: December 6th 2024

from pygame import *
import random

init()

#Inventory
inventory = open("Inventory", "w").close()

info = display.Info()

#Screen size
width = 800
height = 500
SIZE = (width, height)
screen = display.set_mode(SIZE)

#Initializing whether keys are true or false
KEY_RIGHT = False
KEY_LEFT = False
KEY_UP = False
KEY_DOWN = False

#Character sprites
char_forward = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (1).png")
char_left = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (3) (1) (1).png")
char_right = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (3) (1) (1) (1).png")
char_back = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\image (1) (1).png")

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

#Backgrounds
outdoor = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Outdoor.png")
hallway = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Hallway.png")
living_room = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Living room.png")
kitchen = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Kitchen.png")
dining_room = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Dining room.png")
bathroom = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Bathroom.png")
Room1 = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Room1.png")
Room2 = image.load("C:\\Users\\Daniel\\PycharmProjects\\pythonProject\\sprites\\image (3) (1) (1) (1)\\Room2.png")

#Backgrounds
#outdoor = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Outdoor.png")
#hallway = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\hallway.png")
#living_room = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Living room.png")
#kitchen = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Kitchen.png")
#dining_room = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Dining room.png")
#bathroom = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Bathroom.png")
#Room1 = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Room1.png")
#Room2 = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Room2.png")

#Character Sprites
player_sprites = [char_forward, char_left, char_right, char_back]

#Initializing starting sprite
player = player_sprites[0]

#Initializing starting location
player_x = 360
player_y = 400

#Player speed
player_speed = 5

#Background list
backgrounds = [outdoor, hallway, living_room, kitchen, dining_room, bathroom, Room1, Room2]

backgrounds = backgrounds[0]

#Font
my_font = font.Font(None, 20)
WHITE = (255, 255, 255)

#Interact text
start_text = my_font.render("There's been some suspicious activity around the Howard house, best to investigate", True, WHITE)
my_text = my_font.render("Press E to interact", True, WHITE)
entrance_text = my_font.render("Why is the front door unlocked?", True, WHITE)

#Random stuff
entrance_random = random.randint(1, 2)

#Clues
entrance_clue_1= my_font.render("Hmm, the welcome mat is suspicious, why is it near the bathroom?", True, WHITE)
entrance_clue_2 = my_font.render("Ah, the drawer looks tampered with!", True, WHITE)
Clue_list = [entrance_clue_1, entrance_clue_2]

#Clue timer
message_time = time.get_ticks()
clue_time = 8000

#Door hit boxes
house_door = Rect(320, 100, 120, 20)
house_door_H = Rect(320, 470, 120, 20)
hallway_L = Rect(230, 290, 20, 100)
living_room_door_H = Rect(740, 340, 10, 80)
living_room_door_K = Rect(100, 0, 100, 20)
kitchen_L = Rect(100, 422, 120, 20)
kitchen_D = Rect(140, 20, 100, 20)
dining_room_K = Rect(70, 480, 95, 20)
hallway_R2 = Rect(230, 200, 20, 80)
hallway_R1 = Rect(230, 90, 20, 80)
Room2_H = Rect(775, 190, 25, 110)
Room1_H = Rect(775, 190, 25, 110)
hallway_B = Rect(310, 0, 80, 25)
bathroom_H = Rect(360, 475, 100, 20)

#Object hit boxes
house_rect = Rect(145, 0, 495, 95)
tree1 = Rect(110, 175, 80, 80)
tree2 = Rect(568, 155, 60, 78)
drawer_H = Rect(520, 200, 50, 68)
drawer_H_H = Rect(510, 190, 60, 78)
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
carpet_H = Rect(430, 0, 100, 60)

#Player hit box
player_collision = Rect(player_x, player_y, 64, 64)

#Initialize
display_text = False

def drawScreen():
    global display_text  # This tells Python that we're using the global display_text variable

    screen.blit(backgrounds, (0, 0))

    #Outdoor
    if backgrounds == outdoor:
        screen.blit(start_text, (130, 470))
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(house_door):
            screen.blit(my_text, (340, 100))

    #Hallway
    if backgrounds == hallway:
        if time.get_ticks() - message_time < 4000:
            screen.blit(entrance_text, (290, 460))
        else:
            display_text = True

        if display_text:
            #Clue 1
            if entrance_random == 1:
                if time.get_ticks() - message_time < clue_time:
                    screen.blit(Clue_list[0], (190, 460))
                    display_text = False
            #Clue 2
            if entrance_random == 2:
                if time.get_ticks() - message_time < clue_time:
                    screen.blit(Clue_list[1], (285, 460))
                    display_text = False

        screen.blit(player, (player_x, player_y))
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
        elif predicted_collision.colliderect(drawer_H_H):
            screen.blit(my_text, (435, 185))

    #Living Room
    if backgrounds == living_room:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(living_room_door_H):
            screen.blit(my_text, (660, 315))
        elif player_collision.colliderect(living_room_door_K):
            screen.blit(my_text, (86, 30))

    #Kitchen
    if backgrounds == kitchen:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(kitchen_L):
            screen.blit(my_text, (100, 470))
        if player_collision.colliderect(kitchen_D):
            screen.blit(my_text, (124, 20))

    #Dining Room
    if backgrounds == dining_room:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(dining_room_K):
            screen.blit(my_text, (75, 460))

    #Room2
    if backgrounds == Room2:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(Room2_H):
            screen.blit(my_text, (680, 150))

    #Room1
    if backgrounds == Room1:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(Room1_H):
            screen.blit(my_text, (680, 150))

    #Bathroom
    if backgrounds == bathroom:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(bathroom_H):
            screen.blit(my_text, (330, 460))

    display.flip()

#Initializing clock
myClock = time.Clock()

running = True

while running:
    for evnt in event.get():
        if evnt.type == QUIT:
            running = False

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
                #Outdoor
                if backgrounds == outdoor and player_collision.colliderect(house_door):
                    player_x = 360
                    player_y = 430
                    player = player_sprites[3]
                    backgrounds = hallway
                #Hallway
                elif backgrounds == hallway and player_collision.colliderect(house_door_H):
                    player_x = 360
                    player_y = 120
                    player = player_sprites[0]
                    backgrounds = outdoor
                elif entrance_random == 1 and backgrounds == hallway and predicted_collision.colliderect(carpet_H):
                    inventory = open("Inventory", "w")
                    inventory.write("living_room_key")
                    inventory.close()
                elif entrance_random == 2 and backgrounds == hallway and predicted_collision.colliderect(drawer_H):
                    inventory = open("Inventory", "w")
                    inventory.write("living_room_key")
                    inventory.close()
                elif backgrounds == hallway and player_collision.colliderect(hallway_L):
                    player_x = 740
                    player_y = 340
                    player = player_sprites[1]
                    backgrounds = living_room
                elif backgrounds == hallway and player_collision.colliderect(hallway_R2):
                    player_x = 735
                    player_y = 210
                    player = player_sprites[1]
                    backgrounds = Room2
                elif backgrounds == hallway and player_collision.colliderect(hallway_R1):
                    player_x = 735
                    player_y = 210
                    player = player_sprites[1]
                    backgrounds = Room1
                elif backgrounds == hallway and player_collision.colliderect(hallway_B):
                    player_x = 380
                    player_y = 426
                    player = player_sprites[3]
                    backgrounds = bathroom
                #Living Room
                elif backgrounds == living_room and player_collision.colliderect(living_room_door_H):
                    player_x = 235
                    player_y = 340
                    player = player_sprites[2]
                    backgrounds = hallway
                elif backgrounds == living_room and player_collision.colliderect(living_room_door_K):
                    player_x = 125
                    player_y = 430
                    player = player_sprites[3]
                    backgrounds = kitchen
                #Kitchen
                elif backgrounds == kitchen and player_collision.colliderect(kitchen_L):
                    player_x = 110
                    player_y = 10
                    player = player_sprites[0]
                    backgrounds = living_room
                elif backgrounds == kitchen and player_collision.colliderect(kitchen_D):
                    player_x = 110
                    player_y = 432
                    player = player_sprites[3]
                    backgrounds = dining_room
                #Dining Room
                elif backgrounds == dining_room and player_collision.colliderect(dining_room_K):
                    player_x = 140
                    player_y = 10
                    player = player_sprites[0]
                    backgrounds = kitchen
                #Room2
                elif backgrounds == Room2 and player_collision.colliderect(Room2_H):
                    player_x = 232
                    player_y = 190
                    player = player_sprites[2]
                    backgrounds = hallway
                #Room1
                elif backgrounds == Room1 and player_collision.colliderect(Room1_H):
                    player_x = 232
                    player_y = 75
                    player = player_sprites[2]
                    backgrounds = hallway
                #Bathroom
                elif backgrounds == bathroom and player_collision.colliderect(bathroom_H):
                    player_x = 305
                    player_y = 15
                    player = player_sprites[0]
                    backgrounds = hallway


        #Initializing key state
        if evnt.type == KEYUP:
            if evnt.key == K_LEFT:
                KEY_LEFT = False
            if evnt.key == K_RIGHT:
                KEY_RIGHT = False
            if evnt.key == K_UP:
                KEY_UP = False
            if evnt.key == K_DOWN:
                KEY_DOWN = False

    # Updating player collision
    player_collision = Rect(player_x, player_y, 64, 64)

    if KEY_LEFT:
        player = player_sprites[1]
        predicted_collision = player_collision.move(-player_speed * 1.5, 0)

        #Outdoor
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_x >= -10:
                    player = player_sprites[1]
                    player_x -= player_speed

        #Hallway
        elif backgrounds == hallway:
            if not predicted_collision.colliderect(drawer_H) and player_x >= 230:
                player = player_sprites[1]
                player_x -= player_speed

        #Living Room
        elif backgrounds == living_room:
            if not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_x >= -10:
                player = player_sprites[1]
                player_x -= player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_x >= -10:
            player = player_sprites[1]
            player_x -= player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_x >= -10:
            player = player_sprites[1]
            player_x -= player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_x >= -10:
            player = player_sprites[1]
            player_x -= player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_x >= -10:
            player = player_sprites[1]
            player_x -= player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_x >= 173:
            player = player_sprites[1]
            player_x -= player_speed


    if KEY_RIGHT:
        player = player_sprites[2]
        predicted_collision = player_collision.move(player_speed, 0)

        #Outdoor
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_x <= 745:
                player = player_sprites[2]
                player_x += player_speed

        #Hallway
        elif backgrounds == hallway:
            if not predicted_collision.colliderect(drawer_H) and player_x <= 500:
                player = player_sprites[2]
                player_x += player_speed

        #Living Room
        elif backgrounds == living_room:
            if not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_x <= 740:
                player = player_sprites[2]
                player_x += player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_x <= 740:
            player = player_sprites[2]
            player_x += player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_x <= 740:
            player = player_sprites[2]
            player_x += player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_x <= 740:
            player = player_sprites[2]
            player_x += player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_x <= 740:
            player = player_sprites[2]
            player_x += player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_x <= 585:
            player = player_sprites[2]
            player_x += player_speed


    if KEY_UP:
        player = player_sprites[3]
        predicted_collision = player_collision.move(0, -player_speed * 1.7)

        #Outdoor
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_y >= 0:
                player = player_sprites[3]
                player_y -= player_speed

        #Hallway
        elif backgrounds == hallway:
            if not predicted_collision.colliderect(drawer_H) and player_y >= 5:
                player = player_sprites[3]
                player_y -= player_speed

        #Living Room
        elif backgrounds == living_room:
            if not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_y >= 5:
                player = player_sprites[3]
                player_y -= player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_y >= 5:
            player = player_sprites[3]
            player_y -= player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_y >= 5:
            player = player_sprites[3]
            player_y -= player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_y >= 5:
            player = player_sprites[3]
            player_y -= player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_y >= 5:
            player = player_sprites[3]
            player_y -= player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_y >= 5:
            player = player_sprites[3]
            player_y -= player_speed

    if KEY_DOWN:
        player = player_sprites[0]
        predicted_collision = player_collision.move(0, player_speed)

        #Outdoor
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_y <= 430:
               player = player_sprites[0]
               player_y += player_speed

        #Hallway
        elif backgrounds == hallway and player_y <= 426:
            if not predicted_collision.colliderect(drawer_H) and player_y <= 426:
                player = player_sprites[0]
                player_y += player_speed

        #Living Room
        elif backgrounds == living_room and player_y <= 426:
            if not predicted_collision.colliderect(bookshelf_L) and not predicted_collision.colliderect(couch) and not predicted_collision.colliderect(chip_table) and not predicted_collision.colliderect(TV) and player_y <= 426:
                player = player_sprites[0]
                player_y += player_speed

        #Kitchen
        elif backgrounds == kitchen and not predicted_collision.colliderect(kitchen_table_1) and not predicted_collision.colliderect(kitchen_table_2) and not predicted_collision.colliderect(kitchen_table_3_1) and not predicted_collision.colliderect(kitchen_table_3_2) and not predicted_collision.colliderect(garbage) and player_y <= 426:
            player = player_sprites[0]
            player_y += player_speed

        #Dining Room
        elif backgrounds == dining_room and not predicted_collision.colliderect(dining_table) and player_y <= 426:
            player = player_sprites[0]
            player_y += player_speed

        #Room2
        elif backgrounds == Room2 and not predicted_collision.colliderect(room2_table) and not predicted_collision.colliderect(room2_drawer) and not predicted_collision.colliderect(room2_bookshelf) and player_y <= 426:
            player = player_sprites[0]
            player_y += player_speed

        #Room1
        elif backgrounds == Room1 and not predicted_collision.colliderect(room1_table) and not predicted_collision.colliderect(room1_drawer) and not predicted_collision.colliderect(treasure) and player_y <= 426:
            player = player_sprites[0]
            player_y += player_speed

        #Bathroom
        elif backgrounds == bathroom and not predicted_collision.colliderect(sink) and not predicted_collision.colliderect(bathtub) and not predicted_collision.colliderect(toilet) and player_y <= 426:
            player = player_sprites[0]
            player_y += player_speed

    drawScreen()
    display.flip()
    myClock.tick(60)

quit()
