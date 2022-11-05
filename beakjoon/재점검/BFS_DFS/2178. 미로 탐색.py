import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

dcols = [0, 0, 1, -1]
drows = [1, -1, 0, 0]

visited = [[sys.maxsize for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
que = deque([[0, 0]])
while que:
    now_row, now_col = que.popleft()
    if [now_row, now_col] == [N - 1 , M - 1]:
        print(visited[now_row][now_col])
        break
    for (drow, dcol) in zip(drows, dcols):
        next_row = now_row + drow
        next_col = now_col + dcol
        if 0 <= next_row < N and 0 <= next_col < M and graph[next_row][next_col] == 1 and visited[now_row][now_col] + 1 < visited[next_row][next_col]:
            visited[next_row][next_col] = min(visited[next_row][next_col], visited[now_row][now_col] + 1)
            que.append([next_row, next_col])