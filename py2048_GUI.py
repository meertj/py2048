# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 21:20:22 2021

@author: meert
"""

import pygame, sys
from pygame.locals import *

pygame.init()

DISPLAYSURF = pygame.display.set_mode((500, 500))

#pygame.display.set_mode()


pygame.display.set_caption('Hello World!')

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file).convert_alpha()
        self.image = pygame.transform.scale(self.image, (499, 500)) 
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
class Ship(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        
BackGround = Background('Board.png', [0,0])
# ship = Ship("images\ship.png", [a, b])




while True: # main game loop
    DISPLAYSURF.fill([255, 255, 255])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)
    # DISPLAYSURF.blit(ship.image, ship.rect)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()