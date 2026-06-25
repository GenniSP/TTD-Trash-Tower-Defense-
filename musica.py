import pygame
import time

pygame.mixer.init()


playlist = ["peppe1.mp3", "Sayonara Fujisan.mp3", "Tokyo Reggie.mp3"]
indice_canzone = 0

# Fai partire la prima canzone
pygame.mixer.music.load(f"musica/{playlist[indice_canzone]}")
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
        print(f"Nuova canzone partita: {playlist[indice_canzone]}")

    
    time.sleep(1) 



