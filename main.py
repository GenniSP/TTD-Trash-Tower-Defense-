import pygame

# initialize the environment
pygame.init()

# define the screen size
sizeX = 450
sizeY = 800
myScreen= pygame.display.set_mode((sizeX, sizeY))
pygame.display.set_caption('DTT')

# custom background
background = pygame.image.load('background1.png') 
# fit to window size
background = pygame.transform.scale(background, (sizeX, sizeY))
myScreen.blit(background, (0, 0))

while True:
    pygame.display.flip()

x=0