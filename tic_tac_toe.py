import numpy
global player
user =True#when true it refers x else false
turns=0

board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]


def print_board(board):  # func to print board after each turn
    for row in board:
        for slot in row:
            print(f"{slot} ", end='')
        print()


def quit(user_input):  # func to quit
    if user_input == 'q':
        print('thanks for playing.')
        return True
    else:
        return False


def check_input(user_input):  # CHECK IF ITS A NO,

    if not isnum(user_input):
        return False
    user_input = int(user_input)
    # CHECK IF ITS 1 TO 9
    if not bounds(user_input): return False
    return True


def isnum(user_input):
    if not user_input.isnumeric():
        print("this is not a valid input")
        return False
    else:
        return True


def bounds(user_input):  # func to bound user input
    if user_input > 9 or user_input < 1:
        print("this is not a valid input")
        return False
    else:
        return True


def istaken(cords, board):  # to check which squres are taken
    row = coords[0]
    col = coords[1]
    if board[row][col] != '-':
        print('This position is already taken')
        return True
    else:
        return False


def cordinates(user_input):  # cordinates of board
    row = int(user_input / 3)
    col = user_input
    if col > 2: col = int(col % 3)
    return (row, col)


def add_to_board(coords, board,active_user):  # adding movees to board
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

def current_user(user):
    if user: return 'X'
    else:return 'O'

def iswin(user,board):
    if check_row(user,board):return True 
    if check_col(user,board):return True
    if check_diag(user,board): return True
    return False
        
def check_row(user,board):
    for row in board:
        complete_row=True
        for slot in row:
            if slot!=user:
                complete_row=False
                break
        if complete_row:return True
    return False

def check_col(user,board):
    for col in range(3):
        complete_col=True
        for row in range(3):
            if board[row][col]!=user:
                complete_col=False
                break
        if complete_col: return True
    return False

def check_diag(user,board):
    if board[0][0]==user and board[1][1]==user and board[2][2]==user: return True
    elif board[2][0]==user and board[1][1]==user and board[0][2]==user: return True
    return False

print_board(board)
while turns<9:
    active_user=current_user(user)

    user_input = input('plz enter a position 1 to 9 or enter or enter\'q\' to quit:')
    if quit(user_input):
        break
    if not check_input(user_input):
        print("plz try again")
        continue

    user_input = int(user_input) - 1
    coords = cordinates(user_input)
    if istaken(coords, board):
        print('plz try again')
        continue
    add_to_board(coords, board, active_user)
    if iswin(active_user,board):
        print(f'{active_user.upper()} won')
        break
    user=not user
    print_board(board)
    turns+=1
if turns==9:
    print('tie')

