import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visited = [sys.maxsize for _  in range(F + 1)]
visited[S] = 0
que = deque([S])
while que:
    now_h = que.popleft()
    if now_h == G:
        break
    for d in [U, -D]:
        next_h = now_h + d
        if 0 < next_h <= F and visited[now_h] + 1 < visited[next_h]:
            visited[next_h] = visited[now_h] + 1
            que.append(next_h)

if visited[G] < sys.maxsize:
    print(visited[G])
else:
    print("use the stairs")