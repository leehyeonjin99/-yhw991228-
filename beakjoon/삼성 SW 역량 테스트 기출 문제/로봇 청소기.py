import sys
input = sys.stdin.readline

N, M = map(int, input().split())
now_r, now_c, now_d = map(int, input().split())
dirs = {0: [-1, 0], 1: [0, 1], 2: [1, 0], 3: [0, -1]}
room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

answer = 0
while True:
    if room[now_r][now_c] == 0:
        room[now_r][now_c] = -1
        answer += 1
    check = False
    for cnt in range(4):
        now_d = (now_d - 1) % 4
        next_r = now_r + dirs[now_d][0]
        next_c = now_c + dirs[now_d][1]
        if room[next_r][next_c] == 0:
            now_r, now_c = next_r, next_c
            check = True
            break
    if not check:
        next_r = now_r - dirs[now_d][0]
        next_c = now_c - dirs[now_d][1]
        if not (0 <= next_r < N and 0 <= next_c < M) or room[next_r][next_c] == 1:
            break
        now_r, now_c = next_r, next_c

print(answer)