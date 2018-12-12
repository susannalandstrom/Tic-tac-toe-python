from random import randint


def initializeBoard():
    return [1, 2, 3, 4, 5, 6, 7, 8, 9]


def initializeSettings():
    print ("Play modes:" + "\n" + "1. 2 Players" + "\n" + "2. Against computer" + "\n")
    playMode = raw_input("Choose play mode: " + "\n")

    if is_legal_play_mode(playMode):
        playMode = int(playMode)

        if playMode == 1:
            players = {"player1": ("Player 1", "X"), "player2": ("Player 2", "O")}
            currentPlayer = players["player1"]
        elif playMode == 2:
            players = {"player": ("Player", "X"), "computer": ("Computer", "O")}
            currentPlayer = players["player"]

        return (playMode, players, currentPlayer)


    else:
        print "Invalid input" + "\n" + "Give only number 1 or 2 as input" + "\n"
        return initializeSettings()


#prints the board
def draw_board(board):
    print board[6], " ", board[7], " ", board[8]
    print board[3], " ", board[4], " ", board[5]
    print board[0], " ", board[1], " ", board[2]
    print ""


#defines whether the play mode input is legal
def is_legal_play_mode(mode):
    if mode == "1" or mode == "2":
        return True
    return False


#defines whether the move is legal, meaning that it is a number from 1 to 9 and the place is still empty on the board
def is_legal_move(board, move):
    if isinstance(move, int) or move.isdigit():
        if 0 < int(move) < 10:
            if isinstance(board[int(move) - 1], int):
                return True
    return False


#function is called when player is on turn
#asks the user for input and checks whether the move is legal
def ask_for_move(board):
    move = raw_input("Give the number where you want to place your marker: ")
    while not (is_legal_move(board, move)):
        move = raw_input("Invalid move! Give the number where you want to place your marker: ")
    return int(move)


#function is called when computer is on turn
def computers_move(board):
    #checks if computer can win with this move (has already to marks aligned)
    for combination in winCombinations:
        count = 0
        for i in combination:
            if board[i] == currentPlayer[1]:
                count += 1
                if count == 2:
                    for j in combination:
                        if isinstance(board[j], int):
                            return j+1

    #checks if player has to marks aligned and places his mark on the third blocking the player
    for combination in winCombinations:
        count = 0
        for i in combination:
            if board[i] == players["player"][1]:
                count += 1
                if count == 2:
                    for j in combination:
                        if isinstance(board[j], int):
                            return j+1

    #places the mark in the middle of the board if possible, if not, mark is randomly placed to a free spot
    if is_legal_move(board, 5):
        return 5
    else:
        move = randint(0, 8)
        while not (is_legal_move(board, move)):
            move = randint(0, 8)
        return move+1


#winner is checked on each turn
#if the currentPlayer's mark is found in a combination similar to winning combination, currentPlayer wins
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


#loop while the player chooses to continue playing
while(raw_input("Do you want to play? (y/n)") == "y"):
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

    board = initializeBoard()
    settings = initializeSettings()
    playMode = settings[0]
    players = settings[1]
    currentPlayer = settings[2]
    draw_board(board)

    #loop while there is no winner
    while not winner:

        #two player mode
        if playMode == 1:

            print currentPlayer[0] + " in turn" + "\n"
            move = ask_for_move(board)
            board[move - 1] = currentPlayer[1]                  #players move is placed on the board
            moves += 1
            draw_board(board)
            winner = check_winner(board, currentPlayer)         #possible winner is checked on each turn
            if winner:
                print currentPlayer[0] + " wins!"
                break
            if moves == 9:                                      #the board has no more empty spaces for playmarks
                print "No winner this time."
                winner = True
                break
            #switch currentPlayer to the player next on turn
            if currentPlayer[0] == "Player 1":
                currentPlayer = players["player2"]
            else:
                currentPlayer = players["player1"]

        #player vs. computer mode
        if playMode == 2:

            #when player is on turn
            if currentPlayer == players["player"]:
                print currentPlayer[0] + " in turn" + "\n"
                move = ask_for_move(board)
                board[move - 1] = currentPlayer[1]
                moves += 1
                draw_board(board)
                winner = check_winner(board, currentPlayer)
                if winner:
                    print currentPlayer[0] + " wins!"
                    break
                if moves == 9:
                    print "No winner this time."
                    winner = True
                    break
                if currentPlayer[0] == "Player":
                    currentPlayer = players["computer"]
                else:
                    currentPlayer = players["player"]

            #when computer is on turn
            if currentPlayer == players["computer"]:
                print currentPlayer[0] + " in turn" + "\n"
                move = computers_move(board)
                board[move - 1] = currentPlayer[1]              #computers playmark is added to the board
                moves += 1
                draw_board(board)
                winner = check_winner(board, currentPlayer)
                if winner:
                    print currentPlayer[0] + " wins!"
                    break
                if moves == 9:
                    print "No winner this time."
                    winner = True
                    break
                if currentPlayer[0] == "Player":
                    currentPlayer = players["computer"]
                else:
                    currentPlayer = players["player"]