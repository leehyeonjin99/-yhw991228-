import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().split())
r, c = r - 1, c - 1
board = []
for _ in range(3):
    board.append(list(map(int, sys.stdin.readline().split())))

def row_oper():
    max_length = 0
    new_board = []
    for row in board:
        new_row = []
        count = sorted(dict(Counter(row)).items(), key = lambda x : (x[1], x[0]))
        for (value, cnt) in count:
            if value == 0:
                continue
            new_row += [value, cnt]
        max_length = max(max_length, len(new_row))
        new_board.append(new_row)
    for row in range(len(new_board)):
        if len(new_board[row]) == max_length:
            continue
        else:
            new_board[row] += [0 for _ in range(max_length - len(new_board[row]))]
    return new_board

def solution():
    global board
    day = 0
    while day <= 100:
        if len(board) > r and len(board[0]) > c and board[r][c] == k:
            return day
        if len(board) >= len(board[0]):
            board = row_oper()
        else:
            board = [list(tmp) for tmp in zip(*board)]
            board = row_oper()
            board = [list(tmp) for tmp in zip(*board)]
        day += 1
    return -1

print(solution())