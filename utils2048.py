# moveUpDown.py

def moveUpDown(board, score, up):
    # MoveUpDown Takes a matrix, current score, and up or down as input.
    # Shifts matrix according to inputs and outputs new board and score.
    # Check for shift and for loops to shift accordingly
    if up == 1:
    # Adds like terms and eliminates duplicates up shifts
            for xx in range(4):
                for ee in range(3):
                    if board[ee][xx] == board[ee+1][xx]:
                        board[ee][xx] = 2*board[ee][xx]
                        board[ee+1][xx] = 0
                    elif ee < 2 and board[ee+1][xx] == 0 and board[ee][xx] == board[ee+2][xx]:
                        board[ee][xx] = 2*board[ee][xx]
                        board[ee+2][xx] = 0
                    elif ee < 1 and board[ee+2][xx] == 0 and board[ee][xx] == board[ee+3][xx]:
                        board[ee][xx] = 2*board[ee][xx]
                        board[ee+3][xx] = 0
                    else:
                        break
                    # Change Score
                    score = score + board[ee][xx]

            for aa in range(3):
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
        for xx in range(3, 0):
            for ee in range(3, 1):
                if board[ee][xx] == board[ee-1][xx]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee-1][xx] = 0
                elif ee > 1 and board[ee-1][xx] == 0 and board[ee][xx] == board[ee-2][xx]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee-2][xx] = 0
                elif ee > 2 and board[ee-2][xx] == 0 and board[ee][xx] == board[ee-3][xx]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee-3][xx] = 0
                else:
                    break
                # Change Score
                score = score + board[ee][xx]

        for aa in range(3):
            for jj in range(4): 
                for ii in range(3, 0):
                    if board[ii][jj] == 0:
                        if ii == 0:
                            board[ii][jj] = 0
                        else:
                            board[ii][jj] = board[ii-1][jj]
                            board[ii-1][jj] = 0

    return board, score 

def moveLeftRight(board,score,left):
    
    # MoveLeftRight Takes a matrix, current score, and left or right as input.
    # Shifts matrix according to inputs and outputs new board and score.
    # Check for shift and for loops to shift accordingly
    if left == 1:
    # Adds like terms and eliminates duplicates for left shifts
        for ee in range(4):
            for xx in range(3):
                if board[ee][xx] == board[ee][xx+1]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee][xx+1] = 0
                elif xx < 2 and board[ee][xx+1] == 0 and board[ee][xx] == board[ee][xx+2]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee][xx+2] = 0
                elif xx < 1 and board[ee][xx+2] == 0 and board[ee][xx] == board[ee][xx+3]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee+3][xx] = 0
                else:
                    break
                # Change Score
                score = score + board[ee][xx]

            for aa in range(3):
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
        for ee in range(4):
            for xx in range(4,1):
                if board[ee][xx] == board[ee][xx-1]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee][xx-1] = 0
                elif xx > 2 and board[ee][xx-2] == 0 and board[ee][xx] == board[ee][xx-3]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee][xx-3] = 0
                elif xx > 1 and board[ee][xx-1] == 0 and board[ee][xx] == board[ee][xx-2]:
                    board[ee][xx] = 2*board[ee][xx]
                    board[ee][xx-2] = 0
                else:
                    break
                # Change Score
                score = score + board[ee][xx]
                    
        for aa in range(4):
            for jj in range(4, 0):
                for ii in range(4):
                    if board[ii][jj] == 0:
                        if jj == 1:
                            board[ii][jj] = 0
                        else:
                            board[ii][jj] = board[ii][jj-1]
                            board[ii][jj-1] = 0

    return board, score

