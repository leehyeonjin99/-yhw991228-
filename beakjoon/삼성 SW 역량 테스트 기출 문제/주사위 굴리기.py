import sys
input = sys.stdin.readline

N, M, x, y, K = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))
movings = list(map(int, input().split()))
jusawe = {idx : 0 for idx in range(1, 7)}
dirs = {1: [0, 1], 2: [0, -1], 3: [-1, 0], 4: [1, 0]}
jusawe[6] = board[x][y]
board[x][y] = 0

for moving in movings:
    next_x, next_y = x + dirs[moving][0], y + dirs[moving][1]
    if not (0 <= next_x < N and 0 <= next_y < M):
        continue
    x, y = next_x, next_y
    if moving == 1:
        jusawe[1], jusawe[3], jusawe[4], jusawe[6] = jusawe[4], jusawe[1], jusawe[6], jusawe[3]
    elif moving == 2:
        jusawe[1], jusawe[3], jusawe[4], jusawe[6] = jusawe[3], jusawe[6], jusawe[1], jusawe[4]
    elif moving == 3:
        jusawe[1], jusawe[2], jusawe[5], jusawe[6] = jusawe[5], jusawe[1], jusawe[6], jusawe[2]
    else:
        jusawe[1], jusawe[2], jusawe[5], jusawe[6] = jusawe[2], jusawe[6], jusawe[1], jusawe[5]
    if board[x][y] != 0:
        jusawe[6] = board[x][y]
        board[x][y] = 0
    else:
        board[x][y] = jusawe[6]
    print(jusawe[1])