from csv import reader
from settings import Tile_size
import pygame

def import_csv_layout(path):
    terrain_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:            
            terrain_map.append(list(row))            
        return terrain_map


def import_cut_graph(path):
    surface = pygame.image.load(path).convert_alpha()
    tile_num_x = int(surface.get_size()[0] / Tile_size)
    tile_num_y = int(surface.get_size()[1] / Tile_size)
    
    cut_tiles = []
    for row in range(tile_num_y):
        for col in range(tile_num_x):
            x = col * Tile_size
            y = row * Tile_size
            new_surface = pygame.Surface((Tile_size,Tile_size))
            new_surface.blit(surface,(0,0),pygame.Rect(x,y,Tile_size,Tile_size))
            pygame.draw.rect(new_surface,(255,255,255),pygame.Rect(x,y,Tile_size,Tile_size),2)
            cut_tiles.append(new_surface)            
    
        
            
    return cut_tiles        
    
        