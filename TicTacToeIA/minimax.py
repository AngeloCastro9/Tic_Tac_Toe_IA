from TicTacToe import blankSpace, token, checkWinner

def movementIA(board, player):

    #pega todas as posicoes disponiveis, em branco
    possibilities = getPositions(board)
    best_value = None
    #melhor movimento se da pensando em todas as possibilities e escolhendo o melhor movimento a se fazer
    best_movement = None
    
    for possibilitie in possibilities:
        # se coloca o token do jogador em todos os campos possiveis
        board[possibilitie[0]][possibilitie[1]] = token[player]
        # chama o algoritmo do minimax
        value = minimax(board, player)
        # se limpa todos os campos marcados para possibilidade
        board[possibilitie[0]][possibilitie[1]] = blankSpace
        if(best_value is None):
            best_value = value
            best_movement = possibilitie
        #verifica se a IA e o jogador 0 ( o que a IA comeca )
        elif(player == 0):
            if(value > best_value):
                best_value = value
                best_movement = possibilitie
        #verifica se a IA e o jogador 1 ( o que o jogador humano comeca )
        elif(player == 1):
            if(value < best_value):
                best_value = value
                best_movement = possibilitie

    return best_movement[0], best_movement[1]

# pega todas as posicoes disponiveis para se jogar
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
    #verifica se existe um vencedor
    winner = checkWinner(board)
    if(winner):
        #retorna o ganhador/empate 
        return score[winner]
    #troca o jogador, para que seja a vez do proximo jogador
    player = (player + 1)%2 #%2 = resto da divisao por 2
    #pega todas as posicoes 
    possibilities = getPositions(board)
    best_value = None
    for possibilitie in possibilities:
        # se coloca o token do jogador em todos os campos possiveis
        board[possibilitie[0]][possibilitie[1]] = token[player]
        # chama o algoritmo minimax
        value = minimax(board, player)
        # se limpa todos os campos marcados para possibilidade
        board[possibilitie[0]][possibilitie[1]] = blankSpace
        if(best_value is None):
            best_value = value
        #verifica se a IA e o jogador 0 ( o que a IA comeca )
        elif(player == 0):
            if(value > best_value):
                best_value = value
        #verifica se a IA e o jogador 1 ( o que o jogar humano comeca )
        elif(player == 1):
            if(value < best_value):
                best_value = value
    return best_value