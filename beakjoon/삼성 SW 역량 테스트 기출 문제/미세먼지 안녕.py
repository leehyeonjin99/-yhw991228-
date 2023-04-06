import sys
input = sys.stdin.readline
R, C, T = map(int, input().split())
room = []
cleaner = []
duty = set([])
total_duty = 0
for row in range(R):
    tmp = list(map(int, input().split()))
    room.append(tmp)
    for col, value in enumerate(tmp):
        if value == -1:
            cleaner.append([row, col])
        elif value > 0:
            total_duty += value
            duty.add((row, col))

((up_row, up_col), (down_row, down_col)) = cleaner
drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]

def edit_duty_loc(row, col, now_duty):
    if now_duty > 0:
        duty.add((row, col))
    elif now_duty == 0 and room[row][col] > 0:
        duty.remove((row, col))

def spread():
    global duty
    add_duty = set([])
    add_cnt = [[0 for _ in range(C)] for _ in range(R)]
    for (row ,col) in duty:
        remove_duty = 0
        for (drow, dcol) in zip(drows, dcols):
            next_row, next_col = row + drow, col + dcol
            if 0 <= next_row < R and 0 <= next_col < C and room[next_row][next_col] != -1:
                add_duty.add((next_row, next_col))
                add_cnt[next_row][next_col] += room[row][col] // 5
                remove_duty += room[row][col] // 5
        room[row][col] -= remove_duty
    
    duty |= add_duty
    for (row, col) in add_duty:
        room[row][col] += add_cnt[row][col]

def moving():
    global total_duty
    # 청소기 윗 바람
    now_duty = 0
    for col in range(1, C):
        edit_duty_loc(up_row, col, now_duty)
        room[up_row][col], now_duty = now_duty, room[up_row][col]
    
    for row in range(up_row - 1, -1, -1):
        edit_duty_loc(row, C - 1, now_duty)
        room[row][C - 1], now_duty = now_duty, room[row][C - 1]
    
    for col in range(C - 2, -1, -1):
        edit_duty_loc(0, col, now_duty)
        room[0][col], now_duty = now_duty, room[0][col]
    
    for row in range(1, up_row):
        edit_duty_loc(row, 0, now_duty)
        room[row][0], now_duty = now_duty, room[row][0]
    
    total_duty -= now_duty

    # 청소기 아랫 바람
    now_duty = 0
    for col in range(1, C):
        edit_duty_loc(down_row, col, now_duty)
        room[down_row][col], now_duty = now_duty, room[down_row][col]
    
    for row in range(down_row + 1, R):
        edit_duty_loc(row, C - 1, now_duty)
        room[row][C - 1], now_duty = now_duty, room[row][C - 1]
    
    for col in range(C - 2, -1, -1):
        edit_duty_loc(R - 1, col, now_duty)
        room[R - 1][col], now_duty = now_duty, room[R - 1][col]
    
    for row in range(R - 2, down_row, -1):
        edit_duty_loc(row, 0, now_duty)
        room[row][0], now_duty = now_duty, room[row][0]
    
    total_duty -= now_duty

for t in range(T):
   spread()
   moving()

print(total_duty)