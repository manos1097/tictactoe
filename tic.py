import random

# Function definitions

def initBoard():
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board

def playerMarkerSelection():
    player1 = ''
    while(player1 not in ('X', 'O')):
        player1 = input('\n  Player 1: Select a symbol. Write X or O\n')
    else:
        if player1 == 'X':
            player2 = 'O'
        else:
            player2 = 'X'

    return (player1, player2)

def drawBoard(board):
    print('\n' * 100)
    print('    ' + board[6] + '|' + board[7] + '|' + board[8])
    print('    -+-+-')
    print('    ' + board[3] + '|' + board[4] + '|' + board[5])
    print('    -+-+-')
    print('    ' + board[0] + '|' + board[1] + '|' + board[2])
    print('\n' * 2)

def markPosition(board, pos, mark):
    board[pos - 1] = mark
    return (pos, mark)

def askPlayerPosMark(board, currentPlayer):
    pos = 0
    while pos not in range(1,10):
        try:
            pos = int(input('\n  {}: Select a free position to mark. Enter a valid number from 1 to 9 and hit Enter!\n\n'.format(playerNames[currentPlayer])))
        except ValueError:
            print('  Invalid number. Please input a valid number from 1 to 9')
    else:
        return pos

def resetBoard(board):
    board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
    return board

def randomPlayerStart(players):
    return random.randrange(0, players)

def askReplay():
    answer = ''
    while answer not in ('y', 'n'):
        answer = input('\n  Do you want to play again? Write "y" for yes or "n" for no and hit Enter !\n')
    return answer == 'y'

def nextPlayer(currentPlayer):
    if currentPlayer == player1:
        currentPlayer = player2
    else:
        currentPlayer = player1
    return currentPlayer

def checkPlayerWin(board, mark):

    # horizontally check
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        return True

    # diagonally check
    elif board[6] == mark and board[4] == mark and board[2] == mark:
        return True
    elif board[8] == mark and board[4] == mark and board[0] == mark:
        return True

    # vertically check
    elif board[6] == mark and board[3] == mark and board[0] == mark:
        return True
    elif board[7] == mark and board[4] == mark and board[1] == mark:
        return True
    elif board[8] == mark and board[5] == mark and board[2] == mark:
        return True

    return False

def checkFreePos(board, pos):
    return board[pos - 1] not in ('X', 'O')

def checkFullBoard(board):
    return set(board) <= set(('X','O'))

# The actual program

while True:
    print('\n  Welcome to Tic Tac Toe!')
    print('\n  If you want to stop the game, just press Ctrl + C !')

    # Initialize the board list with empty values
    board = initBoard()

    # Choose between 'X' or 'O' for player 1 and give the other char to player 2
    (player1, player2) = playerMarkerSelection()

    players = (player1, player2)
    playerNames = {player1: 'Player 1', player2: 'Player 2'}

    # Let python choose a random player to play first
    currentPlayer = players[randomPlayerStart(2)]

    drawBoard(board)

    # The loop to fill the board with marks
    # It stops when someone wins the game
    hasWinner = False

    while not hasWinner:
        posToMark = askPlayerPosMark(board, currentPlayer)
        if checkFreePos(board, posToMark):
            markPosition(board, posToMark, currentPlayer)
            drawBoard(board)

            if checkFullBoard(board):
                print("\n  It's a tie!\n")
                break
            elif checkPlayerWin(board, currentPlayer):
                hasWinner = True
                print(f'\n  {playerNames[currentPlayer]} wins!\n')
            else:
                currentPlayer = nextPlayer(currentPlayer)

    # If the user doesn't want to play again, stop the top level while loop, to terminate the game
    if not askReplay():
        break
