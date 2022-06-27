import sys
from collections import deque

col_num, row_num = map(int, sys.stdin.readline().split())
M = [input() for _ in range(row_num)]
laser = []
for row in range(row_num):
    for col in range(col_num):
        if M[row][col] == 'C':
            laser.append([row, col])
dist = [[col_num * row_num + 1 for _ in range(col_num)] for _ in range(row_num)]
# 위치, 방향, 횟수
que = deque([laser[0]])
dist[laser[0][0]][laser[0][1]] = 0
while que:
    now_row, now_col = que.popleft()
    for drow, dcol in zip([1, -1, 0, 0], [0, 0, 1, -1]):
        next_row = now_row + drow
        next_col = now_col + dcol
        while True:
            if not(0<=next_row<row_num and 0<=next_col<col_num):
                break
            if M[next_row][next_col]=='*':
                break
            if dist[next_row][next_col] < dist[now_row][now_col] + 1:
                break
            que.append([next_row, next_col])
            dist[next_row][next_col] = dist[now_row][now_col] + 1
            next_row += drow
            next_col += dcol
print(dist[laser[1][0]][laser[1][1]]-1)