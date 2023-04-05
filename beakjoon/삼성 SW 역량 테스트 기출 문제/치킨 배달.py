import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
houses = []
chickens = []
for row in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for col in range(N):
        if tmp[col] == 1:
            houses.append([row, col])
        elif tmp[col] == 2:
            chickens.append([row, col])

answer = 2 * N * len(houses)
for M_chickens in combinations(chickens, M):
    tmp_answer = 0
    for house in houses:
        tmp_tmp_answer = 2 * N
        for chicken in M_chickens:
            dist = abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])
            tmp_tmp_answer = min(tmp_tmp_answer, dist)
        tmp_answer += tmp_tmp_answer
    answer = min(answer, tmp_answer)

print(answer)