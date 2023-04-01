import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
baord = []
answer = 0
for _ in range(N):
    tmp = list(map(int, input().split()))
    baord.append(tmp)
    answer = max(answer, max(tmp))

def solution(dir):
    global answer
    dirs = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
    (drow, dcol) = dirs[dir]
    next_board = [tmp.copy() for tmp in now_board]
    addition = [[False for _ in range(N)] for _ in range(N)]
    for row in range(N - 1 if dir == 4 else 0, -1 if dir == 4 else N, -1 if dir == 4 else 1):
        for col in range(N - 1 if dir == 1 else 0, -1 if dir == 1 else N, -1 if dir == 1 else 1):
            now_row, now_col = row, col
            value = next_board[now_row][now_col]
            next_board[now_row][now_col] = 0
            while True:
                next_row, next_col = now_row + drow, now_col + dcol
                if not (0 <= next_row < N and 0 <= next_col < N):
                    next_board[now_row][now_col] = value
                    break
                elif next_board[next_row][next_col] == 0:
                    now_row, now_col = next_row, next_col
                elif value == next_board[next_row][next_col] and not addition[next_row][next_col]:
                    next_board[next_row][next_col] += value
                    answer = max(answer, next_board[next_row][next_col])
                    addition[next_row][next_col] = True
                    break
                else:
                    next_board[now_row][now_col] = value
                    break
    return next_board

que = deque([[baord, 0]])
while que:
    now_board, now_cnt = que.popleft()
    if now_cnt == 5:
        continue
    
    for dir in range(1, 5):
        next_board = solution(dir)
        que.append([next_board, now_cnt + 1])
                
print(answer)        