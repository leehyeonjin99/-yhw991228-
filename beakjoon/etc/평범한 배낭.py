import sys

N, M = map(int, sys.stdin.readline().split())
weight_value = [[0 for _ in range(M+1)] for _ in range(N+1)]
for idx in range(1, N+1):
    weight, value = map(int, sys.stdin.readline().split())
    for compare in range(M+1):
        if compare >= weight:
            weight_value[idx][compare] = max(weight_value[idx-1][compare], weight_value[idx-1][compare - weight] + value)
        else:
            weight_value[idx][compare] = weight_value[idx-1][compare]
    print(weight_value[idx])
print(weight_value[-1][-1])

# DFS 메모리 초과
# from collections import deque
# N, M = map(int, sys.stdin.readline().split())
# weights = []
# values = []
# for _ in range(N):
#     weight, value = map(int, sys.stdin.readline().split())
#     weights.append(weight)
#     values.append(value)
# answer = 0
# for idx in range(N):
#     weight = weights[idx]
#     value = values[idx]
#     remainder = set(range(N)) - set([idx])
#     que = deque([[weight, value, remainder]])
#     while que:
#         weight, value, remainders = que.popleft()
#         for remainder in remainders:
#             if weight + weights[remainder] <= M:
#                 next_weight = weight + weights[remainder]
#                 next_value = value + values[remainder]
#                 next_remainders = remainders - set([remainder])
#                 que.append([next_weight, next_value, next_remainders])
#                 if answer < next_value:
#                     answer = next_value
# print(answer)