import sys

N, M, x, y, K = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
dir = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
direction = list(map(int, sys.stdin.readline().split()))
dice = [0 for _ in range(6)]

def turn(dice, dir):
    a, b, c, d, e, f = dice
    if dir == 1:
        dice = [d, b, a, f, e, c]
    elif dir == 2:
        dice = [c, b, f, a, e, d]
    elif dir == 3:
        dice = [e, a, c, d, f, b]
    elif dir == 4:
        dice = [b, f, c, d, a, e]
    return dice

def change_dice():
    if board[x][y] == 0:
        board[x][y] = dice[-1]
    else:
        dice[-1] = board[x][y]
        board[x][y] = 0

change_dice()


for d in direction:
    next_x = x + dir[d][0]
    next_y = y + dir[d][1]
    if 0 <= next_x < N and 0 <= next_y < M:
        x, y = next_x, next_y
        dice = turn(dice, d)
        change_dice()
        print(dice[0])
