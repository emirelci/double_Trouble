import pygame
from settings import screen_height

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        
        
        self.sprites_attack = []
        self.sprites_attack_left = []
        self.sprites_idle = []
        self.sprites_dead = []
        self.sprites_walking = []
        self.sprites_walking_left = []        
        
        for num in range(0,4):
            self.sprites_attack.append(pygame.image.load(f'asset/warriorCharacter/Warrior_2/attack/sprite_attack{num}.png'))    
            self.sprites_attack_left.append(pygame.transform.flip(self.sprites_attack[num],True,False))    
        for num in range(0,5):
            self.sprites_idle.append(pygame.image.load(f'asset/warriorCharacter/Warrior_2/idle/sprite_idle{num}.png')) 
        for num in range(0,4):
            self.sprites_dead.append(pygame.image.load(f'asset/warriorCharacter/Warrior_2/dead/sprite_dead{num}.png'))                   
        for num in range(0,8):
            self.sprites_walking.append(pygame.image.load(f'asset/warriorCharacter/Warrior_2/walking/sprite_walking{num}.png'))  
            self.sprites_walking_left.append(pygame.transform.flip(self.sprites_walking[num], True, False))              
        
                  
        self.image = pygame.Surface((50,100))
        self.image = self.sprites_idle[0]        
        self.rect  = self.image.get_rect(topleft = pos)        
        
        #Player Movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16                
        
    
    def get_input(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.direction.x = 1
        elif keys[pygame.K_a]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        
        if keys[pygame.K_SPACE]:
            self.jump()

        
    def fall_down_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y    
    
    def jump(self):
        self.direction.y = self.jump_speed       
   
    
    def update(self):  
        self.get_input()
        
                         
         
        
       
                
            
              
        
        
        
        
    