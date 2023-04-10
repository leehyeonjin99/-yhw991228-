import sys
N, Q = map(int, sys.stdin.readline().split())
R = C = 2 ** N
board = []
for _ in range(R):
    board.append(list(map(int, sys.stdin.readline().split())))
L = list(map(int, sys.stdin.readline().split()))

def take_partial(row, col):
    partial = []
    for tmp_row in board[row: row + tmp_R]:
        partial.append(tmp_row[col: col + tmp_C])
    return partial

def rotate(mat):
    return [list(tmp[::-1]) for tmp in zip(*mat)]

def rotation():
    final_matrix = []
    for row in range(0, R, tmp_R):
        tmp_matrix = []
        for col in range(0, C, tmp_C):
            partial_rot_matrix = rotate(take_partial(row, col))
            tmp_matrix.append(partial_rot_matrix)
        final_row_matrix = []
        for tmps in zip(*tmp_matrix):
            row_tmp = []
            for tmp in tmps:
                row_tmp += tmp
            final_row_matrix.append(row_tmp)
        final_matrix += final_row_matrix
    return final_matrix

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]

def processing():
    check_board = [tmp.copy() for tmp in board]
    for row in range(R):
        for col in range(C):
            if board[row][col] == 0:
                continue
            ice = 0
            for (drow, dcol) in zip(drows, dcols):
                next_row = row + drow
                next_col = col + dcol
                if 0 <= next_row < R and 0 <= next_col < C and check_board[next_row][next_col] > 0:
                    ice += 1
            if ice <= 2:
                board[row][col] -= 1

from collections import deque
def solution():
    ice = 0
    max_ice = 0
    visited = [[0 for _ in range(R)] for _ in range(C)]
    for row in range(R):
        for col in range(C):
            ice += board[row][col]
            if board[row][col] == 0:
                visited[row][col] = 1
                continue
            if visited[row][col] == 1:
                continue
            visited[row][col] = 1
            que = deque([[row, col]])
            tmp_ice = 1
            while que:
                now_row, now_col = que.popleft()
                for (drow, dcol) in zip(drows, dcols):
                    next_row, next_col = now_row + drow, now_col + dcol
                    if 0 <= next_row < R and 0 <= next_col < C and board[next_row][next_col] > 0 and not visited[next_row][next_col]:
                        visited[next_row][next_col] = 1
                        tmp_ice += 1
                        que.append([next_row, next_col])
            max_ice = max(max_ice, tmp_ice)
    return ice, max_ice



for l in L:
    tmp_R = tmp_C = 2 **l
    board = rotation()
    processing()

ans1, ans2 = solution()
print(ans1)
print(ans2)