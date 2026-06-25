import pygame
import random

# Load and cache fungus images
mushroom_image_1 = pygame.image.load('assets/funghetto_corsa_1.png')
mushroom_image_1 = pygame.transform.scale(mushroom_image_1, (65, 65))
mushroom_image_2 = pygame.image.load('assets/funghetto_corsa_2.png')
mushroom_image_2 = pygame.transform.scale(mushroom_image_2, (65, 65))

class Enemy:
    def __init__(self, x, y,):
        self.x = x
        self.y = y
        self.vita=random.randint(8,12)

startValue02 = 210
startValue1 = 250

enemies = []
enemy_limit = 3
enemy_cooldown = 0

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

ponti= {
    pos_x_0:0,
    pos_x_1:1,
    pos_x_2:2
}
def attack_sq(alleati):
    for nemico in enemies:
        for alleato in alleati:
            if ponti[nemico.x]==alleato.ponte and abs(nemico.y-alleato.pos)<=15:
                nemico.y-=15
                alleato.pos+=15
                nemico.vita-=alleato.carta.power
                alleato.vita-=2.5




def move_monster(screen, height):
    global last_toggle_ms, current_image
    loss = 0
    now_ms = pygame.time.get_ticks()
    if now_ms - last_toggle_ms >= 200:
        last_toggle_ms = now_ms
        current_image = 2 if current_image == 1 else 1

    mushroom_img = mushroom_image_1 if current_image == 1 else mushroom_image_2

    for enemy in enemies:
        if enemy.vita<=0:
            enemies.remove(enemy)
            continue
        screen.blit(
            mushroom_img,
            (enemy.x - mushroom_img.get_width() / 2, enemy.y - mushroom_img.get_height() / 2),
        )
        enemy.y += shift_y
        if enemy.y > height:
            enemies.remove(enemy)
            loss = 1
    return loss


def choose_position():
    if len(enemies) < enemy_limit:
        choice = random.randint(0, 2)
        match choice:
            case 0:
                enemies.append(Enemy(pos_x_0, pos_y_0))
            case 1:
                enemies.append(Enemy(pos_x_1, pos_y_1))
            case 2:
                enemies.append(Enemy(pos_x_2, pos_y_2))
        global enemy_cooldown
        enemy_cooldown = random.randint(100, 1000)
        return enemy_cooldown
    else: return enemy_cooldown