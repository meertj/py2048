# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : JJM
# Created Date: Wed Dec  8 21:20:22 2021
# version ='1.0'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
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
        
class Tile(pygame.sprite.Sprite):
    def __init__(self, image_file, speed, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (106, 106)) 
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        
        
BackGround = Background('Board.png', [0,0])
Tile2 = Tile("Tile2.png", 0, [0, 0])
Tile4 = Tile("Tile4.png", 0, [0, 0])
Tile8 = Tile("Tile8.png", 0, [0, 0])
Tile16 = Tile("Tile16.png", 0, [0, 0])
Tile32 = Tile("Tile32.png", 0, [0, 0])
Tile64 = Tile("Tile64.png", 0, [0, 0])
Tile128 = Tile("Tile128.png", 0, [0, 0])
Tile256 = Tile("Tile256.png", 0, [0, 0])
Tile512 = Tile("Tile512.png", 0, [0, 0])
Tile1024 = Tile("Tile1024.png", 0, [0, 0])
Tile2048 = Tile("Tile2048.png", 0, [0, 0])

# Tiles in the game space are as follows

tile2pixelRow = { 0 : 15, 1 : 137, 2 : 257, 3 : 377 }
tile2pixelCol = { 0 : 15, 1 : 140, 2 : 260, 3 : 380 }

# tile2pixelCol
# # Just doing this for readability
# Mat2Tile[(0, 0)] = [15, 15]
# Mat2Tile[(0, 1)] = [137, 15]
# Mat2Tile[(0, 2)] = [257, 15]
# Mat2Tile[(0, 3)] = [377, 15]


#                                     15  137  257  377  
# 01 02 03 04                   15  | 
# 05 06 07 08  --\  Pixel  --\  140 |
# 09 10 11 12  --/  Space  --/  260 |
# 13 14 15 16                   380 |


while True: # main game loop
    DISPLAYSURF.fill([255, 255, 255])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)
    
    # Traverse current matrix while or double for loops O(1) space
    if entry != 0:
        # Check this tile and map to the correct png
        # Map tile location to pixel space
        # Insert image onto board at mapped space
        
        # -> blit these to the board
    DISPLAYSURF.blit(Tile2.image, [tile2pixelRow[tileRow], tile2pixelCol[tileCol]])
    DISPLAYSURF.blit(Tile2.image, [15, 138])


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()