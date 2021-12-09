# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:28:28 2021

@author: meert
"""

# TODOs 
# Verify L/R and U/D logic against test cases
# Error check (termination criteria)
# Directly ingest key type
# Need to input new random 4 or 2 in an empty space in the board
# Rescale board image
# Dont insert random val for a non-valid move


from pynput.keyboard import Key, Listener
from utils2048 import moveUpDown, moveLeftRight, randEntry
import copy

def on_release(key):
    global userInput
    userInput = Key
    validKeys = [Key.up, Key.down, Key.left, Key.right]
    if key in validKeys: 
        userInput = key
        return False
    else:
        return False

def getKeyPress():
    with Listener(on_release=on_release) as listener:
      listener.join()
    

def main():
    #board = [[2, 0, 0, 0],[2, 0, 0, 0],[4, 0, 0, 0],[0, 0, 0, 0]]
    #score = 0
    #up = 1
    #return moveUpDown(board, score, up)
    #board = [[2, 2, 4, 0],[2, 0, 2, 0],[4, 0, 0, 2],[0, 0, 0, 0]]
    
    # Game Initialization
    board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    randEntry(board) # Initialize board with two entries
    randEntry(board)
    score = 0
    
    
    # Play game logic
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    playGame = True

    while playGame:

        #userInput = Key # Clear out global variable for each game move -> prevents doubling up
        getKeyPress()
        print(str(userInput))
        
        # Checks for a valid game
        if userInput not in [Key.up, Key.down, Key.left, Key.right]:
            print("Invalid Key")
            return False
        
        oldBoard = copy.deepcopy(board)
        
        # I would put in a switch/case statement here if doing in C++/MATLAB etc
        if userInput == Key.up:
            moveUpDown(board, score, 1)
        elif userInput == Key.down:
            moveUpDown(board, score, 0)
        elif userInput == Key.left:
            moveLeftRight(board, score, 1)
        elif userInput == Key.right:
            moveLeftRight(board, score, 0)
        else:
            # Throw error
            print("ERROR")
            
        # Check to see if anything changed
        if oldBoard != board:   
            randEntry(board) # Update board with the new entry
        else: 
            # Keep track of invalid moves, if all four directions cue this logic, it's time to end the game
            print("Logic check")
        
        print(board[0])
        print(board[1])
        print(board[2])
        print(board[3])
    

if __name__ == "__main__":
    main()