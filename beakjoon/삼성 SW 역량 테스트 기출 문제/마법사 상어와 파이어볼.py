import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _  in range(N)]
ball_locs = set([])
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    r, c = r - 1, c - 1
    board[r][c].append([m, s, d])
    ball_locs.add((r, c))

dirs = {0: [-1, 0], 1: [-1, 1], 2: [0, 1], 3: [1, 1], 4: [1, 0], 5: [1, -1], 6: [0, -1], 7: [-1, -1]}

def moving():
    next_ball_locs = set([])
    next_board = [[[] for _ in range(N)] for _ in range(N)]
    for (row, col) in ball_locs:
        for (m, s, d) in board[row][col]:
            now_row, now_col = row, col
            drow, dcol = dirs[d]
            next_row, next_col = (now_row + drow * s) % N, (now_col + dcol * s) % N
            next_ball_locs.add((next_row, next_col))
            next_board[next_row][next_col].append([m, s, d])
    return next_ball_locs, next_board

def processing():
    for (row, col) in ball_locs:
        ball_cnt = len(board[row][col])
        if ball_cnt <= 1:
            continue
        mass_sum, speed_sum, base_dir = board[row][col][0]
        all_odd_even = True
        for idx in range(1, ball_cnt):
            m, s, d = board[row][col][idx]
            mass_sum += m
            speed_sum += s
            if d % 2 != base_dir % 2:
                all_odd_even = False
        final_mass = mass_sum // 5
        final_speed = speed_sum // ball_cnt
        final_dir = [0, 2, 4, 6] if all_odd_even else [1, 3, 5, 7]
        board[row][col] = []
        if final_mass > 0:
            for dir in final_dir:
                board[row][col].append([final_mass, final_speed, dir])

for _ in range(K):
    ball_locs, board = moving()
    processing()

answer = 0
for row in range(N):
    for col in range(N):
        for (m, s, d) in board[row][col]:
            answer += m

print(answer)