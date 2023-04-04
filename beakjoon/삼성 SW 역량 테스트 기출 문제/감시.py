import sys
from collections import deque
from copy import deepcopy
input = sys.stdin.readline

N, M = map(int, input().split())
board = []
cctvs = []
cctv_cnt = 0
total_size = 0
for row in range(N):
    tmp = list(map(int, input().split()))
    board.append(tmp)
    for col in range(M):
        if tmp[col] == 0:
            total_size += 1
        elif 1 <= tmp[col] <= 5:
            cctvs.append([tmp[col], [row, col]])
            cctv_cnt += 1
def check(cctv_row, cctv_col, dir_list):
    dirs = {1 : [1, 0], 2: [0, 1], 3: [-1, 0], 4: [0, -1]}
    can_see = set([])
    for dir in dir_list:
        (drow, dcol) = dirs[dir]
        next_row, next_col = cctv_row + drow, cctv_col + dcol
        while 0 <= next_row < N and 0 <= next_col < M:
            if board[next_row][next_col] == 6:
                break
            elif board[next_row][next_col] == 0:
                can_see.add((next_row, next_col))
            next_row += drow
            next_col +=  dcol
    return can_see


answer = N * M
que = deque([[0, set([])]])
while que:
    cctv_idx, can_see = que.popleft()
    # print(cctv_idx, can_see)
    if cctv_idx == cctv_cnt:
        # print("END")
        # print(total_size - len(can_see), can_see)
        answer = min(answer, total_size - len(can_see))
        continue
    cctv_num, (cctv_row, cctv_col) = cctvs[cctv_idx]
    if cctv_num == 1:
        for dirs in [[1], [2], [3], [4]]:
            que.append([cctv_idx + 1, can_see | check(cctv_row, cctv_col, dirs)])
    elif cctv_num == 2:
        for dirs in [[1, 3], [2, 4]]:
            que.append([cctv_idx + 1, can_see | check(cctv_row, cctv_col, dirs)])
    elif cctv_num == 3:
        for dirs in [[1, 2], [2, 3], [3, 4], [4, 1]]:
            que.append([cctv_idx + 1, can_see | check(cctv_row, cctv_col, dirs)])
    elif cctv_num == 4:
        for dirs in [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]:
            que.append([cctv_idx + 1, can_see | check(cctv_row, cctv_col, dirs)])
    elif cctv_num == 5:
        que.append([cctv_idx + 1, can_see | check(cctv_row, cctv_col, [1, 2, 3, 4])])

print(answer)