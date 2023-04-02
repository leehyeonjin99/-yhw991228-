# import sys
# from collections import deque

# N = int(sys.stdin.readline())
# schedule = {}
# for day in range(N):
#    T, P = map(int, sys.stdin.readline().split())
#    schedule[day] = [T, P] if day + T <= N else []

# que = deque([[day, schedule[day][1]] for day in range(N) if schedule[day]])
# answer = 0
# while que:
#     day, pay = que.popleft()
#     if pay > answer:
#         answer = pay
#     for next_day in range(day + schedule[day][0], N):
#         if schedule[next_day]:
#             que.append([next_day, pay+schedule[next_day][1]])

# print(answer)

import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
schedule = {idx : [] for idx in range(1, N + 1)}
que = deque([])
for day in range(1, N + 1):
    schedule[day] = list(map(int, input().split()))
    if day + schedule[day][0] <= N + 1:
        que.append([day + schedule[day][0], schedule[day][1]])

answer = 0
while que:
    now_day, now_pay = que.popleft()
    answer = max(answer, now_pay)
    if now_day == N + 1:
        continue
    for next_day in range(now_day, N + 1):
        if next_day + schedule[next_day][0] <= N + 1:
            que.append([next_day + schedule[next_day][0], now_pay + schedule[next_day][1]])

print(answer)
