import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
village = []
homes = []
chickens = []
for row in range(N):
    village_row = list(map(int, sys.stdin.readline().split()))
    for col in range(N):
        if village_row[col] == 1:
            homes.append([row, col])
        elif village_row[col] == 2:
            chickens.append([row, col])

answer = 2 * N * 2 * N
for chickens_comb in combinations(chickens, M):
    sum_dist = 0
    for home in homes:
        min_dist = 2 * N
        for chicken in chickens_comb:
            dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
            min_dist = min(min_dist, dist)
        sum_dist += min_dist
    answer = min(answer, sum_dist)
    
print(answer)

# 각 point에서의 최솟값의 합이 도시 치킨 거리의 최솟값이 아니므로 오류
# while True:
#     pick_village = set()
#     chicken_dist_sum = {idx: 0 for idx in range(len(chickens))}
#     answer = 0
#     for home in homes:
#         min_dist = N
#         min_idx = 0
#         for chicken_idx, chicken in enumerate(chickens):
#             dist = abs(home[0] - chicken[0]) + abs(home[1] - chicken[1])
#             chicken_dist_sum[chicken_idx] += dist
#             if dist < min_dist:
#                 min_dist = dist
#                 min_idx = chicken_idx
#         pick_village.add(min_idx)
#         answer += min_dist
#     if len(pick_village) <= M:
#         print(answer)
#         break
#     sorted_dist = sorted(chicken_dist_sum.items(), key = lambda item: item[1], reverse = True)
#     max_dist_chicken_idx = sorted_dist[0][0]
#     chickens.pop(max_dist_chicken_idx)