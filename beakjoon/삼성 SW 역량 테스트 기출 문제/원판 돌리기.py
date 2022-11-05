from collections import deque
import sys

N, M, T = map(int, sys.stdin.readline().split())

values = []
for _ in range(N):
    values.append(list(map(int, sys.stdin.readline().split())))

rotations = []
for _ in range(T):
    rotations.append(list(map(int, sys.stdin.readline().split())))

dirs = [[0, -1], [0, 1], [-1, 0], [1, 0]]
for rot_idx, rotation in enumerate(rotations):
    # print("======================================")
    # print(f"ROTATOIN {rot_idx} : {rotation}")
    # 회전
    x, d, k = rotation
    for circle_idx in range(1, N+1):
        if circle_idx % x !=0:
            continue
        circle_idx -= 1
        if d == 0:
            values[circle_idx] = values[circle_idx][-k:] + values[circle_idx][:-k]
        else:
            values[circle_idx] = values[circle_idx][k:] + values[circle_idx][:k]
    # for value in values:
    #     print(f"{value}")
    
    # 같은 값 찾기
    cnt = 1
    group_loc = {}
    visited = [[0 for _ in range(M)] for _ in range(N)]
    values_sum = 0
    values_cnt = 0
    for row in range(N):
        for col in range(M):
            values_sum += values[row][col]
            values_cnt += 1
            # 방문한 적 있는 위치
            if visited[row][col]:
                continue
            # 방문한 적 없지만 값이 지워진 위치
            elif values[row][col] == 0:
                values_cnt -= 1
                continue
            que = deque([[row, col]])
            visited[row][col] = cnt
            group_loc[cnt] = [[row, col]]
            # print(f"Start {[row, col]}")
            while que:
                now_row, now_col = que.popleft()
                now_value = values[now_row][now_col]
                # print("Now Location :", [now_row, now_col])
                for dir in dirs:
                    next_row, next_col = now_row + dir[0], now_col + dir[1]

                    # 인접 위치 값 조정
                    if not 0 <= next_row < N:
                        continue
                    if next_col < 0:
                        next_col = M -1
                    elif next_col >= M:
                        next_col = 0
                    # 같은 값에 대해서 체크
                    if not visited[next_row][next_col] and now_value == values[next_row][next_col]:
                        # print("Next Location :", [next_row, next_col])
                        que.append([next_row, next_col])
                        visited[next_row][next_col] = cnt
                        group_loc[cnt].append([next_row, next_col])
            cnt += 1
    # print("주변 GROUPING")
    # for visit in visited:
    #     print(f"{visit}")

    change_check = False
    for cnt, locs in group_loc.items():
        if len(locs) > 1:
            change_check = True
            for (loc_row, loc_col) in locs:
                values[loc_row][loc_col] = 0
    # print(f"SUM : {values_sum}, CNT : {values_cnt}")
    if not change_check:
        if values_cnt == 0:
            continue
        values_mean = values_sum / values_cnt
        for row in range(N):
            for col in range(M):
                if values[row][col] == 0:
                    continue
                elif values[row][col] < values_mean:
                    values[row][col] += 1
                elif values[row][col] > values_mean:
                    values[row][col] -= 1
    # print("평균 혹은 제거")
    # for value in values:
    #     print(f"{value}")

answer = sum(sum(value) for value in values)
print(answer)