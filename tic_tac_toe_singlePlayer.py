"""
display the board
get the number of place where he want
check if it is availble and not overide the other
check win row colume and diagonal or tie
check the winner
alternate the turn to computer

input will be get as a string only
"""
import random
import sys

board = []
for var in range(9):
    board.append("-")
winnner = None


def display():
    print(board[0] + " | " + board[1] + " | " + board[2] + " \n" +
          board[3] + " | " + board[4] + " | " + board[5] + " \n" +
          board[6] + " | " + board[7] + " | " + board[8])


def check_input(position, player):
    if position.isnumeric() and 0 < int(position) < 10 and board[int(position) - 1] == "-":
        validinput = int(position)
        board[validinput-1] = player
    else:
        while True:
            if not position.isnumeric():
                print("Make sure to choose the number only ")
                position = input("Please enter the number of position you want to choose from 1-9 ")
            else:
                position = int(position)
                if position < 1 or position > 9:
                    print("Make sure the number from 1 to 9 only")
                    position = input("Please enter the number of position you want to choose from 1-9 ")
                elif board[position - 1] != "-":
                    print("the position is choosen already by ", board[int(position) - 1])
                    position = input("Please enter the number of position you want to choose from 1-9 ")
            if position.isnumeric() and 0 < int(position) < 10 and board[int(position) - 1] == "-":
                validinput = int(position) - 1
                board[validinput] = player
                break


"""
def check_winner():
    check_row()
    check_column()
    check_diagonal()


def check_row():
    if board[0] == board[1] == board[2] != "-":
        winner = board[0]
    elif board[3] == board[4] == board[5] != "-":
        winner = board[3]
    elif board[6] == board[7] == board[8] != "-":
        winner = board[3]


def check_column():
    if board[0] == board[3] == board[6] != "-":
        winner = board[0]
    elif board[1] == board[4] == board[7] != "-":
        winner = board[1]
    elif board[2] == board[5] == board[8] != "-":
        winner = board[3]


def check_diagonal():
    if board[0] == board[4] == board[8] != "-":
        winner = board[0]
    elif board[6] == board[4] == board[2] != "-":
        winner = board[1]

"""
"""
first we get the all the possible move that we can 
then if the computer can win we gonna make it that 
1 check the winner 
if computer cannnot win we have to check the player can win or not if player can win we gonna defend it 
if both cannot win go to the corner
2 check the corner
choose one of the corner by random
3 check the center 
4 check the edge 

"""


def computer_turn():
    possible = [x for x, letter in enumerate(board) if letter == "-"]
    # it is loop to get the free position availble for computer move
    # x is the index letter the value at that index so count from 0
    #print(possible)
    move = -1
    for play in ["O", "X"]:
        for i in possible:
            boardcopy = board[:] # this clone to avoid the copy and the orin have the same pointer mean change in copy will affect original
            boardcopy[i] = play
            if iswinner(boardcopy, play):
                #print("winner ", play)
                move = i
                return move
    opencorner = [var for var in possible if var in [0, 2, 6, 8]]
    if len(opencorner) > 1: # make sure it is not empty list
        move = random.choice(opencorner)
        #print(move)
        return move
    if 5 in possible:
        move = 5
        #print(move)
        return move
    edgecorner = [var for var in possible if var in [1, 3, 5, 7]]
    if len(edgecorner) > 1: # make sure it is not empty list
        move = random.choice(edgecorner)
        #print(move)
    return move



def check_tie():
    if board.count("-") == 0:
        return True
    else:
        return False


def iswinner(bo, play):
    return (bo[0] == bo[1] == bo[2] == play) or (bo[3] == bo[4] == bo[5] == play) or (bo[6] == bo[7] == bo[8] == play) \
           or (bo[0] == bo[3] == bo[6] == play) or (bo[1] == bo[4] == bo[7] == play) or (
                       bo[2] == bo[5] == bo[8] == play) \
           or (bo[0] == bo[4] == bo[8] == play) or (bo[2] == bo[4] == bo[6] == play)

finished = None
display()
while True:
    position = input("Please enter the number of position you want to choose from 1-9 ")
    check_input(position, "X")
    display()
    if not iswinner(board, "X"):
        if not check_tie():
            move = computer_turn()
            if move != -1:
                board[move] = "O"
                print("computer have place at position ", move)
                display()
            else:
                print("computer cannot get the position")
            if iswinner(board, "O"):
                print("you lose the game")
                finished = True
        else:
            print("Tie game")
            finished = True
    else:
        print("congratulation you have win the game")
        finished = True

    if finished:
        repeated = input("do you want restart the game").lower()
        if repeated == "y":
            board = []
            for var in range(9):
                board.append("-")
                finished= None
        else:
            sys.exit(0)