import sys
from copy import deepcopy
N, K = map(int, sys.stdin.readline().split())
belt = {loc : [0, False] for loc in range(1, 2 * N + 1)}
durability = list(map(int, sys.stdin.readline().split()))
for idx, dur in enumerate(durability):
    belt[idx + 1][0] = dur

def check_quit():
    if belt[N][1]:
        belt[N][1] = False 

def check_durability_zero():
    zero_cnt = 0
    for loc in range(1, 2 * N + 1):
        if belt[loc][0] <= 0:
            zero_cnt += 1
    if zero_cnt >= K:
        return True
    return False

def step():
    step_cnt = 1
    while True:
        # step 1. 컨베이어 벨트를 로봇과 함께 이동
        last_info = belt[1]
        for loc in range(2, 2 * N + 1):
            last_info, belt[loc] = belt[loc], last_info
        belt[1] = last_info
        check_quit()

        # step2. 만약 다음 벨트의 내구력이 1 이상이고 로봇이 올려져 있지 않다면 이전 벨트의 로봇을 이동시킨다. 순서는 가장 먼저 올라간 로봇부터
        for loc in range(2 * N, 0, -1):
            if belt[loc][1]:
                if loc + 1 < 2 * N + 1 and not belt[loc + 1][1] and belt[loc + 1][0]:
                    belt[loc + 1][0] -= 1
                    belt[loc + 1][1] = True
                    belt[loc][1] = False
                elif loc + 1 == 2 * N + 1 and belt[1][0] and not belt[1][1]:
                    belt[1][0] -= 1
                    belt[1][1] = True
                    belt[loc][1] = False
        check_quit()

        # step3. 올리는 위치에 있는 칸의 내구도가 0 이상이면 로봇을 올린다.
        if belt[1][0]:
            belt[1][0] -= 1
            belt[1][1] = True
        
        # step4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다.
        if check_durability_zero():
            print(step_cnt)
            return
        
        step_cnt += 1

step()