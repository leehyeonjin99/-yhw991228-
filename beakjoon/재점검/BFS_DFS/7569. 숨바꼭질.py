import sys
from collections import deque

subin, sis = map(int, sys.stdin.readline().split())
visited = [sys.maxsize for _ in range(100001)]
visited[subin] = 0
que = deque([subin])
while que:
    now_subin = que.popleft()
    if now_subin == sis:
        print(visited[sis])
        break
    for dist in [-1, 1]:
        next_subin = now_subin + dist
        if 0 <= next_subin <= 100000 and visited[now_subin] + 1 < visited[next_subin]:
            visited[next_subin] = visited[now_subin] + 1
            que.append(next_subin)
    next_subin = now_subin * 2
    if 0 <= next_subin <= 100000 and visited[now_subin] + 1 <visited[next_subin]:
        visited[next_subin] = visited[now_subin] + 1
        que.append(next_subin)