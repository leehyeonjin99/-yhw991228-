import sys
from collections import deque

N = int(sys.stdin.readline())
schedule = {}
for day in range(N):
   T, P = map(int, sys.stdin.readline().split())
   schedule[day] = [T, P] if day + T <= N else []

que = deque([[day, schedule[day][1]] for day in range(N) if schedule[day]])
answer = 0
while que:
    day, pay = que.popleft()
    if pay > answer:
        answer = pay
    for next_day in range(day + schedule[day][0], N):
        if schedule[next_day]:
            que.append([next_day, pay+schedule[next_day][1]])

print(answer)