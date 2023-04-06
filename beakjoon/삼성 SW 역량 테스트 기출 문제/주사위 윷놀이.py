import sys
from collections import deque
orders = list(map(int, sys.stdin.readline().split()))

# 1: 출발 / 32: 도착
board = {0: [0, 1]}
for idx in range(1, 20):
    board[idx] = [idx * 2, idx + 1]
board[20] = [40, 32]
board[5].append(21)
board[10].append(27)
board[15].append(24)
board[21] = [13, 22]
board[22] = [16, 23]
board[23] = [19, 29]
board[24] = [28, 25]
board[25] = [27, 26]
board[26] = [26, 29]
board[27] = [22, 28]
board[28] = [24, 29]
board[29] = [25, 30]
board[30] = [30, 31]
board[31] = [35, 20]
board[32] = [0]

answer = 0
que = deque([[0, 0, [0, 0, 0, 0]]])
while que:
    now_idx, now_sum, now_locs = que.popleft()
    answer = max(answer, now_sum)
    if now_idx == 10:
        continue
    go_cnt = orders[now_idx]
    for idx in range(4):
        now_loc = now_locs[idx]
        if now_loc == 32:
            continue
        for cnt in range(go_cnt):
            now_loc = board[now_loc][-1] if cnt == 0 else board[now_loc][1]
            if now_loc == 32:
                break
        if now_loc < 32 and now_loc in now_locs:
            continue
        next_locs = now_locs.copy()
        next_locs[idx] = now_loc
        que.append([now_idx + 1, now_sum + board[now_loc][0], next_locs])

print(answer)