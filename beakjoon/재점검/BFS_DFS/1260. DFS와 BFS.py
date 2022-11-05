import sys
from collections import deque

N, M, V = map(int , sys.stdin.readline().split())
graph = {idx : [] for idx in range(1, N + 1)}
for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    graph[start].append(end)
    graph[end].append(start)

for idx in graph.keys():
    graph[idx].sort()

visited = []
def dfs(v):
    visited.append(v)
    for next_v in graph[v]:
        if next_v not in visited:
            dfs(next_v)
dfs(V)
print(*visited)
   
visited = [V]
que = deque([])
que.append(V)
while que:
    now_vertice = que.popleft()
    for next_vertice in graph[now_vertice]:
        if next_vertice not in visited:
            que.append(next_vertice)
            visited.append(next_vertice)
print(*visited)