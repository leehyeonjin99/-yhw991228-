import sys
input = sys.stdin.readline
N = int(input())
students_info = {}
for _ in range(N * N):
    info = list(map(int, sys.stdin.readline().split()))
    students_info[info[0]] = set(info[1:])

class_info = [[0 for _ in range(N)] for _ in range(N)]
drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]

def choose(std_idx):
    c_row, c_col = 0, 0
    max_frd_cnt = -1
    max_zero_cnt = -1
    for row in range(N):
        for col in range(N):
            if class_info[row][col]:
                continue
            now_zero_cnt = 0
            now_frd_cnt = 0
            for (drow, dcol) in zip(drows, dcols):
                next_row, next_col = row + drow, col + dcol
                if 0 <= next_row < N and 0 <= next_col < N:
                    std = class_info[next_row][next_col]
                    if std == 0:
                        now_zero_cnt += 1
                    elif std in students_info[std_idx]:
                        now_frd_cnt += 1
            if max_frd_cnt < now_frd_cnt or (max_frd_cnt == now_frd_cnt and (max_zero_cnt < now_zero_cnt or (max_zero_cnt == now_zero_cnt and (row < c_row or (c_row == row and col < c_col))))):
                c_row, c_col, max_frd_cnt, max_zero_cnt = row, col, now_frd_cnt, now_zero_cnt
    return c_row, c_col

scores = {0: 0, 1: 1, 2: 10, 3: 100, 4: 1000}
def score():
    S = 0
    for row in range(N):
        for col in range(N):
            std_idx = class_info[row][col]
            s = 0
            for (drow, dcol) in zip(drows, dcols):
                next_row, next_col = row + drow, col + dcol
                if 0 <= next_row < N and 0 <= next_col < N and class_info[next_row][next_col] in students_info[std_idx]:
                    s += 1
            S += scores[s]
    return S

for std_idx in students_info:
    row, col = choose(std_idx)
    class_info[row][col] = std_idx

print(score())