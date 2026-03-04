"""
Tic Tac Toe Player
"""

import math
import random

X = "X"
O = "O"
EMPTY = None
class InvalidActionError(Exception):
    def __init__(self, action, board, message):
        self.action = action
        self.board = board
        self.message = message
        super().__init__(self.message)


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
    X_count = 0
    O_count = 0
    for i in range (3):
        for j in range (3):
            if board[i][j] == X:
                X_count += 1
            elif board[i][j] == O:
                O_count += 1

    if X_count > O_count:
        return O
    else:
        return X

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range (3):
        for j in range (3): 
            if board[i][j] == EMPTY:
                moves.add((i, j))

    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Create a deep copy of the board
    new_board = [row.copy() for row in board]
    
    i, j = action
    if new_board[i][j] != EMPTY:
        raise InvalidActionError(action, board, 'Result function tried to perform invalid action on occupied tile: ')
    
    new_board[i][j] = player(board)  #determine whose turn it is
    return new_board
            
    

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    #check columns
    for i in range(3):
        # Direct comparison without string conversion
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] is not EMPTY:
            return board[0][i]
        
    #check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    
    return None



def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) != None or not actions(board):
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



def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    if terminal(board):
        return utility(board)
    
    curr_player= player(board)
    if board == initial_state():
        return random.choice(list(actions(board)))

    if curr_player==X:
        best_value = -math.inf
        best_actions=None
        alpha=-math.inf
        beta=math.inf

        for action in actions(board):
            v = minplayer(result(board, action), alpha, beta)
            if v > best_value:
                best_value = v
                best_actions=action

        return best_actions
    
    else: 
        best_value= math.inf
        best_actions= None
        alpha= -math.inf
        beta=math.inf

        for action in actions(board):
            v = maxplayer(result(board,action), alpha, beta)
            if v < best_value:
                best_value = v 
                best_actions = action


        return best_actions





def maxplayer(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = -math.inf

    
    for action in actions(board):
        v = max(v, minplayer(result(board, action), alpha, beta))
        if v>= beta:
            return v
        alpha= max(alpha, v)

    return v 


def minplayer(board, alpha, beta):
    if terminal(board):
        return utility(board)
    
    v = math.inf

    for action in actions(board):
        v = min(v, maxplayer(result(board, action), alpha, beta))
        if v<= alpha:
            return v
        beta= min(beta, v)

    return v 
