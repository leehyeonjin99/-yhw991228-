import sys
input = sys.stdin.readline
N, K = map(int, input().split())
chess_color = []
for _ in range(N):
    chess_color.append(list(map(int, input().split())))

chess_horse = [[[] for _ in range(N)] for _ in range(N)]
horse_info = {}
for idx in range(K):
    r, c, d = map(int, input().split())
    r, c = r - 1, c - 1
    chess_horse[r][c].append(idx)
    horse_info[idx] = [r, c, 0, d]

dirs = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
def solution():
    day = 0
    while day <= 1000:
        day += 1
        for idx in range(K):
            row, col, height, dir = horse_info[idx]
            next_row, next_col = row + dirs[dir][0], col + dirs[dir][1]
            moving_horse = chess_horse[row][col][height:]
            if not (0 <= next_row < N and 0 <= next_col < N) or chess_color[next_row][next_col] == 2:
                dir = dir + 1 if dir % 2 == 1 else dir - 1
                horse_info[idx][-1] = dir
                next_row, next_col = row + dirs[dir][0], col + dirs[dir][1]
            if not (0 <= next_row < N and 0 <= next_col < N) or chess_color[next_row][next_col] == 2:
                continue
            if chess_color[next_row][next_col] == 0:
                next_height = len(chess_horse[next_row][next_col])
                chess_horse[row][col] = chess_horse[row][col][:height]
                chess_horse[next_row][next_col] += moving_horse
                if len(chess_horse[next_row][next_col]) >= 4:
                    return day
                for add_height, horse_idx in enumerate(moving_horse):
                    horse_info[horse_idx][:-1] = [next_row, next_col, next_height + add_height]
            elif chess_color[next_row][next_col] == 1:
                next_height = len(chess_horse[next_row][next_col])
                chess_horse[row][col] = chess_horse[row][col][:height]
                chess_horse[next_row][next_col] += moving_horse[::-1]
                if len(chess_horse[next_row][next_col]) >= 4:
                    return day
                for add_height, horse_idx in enumerate(moving_horse[::-1]):
                    horse_info[horse_idx][:-1] = [next_row, next_col, next_height + add_height]
    return -1

print(solution())