blankSpace = " "
token = ["X", "O"]

def createBoard():
    board = [
        [blankSpace, blankSpace, blankSpace],
        [blankSpace, blankSpace, blankSpace],
        [blankSpace, blankSpace, blankSpace],
    ]
    return board

def printBoard(board):
    for line in range(3):
        print("|".join(board[line]))
        if(line < 2):
            print("------")

def getValidInput(message):
    try:
        n = int(input(message))
        if(n >= 1 and n <= 3):
            return n - 1
        else:
            print("Number must be between 1 and 3")
            return getValidInput(message)
    except:
        print("invalid number")
        return getValidInput(message)

def checkMovement(board, line , column):
    if(board[line][column] == blankSpace):
        return True
    else:
        return False

def makesMovement(board, line, column, player):
    board[line][column] = token[player]

def checkWinner(board):
    for line in range(3):
        if(board[line][0] == board[line][1] and board[line][1] == board[line][2] and board[line][0] != blankSpace):
            return board[line][0]
    
    for line in range(3):
        if(board[0][line] == board[1][line] and board[1][line] == board[2][line] and board[0][line] != blankSpace):
            return board[0][line]

    if(board[0][0] != blankSpace and board[0][0] == board[1][1] and board[1][1] == board[2][2]):
        return board[0][0]

    if(board[0][2] != blankSpace and board[0][2] == board[1][1] and board[1][1] == board[2][0]):
        return board[0][2]

    for line in range(3):
        for column in range(3):
            if(board[line][column] == blankSpace):
                return False    
    return "DRAW"
