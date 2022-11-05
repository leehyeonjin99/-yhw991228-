import sys
from collections import deque
N = int(sys.stdin.readline())
graph = []
for _ in range(N):
    graph.append(list(map(int, list(sys.stdin.readline())[:-1])))

visited = [[False for _ in range(N)] for _ in range(N)]
estate_cnt = 0
answer = []

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]

for row in range(N):
    for col in range(N):
        if graph[row][col] == 1 and not visited[row][col]:
            estate_cnt += 1
            cnt = 1
            que = deque([[row, col]])
            visited[row][col] = True
            while que:
                now_row, now_col = que.popleft()
                for drow, dcol in zip(drows, dcols):
                    next_row = now_row + drow
                    next_col = now_col + dcol
                    if 0 <= next_row < N and 0 <= next_col < N and graph[next_row][next_col] == 1 and not visited[next_row][next_col]:
                        visited[next_row][next_col] = True
                        cnt += 1
                        que.append([next_row, next_col])
            answer.append(cnt)

print(estate_cnt)
answer.sort()
for cnt in answer:
    print(cnt)