import pygame
import random
import time

class Enemy:
    def __init__(self, x, y, anim):
        self.x = x
        self.y = y
        self.anim = anim

startValue02 = 210
startValue1 = 250

enemies = []

pos_x_0 = 450/5.7
pos_y_0 = startValue02
pos_x_1 = 450/1.9
pos_y_1 = startValue1
pos_x_2 = 450/1.15
pos_y_2 = startValue02
shift_y = 0.5

def move_monster(screen, height):
    for i, enemy in enumerate(enemies):
        match enemy.anim:
            case 1:
                pass #first animation
                enemies[i].anim = 2
            case 2:
                pass #second animation
                enemies[i].anim = 1
        pygame.draw.circle(screen, pygame.Color("red"),(enemy.x,enemy.y),30,15)
        enemies[i].y += shift_y
        if enemy.y > height:
            del enemies[i]

def choose_position():
    choice = random.randint(0, 2)
    match choice:
        case 0:
            enemies.append(Enemy(pos_x_0, pos_y_0, 1))
        case 1:
            enemies.append(Enemy(pos_x_1, pos_y_1, 1))
        case 2:
            enemies.append(Enemy(pos_x_2, pos_y_2, 1))
    return random.randint(100, 200)