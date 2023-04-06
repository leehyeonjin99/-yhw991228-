import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split())
circles = []
for _ in range(N):
    circles.append(list(map(int, input().split())))
orders = []

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
def search():
    visited = [[0 for _ in range(M)] for _ in range(N)]
    check = False
    S, cnt = 0, 0
    for row in range(N):
        for col in range(M):
            if circles[row][col] == 0:
                continue
            S += circles[row][col]
            cnt += 1
            if visited[row][col]:
                continue
            visited[row][col] = 1
            que = deque([[row, col, False]])
            while que:
                now_row, now_col, is_set = que.popleft()
                value = circles[now_row][now_col]
                if is_set:
                    circles[now_row][now_col] = 0
                for (drow, dcol) in zip(drows, dcols):
                    next_row, next_col = (now_row + drow), (now_col + dcol) % M
                    if not (0 <= next_row < N):
                        continue
                    if not visited[next_row][next_col] and circles[next_row][next_col] == value:
                        visited[next_row][next_col] = 1
                        que.append([next_row, next_col, True])
            if is_set:
                circles[row][col] = 0
                check = True
    if cnt ==  0:
        return
    if not check:
        mean = S / cnt
        for row in range(N):
            for col in range(M):
                if circles[row][col] == 0:
                    continue
                elif circles[row][col] < mean:
                    circles[row][col] += 1
                elif circles[row][col] > mean:
                    circles[row][col] -= 1

for _ in range(T):
    x, d, k = map(int, input().split())
    for row in range(N):
        if (row + 1) % x != 0:
            continue
        if d == 0:
            circles[row] = circles[row][-k:] + circles[row][:-k]
        else:
            circles[row] = circles[row][k:] + circles[row][:k]
    search()

print(sum(sum(tmp) for tmp in circles))