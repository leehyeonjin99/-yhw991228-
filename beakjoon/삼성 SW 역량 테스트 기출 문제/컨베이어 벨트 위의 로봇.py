import sys
input = sys.stdin.readline

N, K = map(int, input().split())
A = list(map(int, input().split()))
belt_info = {idx : [a, False] for idx, a in enumerate(A)}

def unload():
    if belt_info[N - 1][1]:
        belt_info[N - 1][1] = False

def check():
    zero_cnt = 0
    for (weight, _) in belt_info.values():
        zero_cnt += 1 if not weight else 0
        if zero_cnt == K:
            return False
    return True

def rotate():
    W_R = belt_info[0]
    for idx in range(1, 2 * N):
        belt_info[idx], W_R = W_R, belt_info[idx]
    belt_info[0] = W_R
    unload()

def moving_robot():
    for idx in range(N - 2, 0, -1):
        if belt_info[idx][1] and not belt_info[idx + 1][1] and belt_info[idx + 1][0] > 0:
            belt_info[idx][1] = False
            belt_info[idx + 1][0] -= 1
            belt_info[idx + 1][1] = True
    unload()

def load():
    if belt_info[0][0] > 0:
        belt_info[0][0] -= 1
        belt_info[0][1] = True

def solution():
    step = 0
    while check():
        rotate()
        moving_robot()
        load()
        step += 1
    return step

print(solution())