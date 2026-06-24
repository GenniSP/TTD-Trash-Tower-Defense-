import pygame
import fun
import carte
import enemy_module

# initialize the environment
pygame.init()

# define the screen size
sizeX = 450
sizeY = 800
cSizeX = 137
cSizeY = 216

myScreen= pygame.display.set_mode((sizeX, sizeY),display=1)
pygame.display.set_caption('DTT')

# custom background
background = pygame.image.load('assets/background1.png') 
# fit to window size
background = pygame.transform.scale(background, (sizeX, sizeY))
myScreen.blit(background, (0, 0))

game_font=pygame.font.Font(None,45)

carte_disp=True

lista_correnti=carte.make_list_cards()
tempo=0
tempo_change=0

game=True
mana=0
ck=pygame.time.Clock() 
passed=0
inizio_passed_carte=-1
mana_time=-1
mana_text_temp=pygame.font.Font(None,25)
not_enough=mana_text_temp.render(f"Not enough Mana!",True,(255,255,255))

while game:
    tempo_change=ck.tick(60) #imposto 60 fps e ottengo in passed quanto tempo è passato dall'ultimo frame
    passed+=tempo_change
    tempo+=tempo_change

    if carte_disp:
        inizio_passed_carte=tempo
    
    if passed>=7200:
        if mana<32:
            mana+=2
        passed-=7150 #tolgo il tempo trascorso/non resetto a 0 altrimenti perderei probabiblmente qualche millisecondo
    mana_text=game_font.render(f"Mana: {mana}",True, (255,255,255))
    myScreen.blit(mana_text,(315,10))

    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN: # if clicked
            pos= pygame.mouse.get_pos()
            mouse_xPos = pos[0]
            mouse_yPos = pos[1]
            if carte_disp:
                x=fun.click_card(mouse_xPos, mouse_yPos,sizeY,sizeX,cSizeX,cSizeY)
                print(x)
                if lista_correnti[x].costo<=mana:
                    mana-=lista_correnti[x].costo
                    carte_disp=False
                else: 
                    print("not enough mana")
                    mana_time=900
                    
            else: print("cards not available")
            #aggiungi sistema di riconoscimento carta

    if mana_time>0:
        mana_time-=tempo_change
        myScreen.blit(not_enough,(151,540))





    if carte_disp:
        immagine=None
        vertice_x=8
        for i in range(3):
            if lista_correnti[i].tipo==0:
                immagine=pygame.image.load("assets/carta_debole.png")
            if lista_correnti[i].tipo==1:
                immagine=pygame.image.load("assets/carta_media.png")
            if lista_correnti[i].tipo==2:
                immagine=pygame.image.load("assets/carta_forte.png")

            carta_scaled=pygame.transform.scale(immagine,(137,216))
            myScreen.blit(carta_scaled,(vertice_x,575))
            vertice_x+=149



    if not carte_disp and tempo-inizio_passed_carte>=5000:
        carte_disp=True
        lista_correnti=carte.make_list_cards()
        
    enemy_module.move_monster(myScreen, sizeY-cSizeY-30)

            
    pygame.display.flip() #ricarica con il mana
    myScreen.blit(background, (0, 0)) #fai ritornare il background




