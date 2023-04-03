import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque

N, M = map(int, input().split())
board = []
virus = []
nothing = []
total = 0
for row in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for col in range(M):
        if tmp[col] == 0:
            nothing.append([row, col])
            total += 1
        elif tmp[col] == 2:
            virus.append([row, col])

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
answer = 0
for (r1, c1), (r2, c2), (r3, c3) in combinations(nothing, 3):
    
    board[r1][c1] = 1
    board[r2][c2] = 1
    board[r3][c3] = 1

    max_answer = total - 3
    visited = set([])
    que = deque([])
    for (v1, v2) in virus:
        que.append([v1, v2])
        visited.add((v1, v2))
    while que:
        now_row, now_col = que.popleft()
        for (drow, dcol) in zip(drows, dcols):
            next_row = now_row + drow
            next_col = now_col + dcol
            if not (0 <= next_row < N and 0 <= next_col < M):
                continue
            if board[next_row][next_col] == 1:
                continue
            if (next_row, next_col) in visited:
                continue
            que.append([next_row, next_col])
            visited.add((next_row, next_col))
            max_answer -= 1
    answer = max(answer, max_answer)
    
    board[r1][c1] = 0
    board[r2][c2] = 0
    board[r3][c3] = 0

print(answer)