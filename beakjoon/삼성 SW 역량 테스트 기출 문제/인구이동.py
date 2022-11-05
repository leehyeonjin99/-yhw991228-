import sys
from collections import deque

sys.setrecursionlimit(10**5)
nation = []
N, L, R = map(int, sys.stdin.readline().split())
for _ in range(N):
    nation.append(list(map(int, sys.stdin.readline().split())))

day = 0
dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]]
while True:
    # print(f"Day {day}")
    visited = [[0 for _ in range(N)] for _ in range(N)]
    union_count = 0
    for not_visit_row in range(N):
        for not_visit_col in range(N):
            if visited[not_visit_row][not_visit_col] == 0:
                visited[not_visit_row][not_visit_col] = 1
                need_explore = False
                # 시간 초과 방지를 위해 주변 탐색이 필요한지 확인
                for dir in dirs:
                        next_row = not_visit_row + dir[0]
                        next_col = not_visit_col + dir[1]
                        if 0 <= next_row < N and 0 <= next_col < N and L <= abs(nation[not_visit_row][not_visit_col] - nation[next_row][next_col]) <= R:
                            need_explore = True
                if need_explore:
                    que = deque([[not_visit_row, not_visit_col]])
                    union = []
                    union_sum = 0
                    union_cnt = 0
                    while que:
                        now_row, now_col = que.popleft()
                        now_population = nation[now_row][now_col]
                        union_sum += now_population
                        union_cnt += 1
                        for dir in dirs:
                            next_row = now_row + dir[0]
                            next_col = now_col + dir[1]
                            if 0 <= next_row < N and 0 <= next_col < N:
                                next_popluation = nation[next_row][next_col]
                                if not visited[next_row][next_col] and L <= abs(now_population - next_popluation) <= R:
                                    # print("Next :", [next_row, next_col])
                                    que.append([next_row, next_col])
                                    union.append([next_row, next_col])
                                    visited[next_row][next_col] = 1
                    if union:
                        union.append([not_visit_row, not_visit_col])
                        for (nation_row, nation_col) in union:
                            nation[nation_row][nation_col] = union_sum // union_cnt
                        union_count += 1
    # print("Village!!!!!")
    # for n in nation:
    #     print(*n)
    if union_count == 0:
        break
    day += 1
print(day)