from collections import deque
from itertools import combinations
import sys

N, M = map(int, sys.stdin.readline().split())
Lab = []
Virus = []
num_blank = 0
visited = [[-1 for _ in range(N)] for _ in range(N)]
for row in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    Lab.append(tmp)
    for col in range(N):
        # 바이러스인 경우
        if tmp[col] == 2:
            Virus.append([row, col])
        # 벽인 경우
        if tmp[col] == 1:
            visited[row][col] = 0

dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
answer = sys.maxsize

for selected_v in combinations(Virus, M):
    # print("="*10, selected_v)
    que = deque([[row, col, 0] for (row, col) in selected_v])
    visited_tmp = [v.copy() for v in visited]
    for virus_row, virus_col in selected_v:
        visited_tmp[virus_row][virus_col] = 0
    while que:
        virus_row, virus_col, time = que.popleft()
        if [virus_row, virus_col] not in Virus and time > answer:
            # print("CAN'T")
            continue
        for (drow, dcol) in dirs:
            next_virus_row = virus_row + drow
            next_virus_col = virus_col + dcol
            if 0 <= next_virus_row < N and 0 <= next_virus_col < N and Lab[next_virus_row][next_virus_col] != 1 and visited_tmp[next_virus_row][next_virus_col] == -1:
                que.append([next_virus_row, next_virus_col, time + 1])
                visited_tmp[next_virus_row][next_virus_col] = time + 1
                
    check = True
    max_time = 0
    for row in range(N):
        # print(*visited_tmp[row])
        for col in range(N):
            if visited_tmp[row][col] == -1:
                check = False
                break
            if [row, col] in Virus:
                continue
            max_time = max(max_time, visited_tmp[row][col])
        if not check:
            break

    # print(max_time)
    if check:
        answer = min(answer, max_time)

if answer == sys.maxsize:
    print(-1)
else:
    print(answer)