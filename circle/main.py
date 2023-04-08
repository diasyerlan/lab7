import pygame
import sys

pygame.init()

screen_size = (400, 400)
screen = pygame.display.set_mode(screen_size)

white = (255, 255, 255)
red = (255, 0, 0)

ball_pos = [screen_size[0] // 2, screen_size[1] // 2]

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                ball_pos[1] -= 20
            
            if event.key == pygame.K_DOWN:
                ball_pos[1] += 20
            
            if event.key == pygame.K_RIGHT:
                ball_pos[0] += 20
            
            if event.key == pygame.K_LEFT:
                ball_pos[0] -= 20
    
    ball_pos[0] = max(25, min(ball_pos[0], screen_size[0] - 25))
    ball_pos[1] = max(25, min(ball_pos[1], screen_size[1] - 25))
    
    screen.fill(white)
    
    pygame.draw.circle(screen, red, ball_pos, 25)
    
    pygame.display.flip()
    
quit()
            
                
    
            