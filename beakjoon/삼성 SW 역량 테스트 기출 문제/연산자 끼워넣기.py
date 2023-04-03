import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
operations = list(map(int, input().split()))

max_ans = -1000000000
min_ans = 1000000000
que = deque([[nums[0], 1, operations]])
while que:
    now_ans, now_idx, now_oper = que.popleft()
    if now_idx == N:
        max_ans = max(max_ans, now_ans)
        min_ans = min(min_ans, now_ans)
        continue
    for oper_idx, oper_cnt in enumerate(now_oper):
        if oper_cnt == 0:
            continue
        next_oper = now_oper.copy()
        next_oper[oper_idx] -= 1
        if oper_idx == 0:
            next_ans = now_ans + nums[now_idx]
        elif oper_idx == 1:
            next_ans = now_ans - nums[now_idx]
        elif oper_idx == 2:
            next_ans = now_ans * nums[now_idx]
        else:
            if now_ans >= 0:
                next_ans = now_ans // nums[now_idx]
            else:
                next_ans = -((-now_ans) // nums[now_idx])
        que.append([next_ans, now_idx + 1, next_oper])

print(max_ans)
print(min_ans)