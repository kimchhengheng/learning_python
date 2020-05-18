"""
board
display board
play game
handle turn
check win
    check row
    check colums
    check diagonals
check tie
flip player
"""
# ---global variable


board = []
for inc in range(9):
    board.append("-")

game_still_going = True
winner = None
current_player = "X"
num = 9
where = None


def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    # display initial board
    display_board()

    while game_still_going:
        handle_turn(current_player)
        check_if_game_over()
        flip_player()

    if winner == "X" or winner == "O":
        print(winner + " won")
        print(where)
    else:
        print("Tie. ")


def check_if_game_over():
    check_for_winner()
    check_if_tie()


def check_for_winner():
    # set/ change the value of global variable
    global winner

    row_winner = check_rows()
    column_winner = check_column()
    diagonal_winner = check_diagonals()
    # if check_rows() return None the if statement is false
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif check_diagonals():
        winner = diagonal_winner
    else:
        winner = None

    return


def check_rows():
    # global board no need since we only check not set any

    global game_still_going
    global where
    # it compare if the row is the same or not but not - so it is boolean
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    if row_1 or row_2 or row_3:
        game_still_going = False
    # return the winner (X or O) but not mention which row is the winning
    if row_1:
        where = "row 1"
        return board[0]
    elif row_2:
        where = "row 2"
        return board[3]
    elif row_3:
        where = "row 3"
        return board[6]
    return
    # if no return before this work return gonna return None


def check_column():
    global game_still_going
    global where
    # it compare if the row is the same or not but not - so it is boolean
    col_1 = board[0] == board[3] == board[6] != "-"
    col_2 = board[1] == board[4] == board[7] != "-"
    col_3 = board[2] == board[5] == board[8] != "-"
    if col_1 or col_2 or col_3:
        game_still_going = False
    # return the winner (X or O)
    if col_1:
        where = "column 1"
        return board[0]
    elif col_2:
        where = "column 2"
        return board[1]
    elif col_3:
        where = "column 3"
        return board[2]
    return


def check_diagonals():
    global game_still_going
    global where
    # it compare if the row is the same or not but not - so it is boolean
    dia_1 = board[0] == board[4] == board[8] != "-"
    dia_2 = board[6] == board[4] == board[2] != "-"
    if dia_1 or dia_2:
        game_still_going = False
    # return the winner (X or O)
    if dia_1:
        where = "diagonal top to down"
        return board[0]
    elif dia_2:
        where = "diagonal down to top"
        return board[6]
    return


def check_if_tie():
    global game_still_going
    # if "-" not in board # board is the list so we can check by not in
    if num == 0:
        game_still_going = False
    return


def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"
    return


def handle_turn(player):
    global num
    print("the current player is " + player)
    position = input("choose a position from 1-9: ")
    # we have to the input from varialbe can be cast into the int , in case user put inappropriate input we handle it
    repeat = True
    # it is not java so we can use while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
    # this mean while is not in the range we keep asking again the loop break only when the user put the number in the list
    while repeat:
        if position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid input choose a position from 1-9: ")
        elif board[int(position) - 1] != "-":
            position = input("the position is already token please choose a position from 1-9: ")
        else:
            repeat = False
    # we have to check the position is valid on the board to make the person does not override it
    position = int(position) - 1

    # set the the type of player
    if player == "X":
        board[position] = "X"
    else:
        board[position] = "O"
    num = num - 1
    display_board()


contin = True

while contin:
    play_game()
    inval = input("do you want to continue ")
    while inval.lower() != "yes" and inval.lower() != "no":
        inval = input("please indicate you want to continue or not ")
    if inval.lower() == "yes":
        game_still_going = True
        winner = None
        current_player = "X"
        num = 9
        where = None
        for inc in range(9):
            board[inc] = "-"
    elif inval.lower() == "no":
        contin = False

