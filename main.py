import os
import random
import math
import pygame
from settings import *
from level import Level
from game_data import level_0
from player import Player
from os import listdir
from os.path import isfile, join

pygame.init()
clock = pygame.time.Clock()
def event_ESC_pressed(get_pressed):
    if get_pressed[pygame.K_ESCAPE]:
        pygame.quit()
        exit()    

#Game Settings
pygame.display.set_caption("DoubleToubleShot")
screen = pygame.display.set_mode((screen_width,screen_height))
FPS = 60

#Level Settings
level = Level(level_0, screen)     

while True:         
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()                                                      
    
    level.run()
    pygame.display.update()
    clock.tick(FPS)
        
    event_ESC_pressed(pygame.key.get_pressed())
        
    

