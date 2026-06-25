import pygame
import random

# Load and cache fungus images
mushroom_image_1 = pygame.image.load('assets/funghetto_corsa_1.png')
mushroom_image_1 = pygame.transform.scale(mushroom_image_1, (65, 65))
mushroom_image_2 = pygame.image.load('assets/funghetto_corsa_2.png')
mushroom_image_2 = pygame.transform.scale(mushroom_image_2, (65, 65))

class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

# Animation timer for mushroom alternation every 200ms
last_toggle_ms = pygame.time.get_ticks()
current_image = 1


def move_monster(screen, height):
    global last_toggle_ms, current_image
    now_ms = pygame.time.get_ticks()
    if now_ms - last_toggle_ms >= 200:
        last_toggle_ms = now_ms
        current_image = 2 if current_image == 1 else 1

    mushroom_img = mushroom_image_1 if current_image == 1 else mushroom_image_2

    for i, enemy in enumerate(enemies):
        screen.blit(
            mushroom_img,
            (enemy.x - mushroom_img.get_width() / 2, enemy.y - mushroom_img.get_height() / 2),
        )
        enemies[i].y += shift_y
        if enemy.y > height:
            del enemies[i]

def choose_position():
    choice = random.randint(0, 2)
    match choice:
        case 0:
            enemies.append(Enemy(pos_x_0, pos_y_0))
        case 1:
            enemies.append(Enemy(pos_x_1, pos_y_1))
        case 2:
            enemies.append(Enemy(pos_x_2, pos_y_2))
    return random.randint(100, 200)