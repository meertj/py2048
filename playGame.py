# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 18:28:28 2021

@author: meert
"""

# TODOs 
# Verify L/R and U/D logic against test cases
# Add in keyboard listening
# Error check (termination criteria)
# Directly injest key type

from pynput.keyboard import Key, Listener
from utils2048 import moveUpDown, moveLeftRight

def on_release(key):
    global userInput
    validKeys = [Key.up, Key.down, Key.left, Key.right]
    if key in validKeys: 
        userInput = key
        return False

def getKeyPress():
    with Listener(on_release=on_release) as listener:
      listener.join()


    

def main():
    #board = [[2, 0, 0, 0],[2, 0, 0, 0],[4, 0, 0, 0],[0, 0, 0, 0]]
    #score = 0
    #up = 1
    #return moveUpDown(board, score, up)
    board = [[2, 2, 4, 0],[2, 0, 2, 0],[4, 0, 0, 2],[0, 0, 0, 0]]
    score = 0
    # Play game logic
    print(board)
    playGame = True

    while playGame:
        # Checks for a valid game
        #userInput = Key # Clear out global variable for each game move -> prevents doubling up
        getKeyPress()
        print(str(userInput))
        
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
        
        print(board)
    

if __name__ == "__main__":
    main()