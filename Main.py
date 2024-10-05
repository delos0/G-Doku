print("Enter k:")
k = int(input())
print("Enter n:")
n = int(input())
board = [[0 for i in range(k**2)] for j in range(k**2)]

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE


l = len(str(n))
def print_board():
    for row in board:
        for cell in row:
            if cell:
                print(f'|{cell:>{l}}', end='')
            else:
                print(f"|{'':>{l}}", end='')
        print('|')


def make_move(mv):
    row = (mv[0] // k) * k + mv[1] // k
    column = (mv[0] % k) * k + mv[1] % k
    prev_val = board[row][column]
    board[row][column] = mv[2]

    return prev_val

def verify_board():
    valid = True
    solved = True
    for box in range(k**2):
        row = (box // k) * k
        column = (box % k) * k
        box_sum = 0
        for i in range(k):
            for j in range(k):
                box_sum += board[row+i][column+j]
                if board[row+i][column+j] == 0:
                    solved = False
        if box_sum > n:
            valid = False
            break
        elif box_sum < n:
            solved = False

    for i in range(k**2):
        row_sum = 0
        column_sum = 0
        for j in range(k**2):
            row_sum += board[i][j]
            column_sum += board[j][i]
        if row_sum > n or column_sum > n:
            valid = False
            break
        elif row_sum < n or column_sum < n:
            solved = False

    if not valid:
        return -1
    else:
        if solved:
            return 1
        else:
            return 0


# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

print_board()
print("Next Move:")
command = ""
while command != "end":
    usr_inp = input().split()
    command = usr_inp[0]
    if command == "move":
        move = int(usr_inp[1]), int(usr_inp[2]), int(usr_inp[3])
        prev_val = make_move(move)
        result = verify_board()
        # If not valid move, undo the move
        if -1 == result:
            move = move[0], move[1], prev_val
            make_move(move)
            print_board()
            print("Your move was invalid, please try again:")
        # If the board wins, end the game
        elif 1 == result:
            print_board()
            print("Congratulations! You have solved the puzzle!")
            break
        else:
            print_board()
            print("Next Move:")




