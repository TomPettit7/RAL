import pygame
import random
import time
import math
from projectile import projectilemotion
from environmentsetup import envsetup
import sys

pygame.init()

p = int(input('Power: '))
a = int(input('Angle: '))
h = int(input('How long: '))

envsetup()
WINDOWWIDTH = 960
WINDOWHEIGHT = 480
BLACK = (0,0,0)
WHITE = (250,250,250)
basicFont = pygame.font.SysFont(None, 96)

clock = pygame.time.Clock()

environment = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
xstart = 480
ystart = 480
y_accel = 2
x_accel = 0
y_pos, x_pos, y_vel, x_vel = projectilemotion(p, a, h)
while True:
    y_vel += y_accel
    x_vel += x_accel
    y_pos += y_vel
    x_pos += x_vel
    environment.fill(BLACK)
    print("x_pos: " + str(x_pos))
    print("y_pos: "+ str(y_pos))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(1)
    #This then returns x_pos and y_pos
    bullet = pygame.Rect(x_pos, y_pos, 20, 20)
    pygame.draw.rect(environment, WHITE, bullet)

    target = pygame.Rect(900, 420, 60, 60) 
    pygame.draw.rect(environment, WHITE, target)

    if x_pos >= 960:
        out = basicFont.render('Out!', True, WHITE, BLACK)
        outRect = out.get_rect()
        outRect.centerx = environment.get_rect().centerx
        outRect.centery = environment.get_rect().centery
        environment.blit(out, outRect)
    if y_pos >= 480:
        out = basicFont.render('Out!', True, WHITE, BLACK)
        outRect = out.get_rect()
        outRect.centerx = environment.get_rect().centerx
        outRect.centery = environment.get_rect().centery
        environment.blit(out, outRect)
            
    if x_pos == target.left: #DOESN'T WORK
        hit = basicFont.render('Hit!', True, WHITE, BLACK)
        hitRect = hit.get_rect()
        hitRect.centerx = environment.get_rect().centerx
        hitRect.centery = environment.get_rect().centery
        environment.blit(hit, hitRect)

    pygame.display.update()
    clock.tick(5)


