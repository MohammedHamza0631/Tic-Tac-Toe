board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

game_still_going = True
current_player = "X"
winner = None


def play_game():
    display_board()

    while game_still_going:

        handle_turn(current_player)

        isGameOver()

        flip_player()

    if winner == "X" or winner == 'O':
        print(winner + " won")
    elif winner == None:
        print('Game is a Tie')


def display_board():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
    print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
    print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")
    print("\n")


def handle_turn(player):

    print(player+"'s turn")
    position = input("Enter a position between 1-9: ")
    valid = False
    while not valid:

        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            position = input("Enter a position between 1-9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again")

    board[position] = player
    display_board()


def isGameOver():
    check_if_win()
    check_if_tie()


def check_if_win():

    global winner
    # check rows
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    # check columns
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        # check diagonals
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:  # any one has won
        game_still_going = False
    # check who won
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    else:
        return None


def check_columns():
    global game_still_going
    column1 = board[0] == board[3] == board[6] != "-"
    column2 = board[1] == board[4] == board[7] != "-"
    column3 = board[2] == board[5] == board[8] != "-"
    if column1 or column2 or column3:  # any one has won
        game_still_going = False
    # check who won
    if column1:
        return board[0]
    elif column2:
        return board[1]
    elif column3:
        return board[2]
    else:
        return None


def check_diagonals():
    global game_still_going
    diagonal1 = board[0] == board[4] == board[8] != "-"
    diagonal2 = board[2] == board[4] == board[6] != "-"

    if diagonal1 or diagonal2:  # any one has won
        game_still_going = False
    # check who won
    if diagonal1:
        return board[0]
    elif diagonal2:
        return board[2]
    else:
        return None


def check_if_tie():
    global game_still_going
    # If board is full
    if "-" not in board:
        game_still_going = False
        return True
    # Else there is no tie
    else:
        return False


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"


play_game()
