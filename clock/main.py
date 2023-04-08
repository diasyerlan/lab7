import pygame
import time
import math

pygame.init()

size = (829, 836)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Clock")

watch_image = pygame.image.load('clock/images/body.jpeg')
minute_image = pygame.image.load('clock/images/right.png')
second_image = pygame.image.load('clock/images/left.png')

minute_image = pygame.transform.rotate(minute_image, 90)
second_image = pygame.transform.rotate(second_image, 90)

minute_angle = 0
second_angle = 0

running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill((255, 255, 255))
    
    screen.blit(watch_image, (0, 0))
    
    current_time = time.localtime()
    current_minute = current_time.tm_min
    current_second = current_time.tm_sec
    
    minute_angle = 360 - (6 * current_minute)
    minute_rotated = pygame.transform.rotate(minute_image, minute_angle)
    minute_pos = ((size[0] - minute_rotated.get_width()) // 2, (size[1] - minute_rotated.get_height()) // 2)
    screen.blit(minute_rotated, minute_pos)
    
    second_angle = 360 - (6 * current_second)
    second_rotated = pygame.transform.rotate(second_image,second_angle)
    second_pos = ((size[0] - second_rotated.get_width()) // 2, (size[1] - second_rotated.get_height()) // 2)
    screen.blit(second_rotated, second_pos)
    
    pygame.display.flip()
    
pygame.quit()
    
    