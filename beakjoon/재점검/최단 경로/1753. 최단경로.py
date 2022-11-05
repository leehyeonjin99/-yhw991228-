import sys
import heapq

V, E = map(int, sys.stdin.readline().split())
S = int(sys.stdin.readline())
graph = {idx : [] for idx in range(1, V + 1)}
for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append([v2, cost])

visited = [sys.maxsize for _ in range(V + 1)]
visited[S] = 0
heap = [[0, S]]
while heap:
    now_cost, now_pos = heapq.heappop(heap)
    for next_pos, cost in graph[now_pos]:
        if now_cost + cost < visited[next_pos]:
            visited[next_pos] = now_cost + cost
            heapq.heappush(heap, [visited[next_pos], next_pos])

for dist in visited[1:]:
    print(dist if dist < sys.maxsize else "INF")