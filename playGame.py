# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : JJM
# Created Date: Sat Dec  4 18:28:28 2021
# version ='1.0'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""
# ---------------------------------------------------------------------------
# Rev history
# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from pynput.keyboard import Key, Listener
from utils2048 import moveUpDown, moveLeftRight, randEntry, printGameDetails
import copy

# TODOs 
# Verify L/R and U/D logic against test cases
# Error check (termination criteria)
# Directly ingest key type
# Rescale board image (gmd line)
# Two game modes (cmd line and gui)


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
    
    printGameDetails(board, score)
    
    # Play game logic
    playGame = True

    while playGame:

        getKeyPress()
        #print(str(userInput))
        
        # Checks for a valid game
        if userInput not in [Key.up, Key.down, Key.left, Key.right]:
            print("Invalid Key")
            return False
        
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
        else: 
            # Keep track of invalid moves, if all four directions cue this logic, it's time to end the game
            print("Logic check")
        
        printGameDetails(board, score)

    

if __name__ == "__main__":
    main()