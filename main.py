import pygame
import fun

# initialize the environment
pygame.init()

# define the screen size
sizeX = 450
sizeY = 800
cSizeX = 137
cSizeY = 216

myScreen= pygame.display.set_mode((sizeX, sizeY))
pygame.display.set_caption('DTT')

# custom background
background = pygame.image.load('assets/background1.png') 
# fit to window size
background = pygame.transform.scale(background, (sizeX, sizeY))
myScreen.blit(background, (0, 0))

game_font=pygame.font.Font(None,45)

game=True
mana=0
ck=pygame.time.Clock() 
passed=0
while game:
    passed+=ck.tick(60) #imposto 60 fps e ottengo in passed quanto tempo è passato dall'ultimo frame
    if passed>=7200:
        mana+=2
        passed-=7200 #tolgo il tempo trascorso/non resetto a 0 altrimenti perderei probabiblmente qualche millisecondo
    mana_text=game_font.render(f"Mana: {mana}",True, (255,255,255))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # if clicked
            pos= pygame.mouse.get_pos()
            mouse_xPos = pos[0]
            mouse_yPos = pos[1]
            print(fun.click_card(mouse_xPos, mouse_yPos,sizeY,sizeX,cSizeX,cSizeY))
            
    myScreen.blit(mana_text,(315,10))
    pygame.display.flip() #ricarica con il mana
    myScreen.blit(background, (0, 0)) #fai ritornare il background




