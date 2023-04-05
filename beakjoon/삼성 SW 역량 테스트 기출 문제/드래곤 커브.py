import sys
input = sys.stdin.readline
N = int(input())
board = [[0 for _ in range(101)] for _ in range(101)]
dirs = {0 : [1, 0], 1: [0, -1], 2: [-1, 0], 3: [0, 1]}
for _ in range(N):
    x, y, d, g = map(int, input().split())
    board[x][y] = 1
    (dx, dy) = dirs[d]
    board[x + dx][y + dy] = 1
    dragon_curve = [[x, y], [x + dx, y + dy]]
    for generation in range(g):
        (last_x, last_y) = dragon_curve[-1]
        for (x, y) in dragon_curve[-2::-1]:
            dx, dy = last_x - x, last_y - y
            next_x, next_y = last_x + dy, last_y - dx
            dragon_curve.append([next_x, next_y])
            board[next_x][next_y] = 1

answer = 0
for row in range(100):
    for col in range(100):
        if board[row][col] and board[row + 1][col] and board[row][col + 1] and board[row + 1][col + 1]:
            answer += 1

print(answer)