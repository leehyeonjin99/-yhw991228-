import sys
input = sys.stdin.readline
circles = []
for _ in range(4):
    circles.append(list(map(int, list(input())[:-1])))
K = int(input())
rots = []
for _ in range(K):
    rots.append(list(map(int, input().split()))) # 1 : 시계 / -1 : 반시계

def rot(c_num, dir):
    if dir == 1:
        circles[c_num] = [circles[c_num][-1]] + circles[c_num][:-1]
    else:
        circles[c_num] = circles[c_num][1:] + [circles[c_num][0]]

answer = 0
for (c_num, dir) in rots:
    c_num -= 1
    compare = []
    for idx in range(3):
        compare.append(circles[idx][2] == circles[idx + 1][6])
    rot(c_num, dir)
    right_dir = dir
    for right in range(c_num + 1, 4):
        if not compare[right - 1]:
            right_dir = -right_dir
            rot(right, right_dir)
        else:
            break
    left_dir = dir
    for left in range(c_num - 1, -1, -1):
        if not compare[left]:
            left_dir = -left_dir
            rot(left, left_dir)
        else:
            break

answer = 0
for idx, nums in enumerate(circles):
    if nums[0] == 1:
        answer += 1 if idx == 0 else (2 if idx == 1 else (4 if idx == 2 else 8))
print(answer)