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
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *
from utils2048 import moveUpDown, moveLeftRight, randEntry, printGameDetails
import copy

## DEFINE CLASSES
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
    """
    Update game. Called once per frame.
    dt is the amount of time passed since last frame.""" 
    
    oldBoard = copy.deepcopy(board)
    
    # Go through events that are passed to the script by the window.
    for event in pygame.event.get():
      # We need to handle these events. Initially the only one you'll want to care
      # about is the QUIT event, because if you don't handle it, your game will crash
      # whenever someone tries to exit.
      if event.type == QUIT:
        pygame.quit() # Opposite of pygame.init
        sys.exit() # Not including this line crashes the script on Windows. Possibly
        # on other operating systems too, but I don't know for sure.
      # Handle other events as you wish.
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
          screen.blit(BackGround.image, BackGround.rect)

          board = randEntry(board) # Update board with the new entry
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
    return score
                      
   
def draw(screen, score):
  """
  Draw things to the window. Called once per frame.
  """
  # Update the score
  scoreString = "py2048 - Score: " + str(score)
  pygame.display.set_caption(scoreString)

  
  # Flip the display so that the things we drew actually show up.
  pygame.display.flip()
 
#def runPyGame():

# All game initialization happens here
#pygame.display.set_mode()
pygame.display.set_caption('2048 - Score: 0')

# Initialize Game
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
                 2048 : Tile2048 }

# Tiles in the game space are as follows
tile2pixelRow = { 0 : 15, 1 : 137, 2 : 257, 3 : 377 }
tile2pixelCol = { 0 : 15, 1 : 140, 2 : 260, 3 : 380 }

#                                     15  137  257  377  
# 01 02 03 04                   15  | 
# 05 06 07 08  --\  Pixel  --\  140 |
# 09 10 11 12  --/  Space  --/  260 |
# 13 14 15 16                   380 |

# Initialise PyGame.
pygame.init()

# Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
fps = 60.0
fpsClock = pygame.time.Clock()

# Set up the window.
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
  
screen.fill([255, 255, 255])
screen.blit(BackGround.image, BackGround.rect)

# Game Initialization
board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
score = 0

board = randEntry(board) # Initialize board with two entries
board = randEntry(board)

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
  
# Main game loop.
dt = 1/fps # dt is the time since last frame.
while True: # Loop forever!
    score = update(dt, board, score) # You can update/draw here, I've just moved the code for neatness.
    draw(screen, score)

    dt = fpsClock.tick(fps)
        
#runPyGame()