import pygame
import sys

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((100, 20))

playlist = [
    'music_player/music/1.mp3',
    'music_player/music/2.mp3',
    'music_player/music/3.mp3'
]

current_track = 0

pygame.mixer.music.load(playlist[current_track])

pygame.mixer.music.set_volume(0.5)

pygame.mixer.music.play()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else: 
                    pygame.mixer.music.unpause()
            
            if event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
            
            if event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()
                
            if event.key == pygame.K_s:
                pygame.mixer.music.stop()
        
        
        pygame.time.wait(10)
            
            
            
            


