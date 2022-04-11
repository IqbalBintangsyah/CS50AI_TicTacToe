"""
Tic Tac Toe Player
"""

import copy
from ctypes import util
from hashlib import new

from numpy import empty

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    countX = 0
    countO = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == X:
                countX = countX + 1
            if board[x][y] == O:
                countO = countO + 1
    if countX + countO == 9:
        return 1
    if board == initial_state() or countX == countO:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibleAction = []
    for x in range(3):
        for y in range(3):
            if board[x][y] == EMPTY:
                possibleAction.append((x, y))

    return possibleAction


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = board
    turn = player(board)
    newBoard[action[0]][action[1]] = turn
    return newBoard


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O
    else:
        for x in range(3):
            for y in range(3):
                #X win
                if board[x][0] == X and board[x][1] == X and board[x][2] == X:
                    return X
                elif board[0][y] == X and board[1][y] == X and board[2][y] == X:
                    return X
                #O win
                elif board[x][0] == O and board[x][1] == O and board[x][2] == O:
                    return O
                elif board[0][y] == O and board[1][y] == O and board[2][y] == O:
                    return O
    return None
    


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None or player(board) == 1:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if terminal(board):
        if winner(board) == X:
            return 1
        elif winner(board) == O:
            return -1
        else:
            return 0
    else:
        return 0


def max(board, score = -9999):
    action = actions(board)
        
    for a in action:
        copy_board = copy.deepcopy(board)
        copy_board[a[0]][a[1]] = X
        print("X moves", a)
        if not terminal(copy_board):
            score = utility(copy_board)
            move = min(copy_board, score)
        else:
            if score <= utility(copy_board):
                score = utility(copy_board)
                move = a
    return move

def min(board, score = 9999):
    action = actions(board)
    
    for a in action:        
        copy_board = copy.deepcopy(board)
        copy_board[a[0]][a[1]] = O
        print("O moves", a)
        if not terminal(copy_board):
            score = utility(copy_board)
            move = max(copy_board, score)
        else:
            if score >= utility(copy_board):
                score = utility(copy_board)
                move = a
    return move


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    opp = player(board)
    if opp == O:
        move = min(board)
    else:
        move = max(board)
    return move
    '''
    opp = player(board)
    if opp == O:
        score = 9999
    else:
        score = -9999
    action = actions(board)
    new_board = copy.deepcopy(board)
    play = opp
    while(not terminal(board)):
        move = action.pop()
        new_board[move[0]][move[1]] = play
        if opp == O:
            if utility(new_board)<score:
                score = utility(new_board)
        else:
            if utility(new_board)>score:
                score = utility(new_board)
        score = utility(new_board)
        play = player(new_board)
        for act in actions(new_board):
            action.append(act)
    '''
    return move
