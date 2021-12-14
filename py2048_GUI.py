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
from utils2048 import moveUpDown, moveLeftRight, randEntry, printGameDetails
import copy
from pynput.keyboard import Key, Listener


# TODOs
# Display score somehow!
    
# def on_release(key):
#     global userInput
    
#     # Clear out global variable for each game move -> prevents doubling up
#     userInput = Key
#     validKeys = [Key.up, Key.down, Key.left, Key.right]
#     if key in validKeys: 
#         userInput = key
#     return False

# def getKeyPress():
#     with Listener(on_release=on_release) as listener:
#       listener.join()

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
  

def main():
    
    pygame.init()
    clock = pygame.time.Clock()

    DISPLAYSURF = pygame.display.set_mode((500, 500))

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
    
    DISPLAYSURF.fill([255, 255, 255])
    DISPLAYSURF.blit(BackGround.image, BackGround.rect)
    
    # Game Initialization
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0
    
    board = randEntry(board) # Initialize board with two entries
    board = randEntry(board)
    
    #printGameDetails(board, score)
    for row in range(4):
        for col in range(4):
            entry = board[row][col]        
            if entry != 0:
                # Check this tile and map to the correct png
                # Map tile location to pixel space
                # Insert image onto board at mapped space
                tileRow = row
                tileCol = col
                DISPLAYSURF.blit(values2tiles[entry].image, [tile2pixelRow[tileRow], tile2pixelCol[tileCol]])
    
    pygame.display.update()

    # Play game logic
    playGame = True
    
    while playGame: # main game loop
        
        # Poll keyboard
        clock.tick(30)
        
        # getKeyPress()
        #print(str(userInput))
        
        # Checks for a valid game
        # if userInput not in [Key.up, Key.down, Key.left, Key.right]:
        #     print("Invalid Key")
        #     return False
        
        oldBoard = copy.deepcopy(board)
        keystate = pygame.key.get_pressed()
        
        # I would put in a switch/case statement here if doing in C++/MATLAB etc
        if keystate[pygame.K_UP]:
            board, score = moveUpDown(board, score, 1)
        elif keystate[pygame.K_DOWN]:
            board, score = moveUpDown(board, score, 0)
        elif keystate[pygame.K_RIGHT]:
            board, score = moveLeftRight(board, score, 1)
        elif keystate[pygame.K_LEFT]:
            board, score = moveLeftRight(board, score, 0)
        # else:
        #     # Throw error
        #     print("ERROR")
            
        # Check to see if anything changed
        if oldBoard != board:   
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
                        DISPLAYSURF.blit(values2tiles[entry].image, [tile2pixelRow[tileRow], tile2pixelCol[tileCol]])
                        print("Entry is non-zero")
        #else: 
            # Keep track of invalid moves, if all four directions cue this logic, it's time to end the game
            # print("Logic check")
        
        #printGameDetails(board, score)

    # scoreText = '2048 - Score: ' + str(score)
    # pygame.display.set_caption(scoreText)
    print("Made it here")
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
            
    print("Start next loop")
    pygame.display.update()
    #pygame.display.flip()

        
if __name__ == "__main__":
    main()