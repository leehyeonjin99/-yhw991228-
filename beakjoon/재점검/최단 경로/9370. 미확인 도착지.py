import sys
from heapq import heappop, heappush

T = int(sys.stdin.readline())

for _ in range(T):
    V, E, N = map(int, sys.stdin.readline().split())
    graph = {idx : [] for idx in range(1, V + 1)}
    S, V1, V2 = map(int, sys.stdin.readline().split())
    for _ in range(E):
        v1, v2, cost = map(int, sys.stdin.readline().split())
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])
    goals = []
    for _ in range(N):
        goals.append(int(sys.stdin.readline()))

    def bfs(start_point):
        visited = [sys.maxsize for _ in range(V + 1)]
        visited[start_point] = 0
        heap = []
        heappush(heap, [0, start_point])
        while heap:
            now_cost, now_pos = heappop(heap)
            for next_pos, cost in graph[now_pos]:
                if now_cost + cost < visited[next_pos]:
                    visited[next_pos] = now_cost + cost
                    heappush(heap, [visited[next_pos], next_pos])
        return visited
    
    for v, c in graph[V1]:
        if v == V2:
            v1v2 = c
    
    start_s = bfs(S)
    start_v1 = bfs(V1)
    start_v2 = bfs(V2)
    # print(start_s)
    # print(start_v1)
    # print(v1v2)
    # print(start_v2)

    answer = []
    # print("start :", S, V1, V2)
    for goal in goals:
        case1 = start_s[V1] + v1v2 + start_v2[goal]
        case2 = start_s[V2] + v1v2 + start_v1[goal]
        # print(f"goal : {goal} -> {start_s[v1]} + {v1v2} + {start_v2[goal]}, {start_s[v2]} + {v1v2} + {start_v1[goal]}")
        real_min = start_s[goal]
        if case1 == real_min or case2 == real_min:
            answer.append(goal)
    answer.sort()
    print(*answer)

    