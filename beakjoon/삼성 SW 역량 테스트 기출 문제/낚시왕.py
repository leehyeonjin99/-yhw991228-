import sys
from copy import deepcopy
input = sys.stdin.readline
R, C, M = map(int, input().split())
sharks_locs = set([])
board = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r, c, s, d, z = map(int, input().split())  # 속력, 방향, 크기
    r, c = r - 1, c - 1
    board[r][c] = [s, d, z]
    sharks_locs.add((r, c))

dirs = {1: [-1, 0], 2: [1, 0], 3: [0, 1], 4: [0, -1]}

def fishing():
    global answer, board, sharks_locs
    for row in range(R):
        if board[row][col]:
            answer += board[row][col][2]
            board[row][col] = []
            sharks_locs.remove((row, col))
            break

def moving():
    global sharks_locs, board
    new_board = [[[] for _ in range(C)] for _ in range(R)]
    new_sharks_locs = set([])
    for (row, col) in sharks_locs:
        (v, d, s) = board[row][col]
        board[row][col] = []
        now_row, now_col = row, col
        (drow, dcol) = dirs[d]
        for move in range(v):
            next_row, next_col = now_row + drow, now_col + dcol
            if not (0 <= next_row < R and 0 <= next_col < C):
                drow, dcol = -drow, -dcol
                d = d - 1 if d % 2 == 0 else d + 1
                next_row, next_col = now_row + drow, now_col + dcol
            now_row, now_col = next_row, next_col
        if new_board[now_row][now_col] and new_board[now_row][now_col][-1] > s:
            continue
        new_board[now_row][now_col] = [v, d, s]
        new_sharks_locs.add((now_row, now_col))
    board = new_board
    sharks_locs = new_sharks_locs

answer = 0
for col in range(C):
    fishing()
    moving()

print(answer)