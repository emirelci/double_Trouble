import pygame
from support import import_csv_layout
from settings import Tile_size
from tiles import Tile, StaticTile
from support import import_cut_graph
from bg import background
from player import Player

class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        
        terrain_layout = import_csv_layout(level_data['terrain'])    
        self.terrain_sprites = self.create_tile_group(terrain_layout, 'terrain')        
        self.sky = background(10)
      
        
    def create_tile_group(self, layout, type):
        sprite_group = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        
        #col = sütun && row = satır                 
        for row_index, row in enumerate(layout):
            for col_index,val in enumerate(row):
                if val != '-1':
                    x = col_index * Tile_size
                    y = row_index * Tile_size
                    
                    if type == 'terrain' and val != "85":
                        terrain_tile_list = import_cut_graph('asset/tileset/Tiles/Tileset.png')                        
                        tile_surface = terrain_tile_list[int(val)]
                        sprite = StaticTile(Tile_size, x, y,tile_surface)                        
                        sprite_group.add(sprite)
                    if val == '85':                        
                        player_sprite = Player((x,y))                        
                        self.player.add(player_sprite)                        
            
        return sprite_group             
                       
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        
        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    
    def vertical_movement_collision(self):
        player = self.player.sprite
        player.fall_down_gravity() 
        
        for sprite in self.terrain_sprites.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    
        
        
    def run(self):
        #run the entire game / level
        
        #Level Tiles        
        self.sky.draw(self.display_surface)              
        self.terrain_sprites.draw(self.display_surface)        
        
         
        #Player
        self.player.update()        
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)
        
        
        
    
    
    