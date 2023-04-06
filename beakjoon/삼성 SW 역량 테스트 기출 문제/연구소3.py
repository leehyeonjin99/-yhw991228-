import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
viruses = []
total_virus = N * N
for row in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for col, value in enumerate(tmp):
        if value == 2:
            viruses.append((row, col))
        elif value == 1:
            total_virus -= 1

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
answer = sys.maxsize
for active_viruses in combinations(viruses, M):
    new_board = [[0 for _ in range(N)] for _ in range(N)]
    active_viruses = set(active_viruses)
    que = deque([])
    for virus in active_viruses:
        que.append([virus, 0])
    max_time = 0
    while que:
        (now_row, now_col), now_cnt = que.popleft()
        if board[now_row][now_col] != 2:
            max_time = max(max_time, now_cnt)
        for drow, dcol in zip(drows, dcols):
            next_row, next_col = now_row + drow, now_col + dcol
            if 0 <= next_row < N and 0 <= next_col < N and board[next_row][next_col] != 1 and (next_row, next_col) not in active_viruses:
                active_viruses.add((next_row, next_col))
                next_cnt = now_cnt + 1
                que.append([(next_row, next_col), next_cnt])
    if len(active_viruses) == total_virus:
        answer = min(answer, max_time)

print(answer if answer < sys.maxsize else -1)