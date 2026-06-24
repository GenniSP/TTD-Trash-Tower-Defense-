import pygame
import random

startValue02 = 210
startValue1 = 250

pos_x_0 = 450/5.7
pos_y_0 = startValue02
pos_x_1 = 450/1.9
pos_y_1 = startValue1
pos_x_2 = 450/1.15
pos_y_2 = startValue02
shift_y = 2
active = False
choice = None

def move_monster(screen, height):
    global pos_y_0, pos_y_1, pos_y_2, choice, active
    if not active:
        choice = random.randint(0, 2)
        active = True
    else:
        match choice:
            case 0:
                pygame.draw.circle(screen, pygame.Color("red"),(pos_x_0,pos_y_0),30,15)
                pos_y_0+=shift_y
            case 1:
                pygame.draw.circle(screen, pygame.Color("red"),(pos_x_1,pos_y_1),30,15)
                pos_y_1+=shift_y
            case 2:
                pygame.draw.circle(screen, pygame.Color("red"),(pos_x_2,pos_y_2),30,15)
                pos_y_2+=shift_y
        if pos_y_0 > height or pos_y_1 > height or pos_y_2 > height:
            pos_y_0 = startValue02
            pos_y_2 = startValue02
            pos_y_1 = startValue1
            active = False