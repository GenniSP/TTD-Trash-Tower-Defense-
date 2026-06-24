import pygame
import random
import time
import sys
pygame.init() 

# schermo
width = 225
height = 400
myScreen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Trash Tower Defense')
background = pygame.image.load('background1.png')
rect_top_left_x = 0
rect_top_left_y = 0
rect_width = 112.5
rect_height = 20
pygame.draw.rect(myScreen, pygame.Color('red'), 
              [rect_top_left_x, rect_top_left_y, 
               rect_width, rect_height])

pygame.display.flip()
5
#vita torri e cosa succede se muoiono
our_health = 100
enemy_health = 200
if enemy_health <= 0:
    print("Enemy defeated! You win!")

if our_health <= 0:
    print("You have been defeated! Game over!")
