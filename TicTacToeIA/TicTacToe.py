blankSpace = " "
token = ["X", "O"]

def createBoard():
    board = [
        [blankSpace, blankSpace, blankSpace],
        [blankSpace, blankSpace, blankSpace],
        [blankSpace, blankSpace, blankSpace],
    ]
    return board

#monta o quadro
def printBoard(board):
    for line in range(3):
        print("|".join(board[line]))
        if(line < 2):
            print("------")

# verifica se os valores informados para jogar sao validos
def getValidInput(message):
    try:
        n = int(input(message))
        if(n >= 1 and n <= 3):
            # precisa ser -1 pois no python a contagem comeca em 0
            print(n)
            return n - 1
        else:
            print("Number must be between 1 and 3")
            return getValidInput(message)
    except:
        print("invalid number")
        return getValidInput(message)

# verifica se o moviemento feito e valido
def checkMovement(board, line , column):
    if(board[line][column] == blankSpace):
        return True
    else:
        return False

# pega os valores da coluna e da linha e movimenta com o token do jogador atual
def makesMovement(board, line, column, player):
    board[line][column] = token[player]

def checkWinner(board):
    # linhas 
    for line in range(3):
        #verifica se tem 3 elementos iguais na mesma linha
        if(board[line][0] == board[line][1] and board[line][1] == board[line][2] and board[line][0] != blankSpace):
            return board[line][0]
    
    # coluna
    for line in range(3):
        #verifica se tem 3 elementos iguais na mesma coluna
        if(board[0][line] == board[1][line] and board[1][line] == board[2][line] and board[0][line] != blankSpace):
            return board[0][line]

    # diagonal principal
    #verifica se tem 3 elementos iguais na diagonal principal
    if(board[0][0] != blankSpace and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    # diagonal secundaria
    #verifica se tem 3 elementos iguais na secundaria
    if(board[0][2] != blankSpace and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    #percorre todas as linhas
    for line in range(3):
        #percorre todas as colunas
        for column in range(3):
            #se as linhas e colunas forem brancas, nao existe ganhador, ainda!
            if(board[line][column] == blankSpace):
                return False
    # caso todos os campos estejam preenchidos, deu empate
    return "DRAW"
