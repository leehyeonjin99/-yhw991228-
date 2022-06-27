import sys
from collections import deque

def raining(M, R, C):
    next_map = [row.copy() for row in M]
    drow = [1, -1, 0, 0]
    dcol = [0, 0, 1, -1]
    next_rain = []
    for r in range(R):
        for c in range(C):
            if M[r][c] == '*':
                for i in range(4):
                    next_row = r + drow[i]
                    next_col = c + dcol[i]
                    if 0<=next_row<R and 0<=next_col<C and M[next_row][next_col] == '.':
                        next_rain.append([next_row, next_col])
    for next_row, next_col in next_rain:
        next_map[next_row][next_col] = '*'
    return next_map

R, C = map(int, sys.stdin.readline().split())
M = [list(input()) for _ in range(R)]

for row in range(R):
    if 'W' in M[row]:
        start = [row, M[row].index('W')]
    if 'H' in M[row]:
        end = [row, M[row].index('H')]

dist = [[R*C+1 for _ in range(C)] for _ in range(R)]

que = deque()
que.append([start, raining(M, R, C)])
dist[start[0]][start[1]] = 0

drow = [1, -1, 0, 0]
dcol = [0, 0, 1, -1]
check = False
while que:
    (now_row, now_col), now_map = que.popleft()
    # print("="*5, now_row, now_col)
    # print(dist)
    # for n in now_map:
    #     print(*n)
    if now_row == end[0] and now_col == end[1]:
        print(dist[now_row][now_col])
        check = True
        break
    next_map = raining(now_map, R, C)
    for i in range(4):
        next_row = now_row + drow[i]
        next_col = now_col + dcol[i]
        if 0<=next_row<R and 0<=next_col<C and (now_map[next_row][next_col] in ['.', 'H']) and dist[next_row][next_col] > dist[now_row][now_col] + 1:
            # print("Append:",next_row, next_col)
            que.append([[next_row, next_col], next_map])
            dist[next_row][next_col] = dist[now_row][now_col] + 1

if not check:
    print("FAIL")