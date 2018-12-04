from random import randint

winner = False
moves = 0
winCombinations = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6)]

def initializeBoard():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def initializeSettings():
    print ("Play modes:" + "\n" + "1. 2 Players" + "\n" + "2. Against computer" + "\n")
    playMode = input("Choose play mode: " + "\n")

    if playMode == 1:
        players = {"player1": ("Player 1", "X"), "player2": ("Player 2", "O")}
        currentPlayer = players["player1"]
    elif playMode == 2:
        players = {"player": ("Player", "X"), "computer": ("Computer", "O")}
        currentPlayer = players["player"]

    return (playMode, players, currentPlayer)

def draw_board(board):
    print board[6], " ", board[7], " ", board[8]
    print board[3], " ", board[4], " ", board[5]
    print board[0], " ", board[1], " ", board[2]
    print ""


def is_legal_move(board, move):
    if (0 < move < 10):
        if isinstance(board[move - 1], int):
            return True
    return False


def ask_for_move(board):
    move = input("Click the number where you want to place your marker: ")
    while not (is_legal_move(board, move)):
        move = input("Invalid move! Click the number where you want to place your marker: ")
    return move


def computers_move(board):
    for combination in winCombinations:
        count = 0
        for i in combination:
            if board[i] == currentPlayer[1]:
                count += 1
                if count == 2:
                    for j in combination:
                        if isinstance(board[j], int):
                            return j+1

    for combination in winCombinations:
        count = 0
        for i in combination:
            if board[i] == players["player"][1]:
                count += 1
                if count == 2:
                    for j in combination:
                        if isinstance(board[j], int):
                            return j+1

    if is_legal_move(board, 5):
        return 5
    else:
        move = randint(0, 8)
        while not (is_legal_move(board, move)):
            move = randint(0, 8)
        return move+1


def check_winner(board, currentPlayer):
    currentPlayerHasWon = False
    for combination in winCombinations:
        count = 0
        for i in combination:
            if board[i] == currentPlayer[1]:
                count += 1
        if count == 3:
            currentPlayerHasWon = True

    return currentPlayerHasWon


board = initializeBoard()
settings = initializeSettings()
playMode = settings[0]
players = settings[1]
currentPlayer = settings[2]

while not winner:

    if playMode == 1:

        print currentPlayer[0] + " in turn" + "\n"
        move = ask_for_move(board)
        board[move - 1] = currentPlayer[1]
        moves += 1
        draw_board(board)
        winner = check_winner(board, currentPlayer)
        if moves == 9:
            print "No winner this time."
            winner = True
            break
        if winner:
            print currentPlayer[0] + " wins!"
            break
        if currentPlayer[0] == "Player 1":
            currentPlayer = players["player2"]
        else:
            currentPlayer = players["player1"]

    if playMode == 2:

        if currentPlayer == players["player"]:
            print currentPlayer[0] + " in turn" + "\n"
            move = ask_for_move(board)
            board[move - 1] = currentPlayer[1]
            moves += 1
            draw_board(board)
            winner = check_winner(board, currentPlayer)
            if moves == 9:
                print "No winner this time."
                winner = True
                break
            if winner:
                print currentPlayer[0] + " wins!"
                break
            if currentPlayer[0] == "Player":
                currentPlayer = players["computer"]
            else:
                currentPlayer = players["player"]

        if currentPlayer == players["computer"]:
            print currentPlayer[0] + " in turn" + "\n"
            move = computers_move(board)
            board[move - 1] = currentPlayer[1]
            moves += 1
            draw_board(board)
            winner = check_winner(board, currentPlayer)
            if moves == 9:
                print "No winner this time."
                winner = True
                break
            if winner:
                print currentPlayer[0] + " wins!"
                break
            if currentPlayer[0] == "Player":
                currentPlayer = players["computer"]
            else:
                currentPlayer = players["player"]

    #if winner:
        #continueGame = raw_input("Do you want to play again? (y/n)")
        #if continueGame == "y":
            #board = initializeBoard()
            #settings = initializeSettings()
            #playMode = settings[0]
            #players = settings[1]
            #currentPlayer = settings[2]