"""
Tic Tac Toe Player
"""

import copy
from ctypes import util
from hashlib import new
from re import L

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
    if countX + countO == 9 or winner(board) is not None:
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


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    else:
        if player(board) == X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if terminal(board):
        return utility(board), None

    v = float('-inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = min_value(result(board, action))
        if aux > v:
            v = aux
            move = action
            if v == 1:
                return v, move

    return v, move


def min_value(board):
    if terminal(board):
        return utility(board), None

    v = float('inf')
    move = None
    for action in actions(board):
        # v = max(v, min_value(result(board, action)))
        aux, act = max_value(result(board, action))
        if aux < v:
            v = aux
            move = action
            if v == -1:
                return v, move

    return v, move
