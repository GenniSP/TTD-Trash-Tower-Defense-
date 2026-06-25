import pygame


pygame.init()
pygame.mixer.init()

playlist = ["song_1.ogg", "song_2.mp3", "song_3.mp3"]
canzone_suonata= 0

pygame.mixer.music.load(playlist[canzone_suonata])
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play()

clock = pygame.time.Clock()

while True:
    if not pygame.mixer.music.get_busy():
        canzone_suonata = canzone_suonata + 1
        if canzone_suonata >= len(playlist):
            canzone_suonata = 0
        pygame.mixer.music.load(playlist[canzone_suonata])
        pygame.mixer.music.play()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    clock.tick(10)
