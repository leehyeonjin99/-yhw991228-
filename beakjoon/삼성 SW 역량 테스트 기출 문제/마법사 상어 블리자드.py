import sys
from heapq import heappush, heappop
from itertools import product
T = int(input())

def push_solution(target_num):
    can_str = [str(num) for num in can_input]
    can_nums = set([])
    for idx in range(1, 4):
        can_nums |= set(map(lambda x : int(''.join(x)), product(can_str, repeat=idx)))
    heap = []
    for num in can_nums:
        heappush(heap, [len(str(num)), int(num)])
    while heap:
        now_push, now_num = heappop(heap)
        if now_num == target_num and now_push <= M:
            return now_push + 1
        if now_push >= M:
            return -1
        if now_num > 999:
            continue
        for next_num in can_nums:
            for oper in can_operate:
                if oper == 1:
                    heappush(heap, [now_push + len(str(next_num)) + 1, now_num + next_num])
                elif oper == 2:
                    heappush(heap, [now_push + len(str(next_num)) + 1, now_num - next_num])
                elif oper == 3:
                    heappush(heap, [now_push + len(str(next_num)) + 1, now_num * next_num])
                elif oper == 4 and next_num != 0:
                    heappush(heap, [now_push + len(str(next_num)) + 1, now_num // next_num])

def solution():
    # 각각 터치
    answer = 0
    each_touch = True
    for num in list(map(int, list(target_num))):
        if num in can_input:
            answer += 1
        else:
            each_touch = False
            break
    if each_touch:
        return answer
    # 한번에 터치
    one_touch = push_solution(int(target_num))
    return one_touch
        

for test_case in range(1, T + 1):
    N, O, M = map(int, input().split())
    can_input = set(map(int, input().split()))
    can_operate = set(map(int, input().split()))
    target_num = input()
    print(f"#{test_case} {solution()}")