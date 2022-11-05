import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]

def group():
    grp_cnt = 0
    visited = [[False for _ in range(M)] for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if graph[row][col] and not visited[row][col]:
                visited[row][col] = True
                grp_cnt += 1
                que = deque([[row, col]])
                while que:
                    now_row, now_col = que.popleft()
                    for drow, dcol in zip(drows, dcols):
                        next_row = now_row + drow
                        next_col = now_col + dcol
                        if 0 <= next_row < N and 0 <= next_col < M and graph[next_row][next_col] and not visited[next_row][next_col]:
                            visited[next_row][next_col] = True
                            que.append([next_row, next_col])
    return grp_cnt

answer = 0
while True:
    answer += 1
    # 줄어들 빙각 계산
    sub = [[0 for _ in range(M)] for _ in range(N)]
    for row in range(N):
        for col in range(M):
            if graph[row][col] > 0:
                for drow, dcol in zip(drows, dcols):
                    ad_row = row + drow
                    ad_col = col + dcol
                    if 0 <= ad_row < N  and 0 <= ad_col < M and graph[ad_row][ad_col] == 0:
                        sub[row][col] -= 1

    # 낮아질 빙산이 없다면 종료
    if sum(sum(row) for row in sub) == 0:
        if group() > 1:
            print(answer)
        else:
            print(0)
        break

    for row in range(N):
        for col in range(M):
            graph[row][col] += sub[row][col]
            graph[row][col] = max(0, graph[row][col])
    
    grp_cnt = group()
    if grp_cnt > 1:
        print(answer)
        break