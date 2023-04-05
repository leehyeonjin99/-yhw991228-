import sys
from collections import deque
input = sys.stdin.readline
N, L, R = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def solution(row, col):
    pos, sum, cnt = [[row, col]], board[row][col], 1
    que = deque([[row, col]])
    visited[row][col] = 1
    while que:
        now_row, now_col = que.popleft()
        for (drow, dcol) in zip(drows, dcols):
            next_row, next_col = now_row + drow, now_col + dcol
            if 0 <= next_row < N  and 0 <= next_col < N and visited[next_row][next_col] == 0 and L <= abs(board[now_row][now_col] - board[next_row][next_col]) <= R:
                visited[next_row][next_col] = 1
                cnt += 1
                sum += board[next_row][next_col]
                pos.append([next_row, next_col])
                que.append([next_row, next_col])
    next_pop = sum // cnt
    if cnt > 1:
        for (row, col) in pos:
            board[row][col] = next_pop

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
day = 0
while True:
    visited = [[0 for _ in range(N)] for _ in range(N)]
    city_idx = 0
    for row in range(N):
        for col in range(N):
            if visited[row][col] > 0:
                continue
            solution(row, col)
            city_idx += 1
    if city_idx == N * N:
        break
    day += 1
    
print(day)