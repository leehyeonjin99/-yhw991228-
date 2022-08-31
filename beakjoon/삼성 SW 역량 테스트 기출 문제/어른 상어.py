import sys

# f = open("/Users/hyounjinlee/development/Algorithm-study/beakjoon/삼성 SW 역량 테스트 기출 문제/log.txt", mode = 'wt')

N, M, k = map(int, sys.stdin.readline().split())
dirs = {1: [-1, 0], 2: [1, 0], 3: [0, -1], 4: [0, 1]}
# idx : [[now_row, now_col], now_dir, {dir_idx : 우선순위 for dir_idx in range(1, 5)}]
sharks = {idx : [] for idx in range(1, M + 1)}
# field[row][col] = [now_shark_idx, [scent_idx, scent_remain_time]]
field = [[[0, [0, 0]] for _ in range(N)] for _ in range(N)]
for row in range(N):
    tmp = list(map(int, sys.stdin.readline().split()))
    for col in range(N):
        if tmp[col]:
            sharks[tmp[col]].append([row, col])
            field[row][col] = [tmp[col], [tmp[col], k]]

sharks_dirs = list(map(int, sys.stdin.readline().split()))
for idx in range(1, M + 1):
    sharks[idx].append(sharks_dirs[idx - 1])

for idx in range(1, M + 1):
    dir_orders = {}
    for dir_idx in range(1, 5):
        order = list(map(int, sys.stdin.readline().split()))
        dir_orders[dir_idx] = order
    sharks[idx].append(dir_orders)

time = 0
while True:
    # f.write(f"===========Time : {time + 1}===========\n")
    # f.write("***Field***\n")
    # for tmp in field:
    #     f.write(f"{tmp}\n")
    # f.write("***Sharks***\n")
    # f.write(f"{sharks.keys()}\n")
    if list(sharks.keys()) == [1]:
        break
    if time > 1000:
        break
    
    # 싱아 이동 및 향기 남기기
    next_locs = {}
    for shark_idx in range(1, M + 1):
        if shark_idx not in sharks:
            continue
        (now_row, now_col), now_dir, dir_order = sharks[shark_idx]
        dir_order = dir_order[now_dir]
        move_check = False
        for dir in dir_order:
            drow, dcol = dirs[dir]
            next_row, next_col = now_row + drow, now_col + dcol
            if 0 <= next_row < N  and 0 <= next_col < N and not field[next_row][next_col][1][0]:
                move_check = True
                break
        if not move_check:
            for dir in dir_order:
                drow, dcol = dirs[dir]
                next_row, next_col = now_row + drow, now_col + dcol
                if 0 <= next_row < N  and 0 <= next_col < N and field[next_row][next_col][1][0] == shark_idx:
                    break
        
        field[now_row][now_col][0] = 0
        sharks[shark_idx][0] = [next_row, next_col]
        sharks[shark_idx][1] = dir
        if (next_row, next_col) not in next_locs:
            next_locs[(next_row, next_col)] = shark_idx
        else:
            if shark_idx < next_locs[(next_row, next_col)]:
                sharks.pop(next_locs[(next_row, next_col)])
                next_locs[(next_row, next_col)] = shark_idx
            else:
                sharks.pop(shark_idx)

    # 모든 칸에 대해서 향기 남은 시간 -= 1
    for row in range(N):
        for col in range(N):
            if field[row][col][1][1] > 0:
                field[row][col][1][1] -= 1
                if field[row][col][1][1] == 0:
                    field[row][col][1][0] = 0
    
    for (row, col), shark_idx in next_locs.items():
        field[row][col][0] = shark_idx
        field[row][col][1] = [shark_idx, k]

    time += 1

print(time if time <= 1000 else -1)