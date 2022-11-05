import sys
from collections import deque

V = int(sys.stdin.readline())
E = int(sys.stdin.readline())
graph = {idx : [] for idx in range(1, V + 1)}

for _ in range(E):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = set([1])
que = deque([1])
while que:
    now_computer = que.popleft()
    for next_computer in graph[now_computer]:
        if next_computer not in visited:
            visited.add(next_computer)
            que.append(next_computer)

print(len(visited) - 1)