import sys

N, M = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

direction = {(-1, 0): 0, (0, 1): 1, (1, 0): 2, (0, -1): 3}
left_direction = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}
count = 0
row, col, dir = r, c, d
cleaning = [[False for _ in range(M)] for _ in range(N)]
while True:
    # print("=======Now", dir, [row, col])
    cleaning[row][col] = True
    check = False
    for _ in range(4):
        next_dir = left_direction[dir]
        next_row = row + next_dir[0]
        next_col = col + next_dir[1]
        # print("Next", next_dir, [next_row, next_col], end = " ")
        dir = direction[next_dir]
        if board[next_row][next_col] == 0 and not cleaning[next_row][next_col]:
            check = True
            row, col = next_row, next_col
            # print("치워야함")
            break
        # print("벽이거나 치워져 있음")
    if not check:
        # print([row - next_dir[0], col - next_dir[1]], end=" ")
        if board[row - next_dir[0]][col - next_dir[1]] == 0:
            row = row - next_dir[0]
            col = col - next_dir[1]
            # print("후진")
        else:
            # print("후진 불가능,,,종료")
            break
num = 0     
for clean in cleaning:
    num += sum(clean)
print(num)