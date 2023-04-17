import pygame
from settings import vertical_title_number,Tile_size,screen_width,screen_height

class background:
    def __init__(self,horizon):
        self.background = pygame.image.load('asset/tileset/Background/Background.png').convert()           
        self.background = pygame.transform.scale(self.background,(screen_width,screen_height))
        self.horizon = horizon     
    
    def draw(self,surface):
        surface.blit(self.background,(0,0))