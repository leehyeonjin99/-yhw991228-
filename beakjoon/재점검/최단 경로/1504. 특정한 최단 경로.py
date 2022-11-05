import sys
import heapq
V, E = map(int, sys.stdin.readline().split())
graph = {idx : [] for idx in range(1, V + 1)}
for _ in range(E):
    v1, v2, cost = map(int, sys.stdin.readline().split())
    graph[v1].append([v2, cost])
    graph[v2].append([v1, cost])
# print(graph)

e1, e2 = map(int, sys.stdin.readline().split())

def bfs(start_point):
    dist = [sys.maxsize for _ in range(V + 1)]
    dist[start_point] = 0
    heap = []
    heapq.heappush(heap, [0, start_point])
    while heap:
        now_cost, now_pos = heapq.heappop(heap)
        for next_pos, cost in graph[now_pos]:
            if now_cost + cost < dist[next_pos]:
                dist[next_pos] = now_cost + cost
                heapq.heappush(heap, [dist[next_pos], next_pos])
    return dist

start = bfs(1)
point1 = bfs(e1)
point2 = bfs(e2)

answer = min(start[e1] + point1[e2] + point2[V], start[e2] + point2[e1] + point1[V])
print(answer if answer < sys.maxsize else -1)