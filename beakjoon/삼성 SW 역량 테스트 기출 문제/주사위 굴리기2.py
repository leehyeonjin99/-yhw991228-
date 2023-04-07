import sys
from collections import deque
N, M, K = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
scores=  [[0 for _ in range(M)] for _ in range(N)]
for row in range(N):
    for col in range(M):
        if scores[row][col]:
            continue
        scores[row][col] = 1
        que = deque([[row, col]])
        same_num, cnt = [[row, col]], 1
        while que:
            now_row, now_col = que.popleft()
            for (drow, dcol) in dirs:
                next_row, next_col = now_row + drow, now_col + dcol
                if 0 <= next_row < N and 0 <= next_col < M and board[now_row][now_col] == board[next_row][next_col] and not scores[next_row][next_col]:
                    scores[next_row][next_col] =  1
                    cnt += 1
                    same_num.append([next_row, next_col])
                    que.append([next_row, next_col])
        for (r, c) in same_num:
            scores[r][c] = cnt

dir_idx = 0
time = 0
# dice[0] : 위 / dice[5] : 아래
dice = [1, 2, 3, 4, 5, 6]
now_row, now_col = 0, 0
answer = 0
while time < K:
    # 이동
    dr, dc = dirs[dir_idx]
    next_row, next_col = now_row + dr, now_col + dc
    if not (0 <= next_row < N and 0 <= next_col < M):
        dir_idx = dir_idx + 2 if dir_idx < 2 else dir_idx - 2
        dr, dc = dirs[dir_idx]
        next_row, next_col = now_row + dr, now_col + dc
    
    # 주사위 회전
    if dir_idx == 0:
        dice[0], dice[2], dice[3], dice[5] = dice[3], dice[0], dice[5], dice[2]
    elif dir_idx == 1:
        dice[0], dice[1], dice[4], dice[5] = dice[1], dice[5], dice[0], dice[4]
    elif dir_idx == 2:
        dice[0], dice[2], dice[3], dice[5] = dice[2], dice[5], dice[0], dice[3]
    elif dir_idx == 3:
        dice[0], dice[1], dice[4], dice[5] = dice[4], dice[0], dice[5], dice[1]
    
    # 점수 획득
    B = board[next_row][next_col]
    answer += B  * scores[next_row][next_col]

    # 방향 전환
    A = dice[5]
    if A > B:
        dir_idx = (dir_idx + 1) % 4
    elif A < B:
        dir_idx = (dir_idx - 1) % 4
    
    now_row, now_col = next_row, next_col
    time += 1

print(answer) 