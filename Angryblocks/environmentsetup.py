import pygame
import time

power = 0
environment = 0
def envsetup():
    global power
    global environment
    BLACK = (0,0,0)
    WHITE = (250,250,250)
    WINDOWWIDTH = 480
    WINDOWHEIGHT = 480
    environment = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    basicFont = pygame.font.SysFont(None, 96)
    powerdisplay = basicFont.render(str(power), True, WHITE, BLACK)
