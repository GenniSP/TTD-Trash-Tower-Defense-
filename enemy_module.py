import pygame
import random


# Load and cache fungus images (scaled down to smaller size)
mushroom_image_1 = pygame.image.load('assets/funghetto_corsa_1.png')
mushroom_image_2 = pygame.image.load('assets/funghetto_corsa_2.png')
# Scale down to 40x40 pixels for smaller mushrooms
mushroom_image_1 = pygame.transform.scale(mushroom_image_1, (65, 65))
mushroom_image_2 = pygame.transform.scale(mushroom_image_2, (65, 65))

startValue02 = 210
startValue1 = 250

pos_x_0 = 450/5.7
pos_y_0 = startValue02
pos_x_1 = 450/1.9
pos_y_1 = startValue1
pos_x_2 = 450/1.15
pos_y_2 = startValue02
shift_y = 0.45
active = False
choice = None

# Timer per alternare le immagini ogni 500ms
animation_timer = 0
current_image = 1  # 1 o 2


def move_monster(screen, height, delta_time=16):
    global pos_y_0, pos_y_1, pos_y_2, choice, active, animation_timer, current_image
    
    # Aggiorna il timer di animazione
    animation_timer += delta_time
    if animation_timer >= 200:  # 200ms per alternanza più veloce
        animation_timer = 0
        current_image = 2 if current_image == 1 else 1
    
    # Seleziona l'immagine corrente
    mushroom_img = mushroom_image_1 if current_image == 1 else mushroom_image_2
    
    if not active:
        choice = random.randint(0, 2)
        active = True
    else:
        match choice:
            case 0:
                screen.blit(mushroom_img, (pos_x_0 - mushroom_img.get_width() / 2, pos_y_0 - mushroom_img.get_height() / 2))
                pos_y_0 += shift_y
            case 1:
                screen.blit(mushroom_img, (pos_x_1 - mushroom_img.get_width() / 2, pos_y_1 - mushroom_img.get_height() / 2))
                pos_y_1 += shift_y
            case 2:
                screen.blit(mushroom_img, (pos_x_2 - mushroom_img.get_width() / 2, pos_y_2 - mushroom_img.get_height() / 2))
                pos_y_2 += shift_y
        if pos_y_0 > height or pos_y_1 > height or pos_y_2 > height:
            pos_y_0 = startValue02
            pos_y_2 = startValue02
            pos_y_1 = startValue1
            active = False