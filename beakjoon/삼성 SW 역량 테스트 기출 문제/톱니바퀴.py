import sys

gear_1 = list(map(int, list(sys.stdin.readline()[:-1])))
gear_2 = list(map(int, list(sys.stdin.readline()[:-1])))
gear_3 = list(map(int, list(sys.stdin.readline()[:-1])))
gear_4 = list(map(int, list(sys.stdin.readline()[:-1])))
gears = {1: gear_1, 2: gear_2, 3: gear_3, 4: gear_4}
rotation_count = int(sys.stdin.readline())
dir = {1: "RIGHT", -1: "LEFT"}

def rotation(gear, dir):
    tmp_gear = gear.copy()
    tmp_gear = [tmp_gear[-1]] + tmp_gear[:-1] if dir == 1 else tmp_gear[1:] + [tmp_gear[0]]
    return tmp_gear

def left_check(left_num):
    # # print(gears[left_num])
    # # print(gears[left_num - 1])
    return gears[left_num][6] == gears[left_num - 1][2] if left_num > 1 else True

def right_check(right_num):
    # # print(gears[right_num])
    # # print(gears[right_num - 1])
    return gears[right_num][2] == gears[right_num + 1][6] if right_num < 4 else True

for _ in range(rotation_count):
    rotation_num, rotation_dir = map(int, sys.stdin.readline().split())
    now_left_check = left_check(rotation_num)
    now_right_check = right_check(rotation_num)
    gears[rotation_num] = rotation(gears[rotation_num], rotation_dir)
    # print(gears[rotation_num])
    left_num = right_num = rotation_num
    left_rotation_dir = right_rotation_dir = rotation_dir
    # print("LEFT CHECK")
    while not now_left_check and left_num > 1:
        left_num -= 1
        left_rotation_dir = -left_rotation_dir
        # print(f"{left_num} TURNING {dir[left_rotation_dir]}")
        now_left_check = left_check(left_num)
        gears[left_num] = rotation(gears[left_num], left_rotation_dir)
        # print(gears[left_num])
        
    # print("RIGHT CHECK")
    while not now_right_check and right_num < 4:
        right_num += 1
        right_rotation_dir = -right_rotation_dir
        now_right_check = right_check(right_num)
        # print(f"{right_num} TURNING {dir[right_rotation_dir]}")
        gears[right_num] = rotation(gears[right_num], right_rotation_dir)
        # print(gears[right_num])

score = 0
for num in range(4):
    gear_top_num = gears[num + 1][0]
    if gear_top_num == 1:
        score += 2**num

print(score)