import sys
from collections import deque
import heapq

N, M = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().split())))

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
heap = [[-graph[0][0], 0, 0]]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
answer = 0
while heap:
    now_h, now_row, now_col = heapq.heappop(heap)
    for drow, dcol in zip(drows, dcols):
        next_row = now_row + drow
        next_col = now_col + dcol
        if 0 <= next_row < N and 0 <= next_col < M and graph[next_row][next_col] < graph[now_row][now_col]:
            if not visited[next_row][next_col]:
                heapq.heappush(heap, [-graph[next_row][next_col], next_row, next_col])
            visited[next_row][next_col] += visited[now_row][now_col]

print(visited[-1][-1])