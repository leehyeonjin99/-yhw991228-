import sys
from collections import deque

N = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
graph = {idx : [] for idx in range(1, N + 1)}

M = int(sys.stdin.readline())
for _ in range(M):
    t1, t2 = map(int, sys.stdin.readline().split())
    graph[t1].append(t2)
    graph[t2].append(t1)

visited = [False for _ in range(N + 1)]
que = deque([[p1, 0]])
check = False
while que:
    now_p, now_cnt = que.popleft()
    if now_p == p2:
        print(now_cnt)
        check = True
        break
    for next_p in graph[now_p]:
        if not visited[next_p]:
            visited[next_p] = True
            que.append([next_p, now_cnt + 1])

if not check:
    print(-1)