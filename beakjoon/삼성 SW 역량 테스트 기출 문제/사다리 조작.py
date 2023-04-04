import sys
from collections import deque
input = sys.stdin.readline
N, M, H = map(int, input().split())
# f = open("check.txt", 'w')
ladder = [[0 for _ in range(N)] for _ in range(H)]
for _ in range(M):
    h, n = map(int, input().split())
    ladder[h - 1][n - 1] = 1

def check():
    for i in range(N):
        r, c = 0, i
        while r < H:
            if ladder[r][c - 1] == 1:
                c -= 1
            elif ladder[r][c] == 1:
                c += 1
            r += 1
        if c != i:
            return False
    return True

answer = 4

def dfs(now_cnt, now_h, now_c):
    global answer
    # f.write(f"==============={now_cnt}==================\n")
    # for tmp in now_ladder:
    #     f.write(f'{tmp}\n')
    if now_cnt > answer:
        return
    if check():
        answer = min(answer, now_cnt)
        return
    if now_cnt == 3:
        return
    for h in range(now_h, H):
        start_c = now_c if h == now_h else 0
        for c in range(start_c, N - 1):
            if ladder[h][c] == 0 and (c == 0 or ladder[h][c - 1] == 0):
                ladder[h][c] = 1
                dfs(now_cnt + 1, h, c + 2)
                ladder[h][c] = 0

dfs(0, 0, 0)
print(answer if answer < 4 else -1)