import pygame
import fun
import carte
import enemy_module
import health_bar
import health_bar_alleati
import card_text
import ps
import good

# initialize the environment
pygame.init()

# define the screen size
sizeX = 450
sizeY = 800
cSizeX = 137
cSizeY = 216


counter = -1
next_enemy_counter = 0

global last_toggle_all
last_toggle_all=0
global now_ms
global current_image
current_image=1

# Enable GPU acceleration with hardware surface and double buffering
myScreen = pygame.display.set_mode((sizeX, sizeY), pygame.HWSURFACE | pygame.DOUBLEBUF,display=0)
pygame.display.set_caption('TTD')

# custom background (convert to GPU-optimized format)
background = pygame.image.load('assets/background1.png') 
# fit to window size
background = pygame.transform.scale(background, (sizeX, sizeY))
background = background.convert()  # Optimize for GPU

# Preload and cache card images (GPU-optimized)
card_images_cache = {}
for tipo in [0, 1, 2]:
    img_path = ['assets/carta_debole.png', 'assets/carta_media.png', 'assets/carta_forte.png'][tipo]
    img = pygame.image.load(img_path)
    img_scaled = pygame.transform.scale(img, (cSizeX, cSizeY))
    card_images_cache[tipo] = img_scaled.convert()  # Optimize for GPU

game_font=pygame.font.Font(None,45)

carte_disp=True

lista_correnti=carte.make_list_cards()
tempo=0
tempo_change=0

game=True
mana=69
ck=pygame.time.Clock() 
passed=0
inizio_passed_carte=-1
mana_time=-1
mana_text_temp=pygame.font.Font(None,25)
not_enough=mana_text_temp.render(f"Not enough Mana!",True,(255,255,255))
ask_pos=False
def_pos=-1
lista_alleati=[]
x=-2

while game:
    next_enemy_counter += 1
    tempo_change=ck.tick(60) #imposto 60 fps e ottengo in passed quanto tempo è passato dall'ultimo frame
    passed+=tempo_change
    tempo+=tempo_change

    if carte_disp:
        inizio_passed_carte=tempo
    
    if passed>=7200:
        if mana<32:
            mana+=4
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
                if x != -1:
                    if lista_correnti[x].costo<=mana:
                        mana-=lista_correnti[x].costo
                        carte_disp=False
                        print(x)
                        current_charachter=lista_correnti[x]

                        ask_pos=True

                        print("pos: "+str(pos))
                    else:
                        print("not enough mana")
                        mana_time=900
                else: print("card not selected")

            def_pos=-1
            if ask_pos:
                if mouse_xPos<=102 and mouse_yPos<=554 and mouse_yPos>=510 and mouse_xPos>=58:
                    def_pos=0
                    ask_pos=False
                if mouse_xPos<=252 and mouse_yPos<=554 and mouse_yPos>=510 and mouse_xPos>=208:   
                    def_pos=1
                    ask_pos=False
                if mouse_xPos<=406 and mouse_yPos<=554 and mouse_yPos>=510 and mouse_xPos>=362:
                    def_pos=2
                    ask_pos=False
                




    if def_pos!=-1:
        temp=good.Alleato(lista_correnti[x],def_pos,532)
        lista_alleati.append(temp)
        def_pos=-1






        
    health_bar.draw_health_bar(myScreen)
    health_bar_alleati.draw_health_bar(myScreen)

    if ask_pos:
        ps.draw_pos(myScreen)

    if mana_time>0:
        mana_time-=tempo_change
        myScreen.blit(not_enough,(151,540))





    if carte_disp:
        vertice_x=8
        for i in range(3):
            # Use cached GPU-optimized card images
            carta_scaled = card_images_cache[lista_correnti[i].tipo]
            myScreen.blit(carta_scaled,(vertice_x,575))
            vertice_x+=149



    if not carte_disp and tempo-inizio_passed_carte>=5000:
        carte_disp=True
        lista_correnti=carte.make_list_cards()

    if next_enemy_counter > counter:
        counter = enemy_module.choose_position()
        next_enemy_counter = 0


    if carte_disp == True:
        for i in range(3):
            card_text.draw_card_values(myScreen, lista_correnti[i], i)


    enemy_module.attack_sq(lista_alleati)
    
    health_loss = enemy_module.move_monster(myScreen, sizeY-cSizeY-40)
    health_bar_alleati.apply_health_loss(health_loss)



    for el in lista_alleati:
        el.pos-=0.5
        if el.vita<=0:
            lista_alleati.remove(el)
            continue
        image=None
        now_ms = pygame.time.get_ticks()
        if el.carta.tipo==2:
            if now_ms - last_toggle_all >= 200:
                last_toggle_all = now_ms
                current_image = 2 if current_image == 1 else 1
            if current_image==1:
                image=pygame.image.load("assets/buoni/mago_forte/design/mago_movimento_1.png")
            else: image=pygame.image.load("assets/buoni/mago_forte/design/mago_movimento_2.png")

        if el.carta.tipo==0:
            if now_ms - last_toggle_all >= 200:
                last_toggle_all = now_ms
                current_image = 2 if current_image == 1 else 1
            if current_image==1:
                image=pygame.image.load("assets/buoni/gufo_debole/design/gufo_movimento_1.png")
            else: image=pygame.image.load("assets/buoni/gufo_debole/design/gufo_moviment_2.png")

        if el.carta.tipo==1:
            image=pygame.image.load("assets/buoni/rana/rana.png")

        
        # Check if ally reached top of screen (80px from top)
        if el.pos <= 150:
            # Deal damage based on card power
            health_bar.current_health -= el.carta.power * 10
            lista_alleati.remove(el)
            continue
        

        image=pygame.transform.scale(image,(60,70))
        x_ponte=-1
        if el.ponte==0:
            x_ponte=49
        if el.ponte==1:
            x_ponte=208
        if el.ponte==2:
            x_ponte=358
        myScreen.blit(image,(x_ponte,el.pos))




    pygame.display.flip() #ricarica con il mana
    myScreen.blit(background, (0, 0)) #fai ritornare il background




