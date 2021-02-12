from TicTacToe import createBoard, makesMovement,  getValidInput, \
                            printBoard, checkWinner,  checkMovement

from minimax import movementIA

# se coloca 1 para o jogador inicar, 0 para a IA
player = 1
board = createBoard()
winner = checkWinner(board)
while(not winner):
    printBoard(board)
    print("===================")
    if(player == 0):
        line, column = movementIA(board, player)
    else:
        # maquina vs maquina
        # line, column = movementIA(board, player)

        #jogador humano vs maquina
        line = getValidInput("Enter the line: ")
        column = getValidInput("Enter the column: ")
    
    if(checkMovement(board, line, column)):
        makesMovement(board, line, column, player)
        #troca o jogador, para que seja a vez do proximo jogador
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