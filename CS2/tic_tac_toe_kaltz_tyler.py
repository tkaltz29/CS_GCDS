#--------------------------------------------------------------
# Tic-Tac-Toe
# Tyler Kaltz | 10/8/26
# A two-player Tic-Tac-Toe game played in the terminal.
# Challenges: Color output, player name entry, random player
#   chooses X or O
#--------------------------------------------------------------

import random


# create_board
# Description: Creates an empty 3x3 Tic-Tac-Toe board.
# Parameters: None
# Returns: board - list of 3 lists, each with 3 empty spaces
def create_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


# color_mark
# Description: Adds color to a mark so X prints blue and O
#   prints red. Empty spaces are left unchanged.
# Parameters: mark - "X", "O", or " "
# Returns: the mark with color codes added
def color_mark(mark):
    if mark == "X":
        return "\033[34m" + mark + "\033[0m"
    elif mark == "O":
        return "\033[31m" + mark + "\033[0m"
    else:
        return mark


# display_board
# Description: Prints the board with row and column labels
#   and divider lines between rows.
# Parameters: board - the 3x3 game board
# Returns: None
def display_board(board):
    print("    1   2   3")
    for i, row in enumerate(board):
        # Color each square before printing the row
        colored = []
        for cell in row:
            colored.append(color_mark(cell))
        print(str(i + 1) + "   " + " | ".join(colored))
        # Divider line between rows
        if i < 2:
            print("   -----------")


# get_player_move
# Description: Asks the player for a row and column until
#   they enter a valid move. Catches non-number input,
#   numbers out of range, and spots already taken.
# Parameters: board - the 3x3 game board
#             player - the current player's mark, "X" or "O"
# Returns: row, col - the move's position (each 0-2)
def get_player_move(board, player):
    while True:
        # Catch letters or other non-number input
        try:
            row = int(input("Player " + color_mark(player) + ", enter row (1-3): "))
            col = int(input("Player " + color_mark(player) + ", enter column (1-3): "))
        except ValueError:
            print("Please enter numbers only.")
            continue

        # Check the numbers are in range and the spot is empty
        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Row and column must be between 1 and 3.")
        elif board[row - 1][col - 1] != " ":
            print("That spot is already taken. Try again.")
        else:
            # Subtract 1 because lists start at 0
            return row - 1, col - 1


# check_winner
# Description: Checks all 8 ways to win: 3 rows, 3 columns,
#   and 2 diagonals.
# Parameters: board - the 3x3 game board
# Returns: "X" or "O" if that player won, otherwise None
def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


# is_draw
# Description: Checks if the board is full and nobody won.
# Parameters: board - the 3x3 game board
# Returns: True if it's a draw, otherwise False
def is_draw(board):
    if check_winner(board) != None:
        return False

    # Any empty square means the game isn't over
    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True


# choose_marks
# Description: Randomly picks one player to choose X or O.
#   Keeps asking until they enter X or O.
# Parameters: name1 - player 1's name
#             name2 - player 2's name
# Returns: x_name, o_name - the X player's name, then the
#   O player's name
def choose_marks(name1, name2):
    chooser = random.choice([name1, name2])
    if chooser == name1:
        other = name2
    else:
        other = name1

    while True:
        choice = input(chooser + ", do you want to be X or O? ").upper()
        if choice == "X":
            return chooser, other
        elif choice == "O":
            return other, chooser
        else:
            print("Please enter X or O.")


# play_game
# Description: Runs one full game. X goes first, players take
#   turns until someone wins or it's a draw.
# Parameters: name1 - player 1's name
#             name2 - player 2's name
# Returns: None
def play_game(name1, name2):
    board = create_board()
    x_name, o_name = choose_marks(name1, name2)
    print(x_name + " is " + color_mark("X") + " and goes first!")
    print(o_name + " is " + color_mark("O") + ".")

    # X always goes first
    player = "X"

    while True:
        # Match the current mark to the player's name
        if player == "X":
            name = x_name
        else:
            name = o_name

        display_board(board)
        print(name + "'s turn")
        row, col = get_player_move(board, player)
        board[row][col] = player

        # End the game if someone won
        winner = check_winner(board)
        if winner != None:
            display_board(board)
            print(name + " wins!")
            break

        # End the game if it's a draw
        if is_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch turns
        if player == "X":
            player = "O"
        else:
            player = "X"


# main
# Description: Gets both player names, then keeps playing
#   games until the players choose to stop.
# Parameters: None
# Returns: None
def main():
    name1 = input("Player 1, enter your name: ")
    name2 = input("Player 2, enter your name: ")

    while True:
        play_game(name1, name2)
        again = input("Play again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing, goodbye!")
            break


if __name__ == "__main__":
    main()