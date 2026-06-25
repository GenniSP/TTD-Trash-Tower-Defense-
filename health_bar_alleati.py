import pygame
import fun
import os
import subprocess
import sys

pygame.font.init()
max_health = 150
current_health = max_health

if current_health <= 0:
    subprocess.run(f'{sys.executable} youloose.py')

health_bar_x = 10
health_bar_y = 33
health_bar_width = 150
health_bar_height = 25

color_red = (0, 255, 0)
color_gray = (200, 200, 200)
color_black = (0, 0, 0)

game_font = pygame.font.Font(None, 25)  


def draw_health_bar(myScreen):
    current_width = (current_health / max_health) * health_bar_width
    
    pygame.draw.rect(myScreen, color_gray, 
                     (health_bar_x, health_bar_y, health_bar_width, health_bar_height))
    pygame.draw.rect(myScreen, color_red, 
                     (health_bar_x, health_bar_y, current_width, health_bar_height))
    pygame.draw.rect(myScreen, color_black, 
                     (health_bar_x, health_bar_y, health_bar_width, health_bar_height), 2)
    
    hp_text = game_font.render(str(current_health), True, color_black)
    text_rect = hp_text.get_rect(center=(health_bar_x + health_bar_width // 2, 
                                          health_bar_y + health_bar_height // 2))
    myScreen.blit(hp_text, text_rect)


def apply_health_loss(loss):
    global current_health
    if loss == 1:
        current_health = max(0, current_health - 25)

