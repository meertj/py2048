# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : JJM
# Created Date: Sat Dec  4 18:28:28 2021
# version ='1.0'
# ---------------------------------------------------------------------------
""" CMD line version of py2048 """
# ---------------------------------------------------------------------------
# Rev history
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from utils2048 import moveUpDown, moveLeftRight, randEntry, printGameDetails, checkTermination
import copy
from pynput.keyboard import Key, Listener

# TODOs 
# Verify L/R and U/D logic against test cases
# Error check (termination criteria)
# Directly ingest key type
# Rescale board image (gmd line)
        
def on_release(key):
    global userInput
    
    # Clear out global variable for each game move -> prevents doubling up
    userInput = Key
    validKeys = [Key.up, Key.down, Key.left, Key.right]
    if key in validKeys: 
        userInput = key
    return False

def getKeyPress():
    with Listener(on_release=on_release) as listener:
      listener.join()

def main():    
    # Game Initialization
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    score = 0
    
    randEntry(board) # Initialize board with two entries
    randEntry(board)
        
    # Play game logic
    playGame = True

    while playGame:
        printGameDetails(board, score)

        getKeyPress()
        
        # Checks for a valid game
        if userInput in [Key.up, Key.down, Key.left, Key.right]:
            
            oldBoard = copy.deepcopy(board)
            
            # I would put in a switch/case statement here if doing in C++/MATLAB etc
            if userInput == Key.up:
                board, score = moveUpDown(board, score, 1)
            elif userInput == Key.down:
                board, score = moveUpDown(board, score, 0)
            elif userInput == Key.left:
                board, score = moveLeftRight(board, score, 1)
            elif userInput == Key.right:
                board, score = moveLeftRight(board, score, 0)
            else:
                # Throw error
                print("ERROR")
                
            # Check to see if anything changed
            if oldBoard != board:   
                randEntry(board) # Update board with the new entry
            elif checkTermination(board):
                playGame = False
                if [max(row) == 2048 for row in board]:
                    print("Congratulations, you win with a score of: ", score)
                else:
                    print("Game over, your final score was: ", score)

if __name__ == "__main__":
    main()