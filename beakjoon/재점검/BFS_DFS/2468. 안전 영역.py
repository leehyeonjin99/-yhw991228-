import sys
from collections import deque

N = int(sys.stdin.readline())
graph = []
max_h = 0
for _ in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    max_h = max(max(row), max_h)
    graph.append(row)

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
max_answer = 1
for rain in range(1, max_h):
    answer = 0
    visited = [[False for _ in range(N)] for _ in range(N)]
    # print("RAIN :", rain, end = '->')
    for row in range(N):
        for col in range(N):
            if graph[row][col] > rain and not visited[row][col]:
                answer += 1
                visited[row][col] = answer
                que = deque([[row, col]])
                while que:
                    now_row, now_col = que.popleft()
                    for drow, dcol in zip(drows, dcols):
                        next_row = now_row + drow
                        next_col = now_col + dcol
                        if 0 <= next_row < N and 0 <= next_col < N and not visited[next_row][next_col] and graph[next_row][next_col] > rain:
                            visited[next_row][next_col] = answer
                            que.append([next_row, next_col])
    # print(answer)
    max_answer = max(max_answer, answer)

print(max_answer)