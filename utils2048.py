# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : JJM
# Created Date: Sat Dec  4 18:28:28 2021
# version ='1.0'
# ---------------------------------------------------------------------------
""" Details about the module and for what purpose it was built for"""
# ---------------------------------------------------------------------------
# Imports
# ---------------------------------------------------------------------------
from random import randint

# moveUpDown.py
def moveUpDown(board, score, up):
    # MoveUpDown Takes a matrix, current score, and up or down as input.
    # Shifts matrix according to inputs and outputs new board and score.
    # Check for shift and for loops to shift accordingly
    if up == 1:
    # Adds like terms and eliminates duplicates up shifts
        for col in range(4):
            for row in range(3):
                if board[row][col] == board[row+1][col]:
                    board[row][col] = 2*board[row][col]
                    board[row+1][col] = 0
                    # Change Score
                    score = score + board[row][col]
                elif row < 2 and board[row+1][col] == 0 and board[row][col] == board[row+2][col]:
                    board[row][col] = 2*board[row][col]
                    board[row+2][col] = 0
                    # Change Score
                    score = score + board[row][col]
                elif row < 1 and board[row+2][col] == 0 and board[row][col] == board[row+3][col]:
                    board[row][col] = 2*board[row][col]
                    board[row+3][col] = 0
                    # Change Score
                    score = score + board[row][col]

        for reps in range(3):
            for jj in range(4):
                for ii in range(4):
                    if board[ii][jj] == 0:
                        if ii == 3:
                           board[ii][jj] = 0
                        else:
                            board[ii][jj] = board[ii+1][jj]
                            board[ii+1][jj] = 0

    # This else shifts all tiles down
    else:
        # Adds like terms and eliminates duplicates for down shifts
        for col in range(3, -1, -1):
            for row in range(3, 0, -1):
                if board[row][col] == board[row-1][col]:
                    board[row][col] = 2*board[row][col]
                    board[row-1][col] = 0
                    # Change Score
                    score = score + board[row][col]
                elif row > 1 and board[row-1][col] == 0 and board[row][col] == board[row-2][col]:
                    board[row][col] = 2*board[row][col]
                    board[row-2][col] = 0
                    # Change Score
                    score = score + board[row][col]
                elif row > 2 and board[row-2][col] == 0 and board[row][col] == board[row-3][col]:
                    board[row][col] = 2*board[row][col]
                    board[row-3][col] = 0
                    # Change Score
                    score = score + board[row][col]

        for reps in range(3):
            for jj in range(4): 
                for ii in range(3, -1, -1):
                    if board[ii][jj] == 0:
                        if ii == 0:
                            board[ii][jj] = 0
                        else:
                            board[ii][jj] = board[ii-1][jj]
                            board[ii-1][jj] = 0

    return board, score 

def moveLeftRight(board, score, left):
    
    # MoveLeftRight Takes a matrix, current score, and left or right as input.
    # Shifts matrix according to inputs and outputs new board and score.
    # Check for shift and for loops to shift accordingly
    if left == 1:
    # Adds like terms and eliminates duplicates for left shifts
        for row in range(4):
            for col in range(3):
                if board[row][col] == board[row][col+1]:
                    board[row][col] = 2*board[row][col]
                    board[row][col+1] = 0
                    # Change Score
                    score = score + board[row][col]
                elif col < 2 and board[row][col+1] == 0 and board[row][col] == board[row][col+2]:
                    board[row][col] = 2*board[row][col]
                    board[row][col+2] = 0
                    # Change Score
                    score = score + board[row][col]
                elif col < 1 and board[row][col+2] == 0 and board[row][col] == board[row][col+3]:
                    board[row][col] = 2*board[row][col]
                    board[row][col+3] = 0
                    # Change Score
                    score = score + board[row][col]

        for reps in range(3):
            for ii in range(4):
                for jj in range(4):
                    if board[ii][jj]== 0:
                        if jj == 3:
                           board[ii][jj] = 0
                        else:
                            board[ii][jj] = board[ii][jj+1]
                            board[ii][jj+1] = 0

    # This else shifts all tiles to the right        
    else:
        # Adds like terms and eliminates duplicates for right shifts
        for row in range(4):
            for col in range(3, 0, -1):
                if board[row][col] == board[row][col-1]:
                    board[row][col] = 2*board[row][col]
                    board[row][col-1] = 0
                    # Change Score
                    score = score + board[row][col]
                elif col > 2 and board[row][col-2] == 0 and board[row][col] == board[row][col-3]:
                    board[row][col] = 2*board[row][col]
                    board[row][col-3] = 0
                    # Change Score
                    score = score + board[row][col]
                elif col > 1 and board[row][col-1] == 0 and board[row][col] == board[row][col-2]:
                    board[row][col] = 2*board[row][col]
                    board[row][col-2] = 0
                    # Change Score
                    score = score + board[row][col]
                
        for reps in range(3):
            for jj in range(3, -1, -1):
                for ii in range(4):
                    if board[ii][jj] == 0:
                        if jj == 0:
                            board[ii][jj] = 0
                        else:
                            board[ii][jj] = board[ii][jj-1]
                            board[ii][jj-1] = 0

    return board, score

def randEntry(board):
    # Need to input new random 4 or 2 in an empty space in the board
    # This will be in constant space, so no need to make something fancy, just loop through twice
    zeroLocations = list()
    randVals = [2, 4]
    randVal = randVals[randint(0, 1)]
    
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                zeroLocations.append([i, j])
                
    insertNew = zeroLocations[randint(0, len(zeroLocations)-1)]
    
    board[insertNew[0]][insertNew[1]] = randVal

    return board

def printGameDetails(board, score):
    
    print(board[0])
    print(board[1])
    print(board[2])
    print(board[3])
    print("Score: ", score)