import sys
input = sys.stdin.readline
N = int(input())
blocks = []
for _ in range(N):
    blocks.append(list(map(int, input().split())))

green = [[0 for _ in range(4)] for _ in range(6)]
blue = [[0 for _ in range(4)] for _ in range(6)]

def one_block(col, board):
    new_board = [tmp.copy() for tmp in board]
    for R in range(6):
        if board[R][col] == 1:
            break
    R -= 1
    if R == 4 and board[5][col] == 0:
        new_board[5][col] = 1
    else:
        new_board[R][col] = 1
    return new_board

def one_by_two(col, board):
    new_board = [tmp.copy() for tmp in board]
    col1, col2 = col, col + 1
    for R in range(6):
        if board[R][col1] == 1 or board[R][col2] == 1:
            break
    R -= 1
    if R == 4 and board[5][col1] == 0 and board[5][col2] == 0:
        new_board[5][col1] = 1
        new_board[5][col2] = 1
    else:
        new_board[R][col1] = 1
        new_board[R][col2] = 1
    return new_board

def two_by_one(col, board):
    new_board = [tmp.copy() for tmp in board]
    for R in range(6):
        if board[R][col] == 1:
            break
    R -= 1
    if R == 4 and board[5][col] == 0:
        new_board[5][col] = 1
        new_board[4][col] = 1
    else:
        new_board[R][col] = 1
        new_board[R - 1][col] = 1
    return new_board

def check_row(board):
    score = 0
    new_board = []
    for R in range(6):
        if sum(board[R]) == 4:
            score += 1
        else:
            new_board.append(board[R].copy())
    new_board = [[0 for _ in range(4)] for _ in range(score)] + new_board
    if 1 in new_board[0]:
        new_board = [[0 for _ in range(4)] for _ in range(2)] + new_board[:-2]
    elif 1 in new_board[1]:
        new_board = [[0 for _ in range(4)]] + new_board[:-1]
    return new_board, score

answer = 0
for (type, row, col) in blocks:
    if type == 1:
        green = one_block(col, green)
        blue = one_block(row, blue)
    elif type == 2:
        green = one_by_two(col, green)
        blue = two_by_one(row, blue)
    elif type == 3:
        green = two_by_one(col, green)
        blue = one_by_two(row, blue)
    green, add_score = check_row(green)
    answer += add_score
    blue, add_score = check_row(blue)
    answer += add_score

print(answer)
blocks = 0
for row in range(6):
    for col in range(4):
        if blue[row][col]:
            blocks += 1
        if green[row][col]:
            blocks += 1
print(blocks)