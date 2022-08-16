import sys
R, C, T = map(int, sys.stdin.readline().split())
A = []
cleaner = []
sum_dust = 0
for row in range(R):
    line = list(map(int, sys.stdin.readline().split()))
    A.append(line)
    for col in range(C):
        if line[col] == -1:
            cleaner.append([row, col])
        else:
            sum_dust += line[col]

dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for time in range(T):
    add_dust = [[0 for _ in range(C)] for _ in range(R)]

    # caculate revised dust
    for row in range(R):
        for col in range(C):
            if A[row][col] >= 5:
                share_cnt = 0
                for dir in dirs:
                    next_row = row + dir[0]
                    next_col = col + dir[1]
                    if 0<=next_row<R and 0<=next_col<C and A[next_row][next_col] != -1:
                        share_cnt += 1
                        add_dust[next_row][next_col] += A[row][col] // 5
                add_dust[row][col] -= A[row][col] // 5 * share_cnt
    
    # update A
    # print("="*15, "Update")
    for row in range(R):
        for col in range(C):
            A[row][col] += add_dust[row][col]
        # print(*A[row])

    # top air cleaner winds
    top_dirs = [[0, 1], [-1, 0], [0, -1], [1, 0]]
    top_dir = 0
    next_row, next_col = cleaner[0]
    before_dust = 0
    while True:
        next_row += top_dirs[top_dir][0]
        next_col += top_dirs[top_dir][1]
        if next_row == cleaner[0][0] and next_col == cleaner[0][1]:
            sum_dust -= before_dust
            break
        if not (0 <= next_row < R and 0 <= next_col < C):
            next_row, next_col = next_row - top_dirs[top_dir][0], next_col - top_dirs[top_dir][1]
            top_dir += 1
            continue
        A[next_row][next_col], before_dust = before_dust, A[next_row][next_col]

    # down air cleaner winds
    down_dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    down_dir = 0
    next_row, next_col = cleaner[1]
    before_dust = 0
    while True:
        next_row += down_dirs[down_dir][0]
        next_col += down_dirs[down_dir][1]
        if next_row == cleaner[1][0] and next_col == cleaner[1][1]:
            sum_dust -= before_dust
            break
        if not (0 <= next_row < R and 0 <= next_col < C):
            next_row, next_col = next_row - down_dirs[down_dir][0], next_col - down_dirs[down_dir][1]
            down_dir += 1
            continue
        A[next_row][next_col], before_dust = before_dust, A[next_row][next_col]

    # wind A
    # print("="*15, "Wind")
    # for row in range(R):
    #     print(*A[row])

print(sum_dust)