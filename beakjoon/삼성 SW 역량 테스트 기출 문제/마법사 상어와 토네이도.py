import sys
# 왼쪽으로 바람, dir_idx == 0

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
now_x, now_y = N // 2, N // 2
answer = 0

lengths = []
for idx in range(1, N):
    for _ in range(2 if idx < N - 1 else 3):
        lengths.append(idx)

def check_out(x, y, p):
    global answer, alpha
    moved_sand = int(value * p) if p < 1 else p
    if 0 <= x < N and 0 <= y < N:
        board[x][y] += moved_sand
    else:
        answer += moved_sand
    return moved_sand

dir_idx = 0
for length in lengths:
    for _ in range(length):
        dx, dy = dirs[dir_idx]
        next_x, next_y = now_x + dx, now_y + dy
        value = board[next_x][next_y]
        alpha = value

        # 5%
        tmp_x, tmp_y = next_x + dx * 2, next_y  + dy * 2
        alpha -= check_out(tmp_x, tmp_y, 0.05)

        for i in [1, -1]:
            tmp_dir = (dir_idx + i) % 4
            tmp_dx, tmp_dy = dirs[tmp_dir]
            tmp_x, tmp_y = now_x + tmp_dx, now_y + tmp_dy
            alpha -= check_out(tmp_x, tmp_y, 0.01)
            tmp_x, tmp_y = next_x + 2 * tmp_dx, next_y + 2 * tmp_dy
            alpha -= check_out(tmp_x, tmp_y, 0.02)
            tmp_x, tmp_y = next_x + tmp_dx, next_y + tmp_dy
            alpha -= check_out(tmp_x, tmp_y, 0.07)
            tmp_x, tmp_y = next_x + dx + tmp_dx, next_y + dy + tmp_dy
            alpha -= check_out(tmp_x, tmp_y, 0.1)
        
        tmp_x, tmp_y = next_x + dx, next_y + dy
        alpha = check_out(tmp_x, tmp_y, alpha)

        board[next_x][next_y] = 0
        now_x, now_y = next_x, next_y
    dir_idx = (dir_idx + 1) % 4

print(answer)