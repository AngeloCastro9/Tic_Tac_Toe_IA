from TicTacToe import blankSpace, token, checkWinner

def movementIA(board, player):

    possibilities = getPositions(board)
    best_value = None
    best_movement = None
    
    for possibilitie in possibilities:
        board[possibilitie[0]][possibilitie[1]] = token[player]
        value = minimax(board, player)

        board[possibilitie[0]][possibilitie[1]] = blankSpace
        if(best_value is None):
            best_value = value
            best_movement = possibilitie
        elif(player == 0):
            if(value > best_value):
                best_value = value
                best_movement = possibilitie        
        elif(player == 1):
            if(value < best_value):
                best_value = value
                best_movement = possibilitie

    return best_movement[0], best_movement[1]

def getPositions(board):
    positions = []
    for line in range(3):
        for column in range(3):
            if(board[line][column] == blankSpace):
                positions.append([line, column])
    
    return positions

score = {
    "DRAW": 0,
    "X": 1,
    "O": -1
}

def minimax(board, player):
    winner = checkWinner(board)
    if(winner):        
        return score[winner]

    player = (player + 1)%2 #%2 = resto da divisao por 2
    possibilities = getPositions(board)
    best_value = None

    for possibilitie in possibilities:
        board[possibilitie[0]][possibilitie[1]] = token[player]
        value = minimax(board, player)

        board[possibilitie[0]][possibilitie[1]] = blankSpace
        if(best_value is None):
            best_value = value
        elif(player == 0):
            if(value > best_value):
                best_value = value
        elif(player == 1):
            if(value < best_value):
                best_value = value
    return best_value