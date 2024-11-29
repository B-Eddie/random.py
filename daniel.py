from pygame import *
import random

init()

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
char_forward = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (1).png")
char_left = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (3) (1) (1).png")
char_right = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (3) (1) (1) (1).png")
char_back = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\image (1) (1).png")

#Doubling character size
char_forward = transform.scale(char_forward, (char_forward.get_width() * 2, char_forward.get_height() * 2))
char_left = transform.scale(char_left, (char_left.get_width() * 2, char_left.get_height() * 2))
char_right = transform.scale(char_right, (char_right.get_width() * 2, char_right.get_height() * 2))
char_back = transform.scale(char_back, (char_back.get_width() * 2, char_back.get_height() * 2))

#Backgrounds
outdoor = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\Outdoor.png")
hallway = image.load("C:\\Users\\2linm\\PycharmProjects\\PythonProject\\pygame files\\image (1) (1)\\New Piskel.png")

#Character Sprites
player_sprites = [char_forward, char_left, char_right, char_back]

#Initializing starting sprite
player = player_sprites[0]

#Initializing starting location
player_x = 360
player_y = 400

#Player speed
player_speed = 1.4

#Background list
backgrounds = [outdoor, hallway]

backgrounds = backgrounds[0]

#Font
my_font = font.Font(None, 20)
WHITE = (255, 255, 255)

#Interact text
start_text = my_font.render("There's been some suspicious activity around the Howard house, best to investigate", True, WHITE)
my_text = my_font.render("Press E to interact", True, WHITE)

#Object hit boxes
house_door = Rect(320, 100, 120, 20)
house_door_H = Rect(320, 440, 120, 20)
house_rect = Rect(145, 0, 495, 95)
living_room_door = Rect(230, 290, 10, 100)
tree1 = Rect(110, 175, 80, 80)
tree2 = Rect(568, 155, 60, 78)

# Player hit box
player_collision = Rect(player_x, player_y, 64, 64)


def drawScreen():
    screen.blit(backgrounds, (0, 0))
    if backgrounds == outdoor:
        screen.blit(start_text, (130, 470))
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(house_door):
            screen.blit(my_text, (340, 100))

    if backgrounds == hallway:
        screen.blit(player, (player_x, player_y))
        if player_collision.colliderect(living_room_door):
            screen.blit(my_text, (185, 300))
        elif player_collision.colliderect(house_door_H):
            screen.blit(my_text, (336, 480))

    display.flip()

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
                if backgrounds == outdoor and player_collision.colliderect(house_door):
                    player_x = 360
                    player_y = 430
                    backgrounds = hallway
                elif backgrounds == hallway and player_collision.colliderect(living_room_door):
                    print("Living Room")
                elif backgrounds == hallway and player_collision.colliderect(house_door_H):
                    player_x = 360
                    player_y = 120
                    backgrounds = outdoor

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
        predicted_collision = player_collision.move(-player_speed * 1.5, 0)
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_x >= -10:
                    player = player_sprites[1]
                    player_x -= player_speed
        elif backgrounds == hallway and player_x >= 230:
            player = player_sprites[1]
            player_x -= player_speed

    if KEY_RIGHT:
        predicted_collision = player_collision.move(player_speed, 0)
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_x <= 745:
                player = player_sprites[2]
                player_x += player_speed
        elif backgrounds == hallway and player_x <= 500:
            player = player_sprites[2]
            player_x += player_speed


    if KEY_UP:
        predicted_collision = player_collision.move(0, -player_speed * 1.7)
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_y >= 0:
                player = player_sprites[3]
                player_y -= player_speed
        elif backgrounds == hallway and player_y >= 0:
            player = player_sprites[3]
            player_y -= player_speed

    if KEY_DOWN:
        predicted_collision = player_collision.move(0, player_speed)
        if backgrounds == outdoor:
            if not predicted_collision.colliderect(house_rect) and not predicted_collision.colliderect(tree1) and not predicted_collision.colliderect(tree2) and player_y <= 430:
               player = player_sprites[0]
               player_y += player_speed
        elif backgrounds == hallway and player_y <= 432:
            player = player_sprites[0]
            player_y += player_speed

    drawScreen()
    display.flip()
    myClock.tick(60)

quit()
