from TicTacToe import createBoard, makesMovement,  getValidInput, \
                            printBoard, checkWinner,  checkMovement

from minimax import movementIA

player = 0
board = createBoard()
winner = checkWinner(board)
while(not winner):
    printBoard(board)
    if(player == 0):
        line, column = movementIA(board, player)
    else:
        # machine vs machine
        # line, column = movementIA(board, player)

        #human vs machine
        line = getValidInput("Enter the line: ")
        column = getValidInput("Enter the column: ")
    
    if(checkMovement(board, line, column)):
        makesMovement(board, line, column, player)
        player = (player + 1)%2
    else:
        print("The informed position is already occupied")
    
    winner = checkWinner(board)

print("===================")
printBoard(board)
if(winner != "DRAW"):
    print("Winner = ", winner)
else:
    print(winner)
print("===================")