#PLAN WORK, WORK PLAN
'''
Step 1: Create a 2d 3x3 grid

Step 2: 2 Human Players

Step 3: Who goes first(random), Enter Names

Step 4: Player 1 chooses between X or O

Step 5: Player chooses a row and column (1-3 each)

Step 6: after each turn check if someone has won. Vertical, horizontal, diagonal.
	if grid [0][0] == 'x'
		and grid [0][1] =='x'
		and grid [0][2] == 'x'

Step 7: present score if won

Step 8: ask to play again if yes then reset the board if no then goodbye!
'''
# Tic-Tac-Toe
# Tyler Kaltz | 10/8/26

def create_board():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]


def display_board(board):
    print("    1   2   3")
    for i, row in enumerate(board):
        print(str(i + 1) + "   " + " | ".join(row))
        if i < 2:
            print("   -----------")


def get_player_move(board, player):
    pass


def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None


def is_draw(board):
    if check_winner(board) != None:
        return False

    for row in board:
        for cell in row:
            if cell == " ":
                return False

    return True


def play_game():
    board = create_board()
    display_board(board)


if __name__ == "__main__":
    play_game()