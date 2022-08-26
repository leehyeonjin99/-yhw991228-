import sys

N, K = map(int, sys.stdin.readline().split())
# f = open("/Users/hyounjinlee/development/Algorithm-study/beakjoon/삼성 SW 역량 테스트 기출 문제/log.txt", mode = "wt")

# 0: 흰색
# 1: 빨간색
# 2; 파란색
chass = []
for _ in range(N):
    chass.append(list(map(int, sys.stdin.readline().split())))

dirs = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
horses = {idx: [] for idx in range(K)}
horses_on_chass = [[[] for _ in range(N)] for _ in range(N)]
for idx in range(K):
    row, col, dir = map(int, sys.stdin.readline().split())
    row, col = row - 1, col - 1
    horses[idx] = [row, col, dirs[dir]]
    horses_on_chass[row][col].append(idx)

# 말이 4개 이상 쌓이는 순간 종료
# 1000 초과시 종료
time = 0
while True:
    # f.write("="*10+f"TIME {time}\n")
    idx = 0
    moving_cnt = K
    not_move = False
    four_horses = False
    while True:
        # f.write(f"HORSE  {idx}\n")
        if idx >= K:
            break
        if four_horses:
            break
        horse = horses[idx]
        horse_row, horse_col, horse_dir = horse
        now_loc_horses = horses_on_chass[horse_row][horse_col]
        horse_index = now_loc_horses.index(idx)
        upper_horses = now_loc_horses[horse_index:]
        # f.write(f"MOVIGN WITH {upper_horses} IN {now_loc_horses}\n")
        next_row, next_col = horse_row + horse_dir[0], horse_col + horse_dir[1]
        if not (0 <= next_row < N and 0 <= next_col < N) or chass[next_row][next_col] == 2:
            if not_move:
                not_move = False
                moving_cnt -= 1
                # f.write("CAN'T GO\n")
            else:
                not_move = True
                horse_dir = [-horse_dir[0], -horse_dir[1]]
                horses[idx][-1] = horse_dir
                # f.write("TURN BACK {horses[idx][-1]}}\n")
                idx -= 1
        elif chass[next_row][next_col] == 0:
            not_move = False
            horses_on_chass[horse_row][horse_col] = now_loc_horses[:horse_index]
            horses_on_chass[next_row][next_col] += now_loc_horses[horse_index:]
            if len(horses_on_chass[next_row][next_col]) >= 4:
                four_horses = True
            for upper_horse in upper_horses:
                horses[upper_horse][0] = next_row
                horses[upper_horse][1] = next_col
            # f.write(f"{horses}\n")
        elif chass[next_row][next_col] == 1:
            not_move = False
            horses_on_chass[horse_row][horse_col] = now_loc_horses[:horse_index]
            horses_on_chass[next_row][next_col] += now_loc_horses[horse_index:][::-1]
            if len(horses_on_chass[next_row][next_col]) >= 4:
                four_horses = True
            for upper_horse in upper_horses:
                horses[upper_horse][0] = next_row
                horses[upper_horse][1] = next_col
            # f.write(f"{horses}\n")
        idx += 1
    # f.write(f"{horses_on_chass}\n")
    
    time += 1
    if moving_cnt == 0:
        time -= 1
        # print("NOT MOVING")
        break
    if time > 1000:
        # print("TIME OVER")
        break
    if four_horses:
        # print("FOUR HORSES")
        break
    
print(time if time < 1000 else -1)