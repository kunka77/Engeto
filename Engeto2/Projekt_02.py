import random




# zkusime_pridat_AI
# Game_board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]
currentPlayer = "X"
winner = None
gameRunning = True
line = (" |---+---+---|")
odd = ("=============================")
inp = int()
End = 1
mod = None


# Welcome
def welcome():
    print(odd)
    print("Hi! Welcome to Tic Tac Toe")
    print("""GAME RULES:
Each player/AI can place one mark (or stone)
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row""")
    print("""Board looks like this: 
 | 1 | 2 | 3 | 
 |---+---+---|
 | 4 | 5 | 6 | 
 |---+---+---|
 | 7 | 8 | 9 |""")
    print(odd)
    print("Let's start the game!")


# Gameset
def game_set():
    global mod
    mod = input(""" For play PvP tipe '1' : 
 For play PvE tipe '2' : """, )
    if mod == "1":
        print("You choise PvP.")
        print(" _____________")
        return mod
    elif mod == "2":
        print("You choise PvE.")
        print(" _____________")
        return mod
    else:
        mod = "konec"


welcome()


# print_game_board
def print_board(board):
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(line)
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(line)
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | ")


def player_input(board):
    # Get position from player
    print(currentPlayer + "'s turn.")
    inp = input("Choose a position from 1-9: ")
    # Whatever the user inputs, make sure it is a valid input, and the spot is open
    valid = False
    while not valid:

        # Make sure the input is valid
        while inp not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            print("Your move must be number in range 1 - 9!\nTry again. ")
            inp = input("Choose a position from 1-9: ")

        # Get correct index in our board list
        inp = int(inp) - 1

        # Then also make sure the spot is available on the board
        if board[inp] == "-":
            valid = True

        else:
            print("You can't go there. Go again.")
    board[inp] = currentPlayer


# check for win, tie or lose
def check_horizont(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def check_row(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def check_dia(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


# check for TIE
def check_tie(board):
    if "-" not in board:
        print_board(board)
        print(" AH! is a TIE!")
        gameRunning = False
        return True
    else:
        return False


# Check for win
def check_win(board):
    global gameRunning
    if check_dia(board) or check_row(board) or check_horizont(board):
        print_board(board)
        print(f"We have a WINNER!  player {winner} won")
        gameRunning = False
        quit(gameRunning)


# switch the plazer
def switch_player(board):
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"        


# AI variant
def AI(board):
    while currentPlayer == "O":
        move = random.randint(0, 8)
        if board[move] == "-":
            board[move] = "O"
            switch_player(board)


# Option_control
game_set()
while mod == "konec":
    print("Frong choice! Must be '1' or '2' ! ")
    game_set()

# check_for_win_tie
while gameRunning:
    print_board(board)
    player_input(board)
    check_win(board)
    if gameRunning == False:
        break
    check_tie(board)
    switch_player(board)
    if mod == "2":
        AI(board)
    check_win(board)
    if gameRunning == False:
        break
    check_tie(board)
