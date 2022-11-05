import sys
from heapq import heappop, heappush

subin, sis = map(int, sys.stdin.readline().split())

dist = [sys.maxsize for _ in range(100001)]
heap = []
heappush(heap, [0, subin])
while heap:
    now_cost, now_subin = heappop(heap)
    if now_subin == sis:
        print(now_cost)
        break
    for d in [-1, 1]:
        if 0 <= now_subin + d <= 100000 and now_cost + 1 < dist[now_subin + d]:
            dist[now_subin + d] = now_cost + 1
            heappush(heap, [now_cost + 1, now_subin + d])
    if 0<= now_subin * 2 <= 100000 and now_cost < dist[now_subin * 2]:
        dist[now_subin * 2] = now_cost
        heappush(heap, [now_cost, now_subin * 2])