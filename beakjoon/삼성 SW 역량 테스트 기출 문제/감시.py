from collections import deque
import sys

N, M = map(int, sys.stdin.readline().split())
cctv_circle = [[0 for _ in range(M)] for _ in range(N)]
office = []
cctv = []

for row in range(N):
    new_row = list(map(int, sys.stdin.readline().split()))
    office.append(new_row)
    for col in range(M):
        if new_row[col] not in [0, 6]:
            cctv.append([row, col, office[row][col]])
        if new_row[col] > 0:
            cctv_circle[row][col] = 1

dir = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def cctv_check(cctv_circle, cctv_row, cctv_col, direction):
    cctv_circle_tmp = [row.copy() for row in cctv_circle]
    cctv_row, cctv_col = cctv_row + direction[0], cctv_col + direction[1]
    while 0 <= cctv_row < N and 0 <= cctv_col < M and office[cctv_row][cctv_col] != 6:
        cctv_circle_tmp[cctv_row][cctv_col] = 1
        cctv_row, cctv_col = cctv_row + direction[0], cctv_col + direction[1]
    return cctv_circle_tmp

def cctv_circle_num(cctv_circle):
    count = 0
    for row in range(N):
        for col in range(M):
            if cctv_circle[row][col] == 0:
                count += 1
    return count

def que_append_check(next_cctv_circle, use_cctv):
    global answer
    if use_cctv < len(cctv):
        que.append([next_cctv_circle, cctv[use_cctv], use_cctv])
    else:
        answer = min(answer, cctv_circle_num(next_cctv_circle))

def show_circle(cctv_circle):
    print("="*10)
    for cctv_cir in cctv_circle:
        print(*cctv_cir)

if len(cctv) == 0:
    print(cctv_circle_num(cctv_circle))
else:
    que = deque([])
    que.append([cctv_circle, cctv[0], 0])
    answer = 64

    while que:
        now_cctv_circle, (cctv_loc_row, cctv_loc_col, cctv_num), use_cctv = que.popleft()
        use_cctv += 1
        if cctv_num == 1:
            for now_dir in dir:
                next_cctv_circle = cctv_check(now_cctv_circle, cctv_loc_row, cctv_loc_col, now_dir)
                que_append_check(next_cctv_circle, use_cctv)
                # show_circle(next_cctv_circle)
        elif cctv_num == 2:
            for idx in range(2):
                next_cctv_circle = cctv_check(now_cctv_circle, cctv_loc_row, cctv_loc_col, dir[idx])
                next_cctv_circle = cctv_check(next_cctv_circle, cctv_loc_row, cctv_loc_col, dir[idx+2])
                que_append_check(next_cctv_circle, use_cctv)
                # show_circle(next_cctv_circle)
        elif cctv_num == 3:
            for idx in range(4):
                first_dir = dir[idx]
                second_dir = dir[idx + 1 if idx < 3 else 0]
                next_cctv_circle = [row.copy() for row in now_cctv_circle]
                for now_dir in [first_dir, second_dir]:
                    next_cctv_circle = cctv_check(next_cctv_circle, cctv_loc_row, cctv_loc_col, now_dir)
                que_append_check(next_cctv_circle, use_cctv)
                # show_circle(next_cctv_circle)
        elif cctv_num == 4:
            for not_dir in dir:
                now_dirs = [d for d in dir if d!=not_dir]
                next_cctv_circle = [row.copy() for row in now_cctv_circle]
                for now_dir in now_dirs:
                    next_cctv_circle = cctv_check(next_cctv_circle, cctv_loc_row, cctv_loc_col, now_dir)
                que_append_check(next_cctv_circle, use_cctv)
                # show_circle(next_cctv_circle)
        elif cctv_num == 5:
            next_cctv_circle = [row.copy() for row in now_cctv_circle]
            for now_dir in dir:
                next_cctv_circle = cctv_check(next_cctv_circle, cctv_loc_row, cctv_loc_col, now_dir)
            que_append_check(next_cctv_circle, use_cctv)
            # show_circle(next_cctv_circle)

    print(answer)


