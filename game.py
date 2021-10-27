import pygame, sys
from pygame.locals import *


pygame.init()

size = width, height = 500, 500
speed = [2, 2]
white = 255, 255, 255

x = 50
y = 50

screen = pygame.display.set_mode(size)
pygame.display.set_caption("Waddup bitch")


while True: 
    pygame.time.delay(75)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        x = x-25
        if x < 0:
            x = 500
    elif keys[pygame.K_RIGHT]:
        x = x+25
        if x > 500:
            x = 0
    elif keys[pygame.K_UP]:
        y = y-25
        if y < 0:
            y = 500
    elif keys[pygame.K_DOWN]:
        y = y+25
        if y > 500:
            y = 0


    screen.fill(white)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 35)
    pygame.draw.rect(screen, (0, 0, 0), (500, 20, 500, 20))
    pygame.display.update()