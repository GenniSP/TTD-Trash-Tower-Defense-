import pygame


pygame.init()
pygame.mixer.init()

playlist = ["song_1.ogg", "song_2.mp3", "song_3.mp3"]
canzone_suonata= 0

pygame.mixer.music.load(playlist[canzone_suonata])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()


gioco_in_corso = True
while gioco_in_corso:
    
    
    if not pygame.mixer.music.get_busy(): 
        
        indice_canzone = indice_canzone + 1
        
        
        if indice_canzone >= len(playlist):
            indice_canzone = 0
            
        
        pygame.mixer.music.load(playlist[indice_canzone])
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(10)
