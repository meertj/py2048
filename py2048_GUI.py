# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : JJM
# Created Date: Wed Dec  8 21:20:22 2021
# version ='1.0'
# ---------------------------------------------------------------------------
""" GUI version of py2048 """
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
import sys
import pygame
from pygame.locals import *
from utils2048 import moveUpDown, moveLeftRight, randEntry, printGameDetails, checkTermination
import copy

# TODOs
# Fix locations of tiles

## Sprites used in this pygame - class definitions
class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
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
 
def update(dt, board, score):
    ## INPUTS: dt - time since last update, board - current state of board matrix,
    ##         score - current score
    ## OUTPUTS: runGame - variable to continue the main game loop, callDraw - 
    ##          has anything on the board changed?
    
    # Need to keep track of initial board (might be more space efficient to do
    # this using the score variable, but a copy of the board doesn't require much
    # memory anyways **shrug**)
    oldBoard = copy.deepcopy(board)
    
    # Reset bools for return
    runGame = True
    callDraw = False
    
    # Loop through events that passed to the script by player
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        sys.exit()
      else:
          keystate = pygame.key.get_pressed()
          # I would put in a switch/case statement here if doing in C++/MATLAB etc
          if keystate[pygame.K_UP]:
              board, score = moveUpDown(board, score, 1)
          elif keystate[pygame.K_DOWN]:
              board, score = moveUpDown(board, score, 0)
          elif keystate[pygame.K_RIGHT]:
              board, score = moveLeftRight(board, score, 0)
          elif keystate[pygame.K_LEFT]:
              board, score = moveLeftRight(board, score, 1)
              
      # Check to see if anything changed
      if oldBoard != board:   
          # Update board with the new entry
          board = randEntry(board)
          # Set callDraw to True so this is reflected in the pyGame window
          callDraw = True
      else:
        if checkTermination(board):
            runGame = False
            # TODO differentiate between term criteria
            
    return runGame, callDraw
                      
   
def draw(board, screen, score, values2tiles):
    """ Writes board background and tiles to the pygame window, also updates
        score in the caption of the pygame window """
    ## INPUTS: 
    ## OUTPUTS: 
      
    # Tiles in the game space are as follows
    tile2pixelRow = { 0 : 15, 1 : 137, 2 : 257, 3 : 377 }
    tile2pixelCol = { 0 : 15, 1 : 140, 2 : 260, 3 : 380 }
    
    #                                     15  137  257  377  
    # 01 02 03 04                   15  | 
    # 05 06 07 08  --\  Pixel  --\  140 |
    # 09 10 11 12  --/  Space  --/  260 |
    # 13 14 15 16                   380 |
    
    screen.blit(values2tiles["BG"].image, values2tiles["BG"].rect)
    
    # Traverse current matrix while or double for loops O(1) space
    for row in range(4):
        for col in range(4):
            entry = board[row][col]        
            if entry != 0:
                # Check this tile and map to the correct png
                # Map tile location to pixel space
                # Insert image onto board at mapped space
                tileRow = row
                tileCol = col
                screen.blit(values2tiles[entry].image, [tile2pixelCol[tileCol], tile2pixelRow[tileRow]])
    
    # Update the score and write to caption
    scoreString = "py2048 - Score: " + str(score)
    pygame.display.set_caption(scoreString)
    
    # Write the display tot he pygame window
    pygame.display.flip()
     
def main():
    
    # Initialize PyGame 
    pygame.init()
    
    fps = 60.0
    fpsClock = pygame.time.Clock()
    
    # Set up the window.
    width, height = 500, 500
    screen = pygame.display.set_mode((width, height))
    
    # Game Initialization
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0
    
    # Initialize board with two entries
    board = randEntry(board) 
    board = randEntry(board)
        
    # Initialize Game Sprites
    BackGround = Background('Board.png', [0, 0])
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
    
    values2tiles = { 2 : Tile2, 4 : Tile4, 8 : Tile8, 16 : Tile16,
                     32 : Tile32, 64 : Tile64, 128 : Tile128, 
                     256 : Tile256, 512 : Tile512, 1024 : Tile1024,
                     2048 : Tile2048, "BG" : BackGround }
  
    # Draw the board for the first time
    draw(board, screen, score, values2tiles)

    # Main game loop.
    dt = 1/fps # dt is the time since last frame
    runGame = True # Bool to keep track of if termination criteria has been met
    
    while runGame:
        runGame, callDraw = update(dt, board, score)
        if callDraw:
            draw(board, screen, score, values2tiles)
            
        dt = fpsClock.tick(fps)
        callDraw = False

if __name__ == "__main__":
    main()