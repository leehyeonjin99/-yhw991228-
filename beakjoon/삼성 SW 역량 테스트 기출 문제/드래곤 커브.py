import sys

N = int(sys.stdin.readline())
board = [[0 for _ in range(101)] for _ in range(101)]
dirs = {0: [0, 1],
        1: [-1, 0],
        2: [0, -1],
        3: [1, 0]}

def rotation(origin, points):
    rot_points = []
    for point in points[::-1][1:]:
        drow, dcol = point[0] - origin[0],  point[1] - origin[1]
        rot_point_row = origin[0] + dcol
        rot_point_col = origin[1] - drow
        rot_points.append([rot_point_row, rot_point_col])
    return rot_points

for _ in range(N):
    # print("="*20)
    col, row, dir, gen = map(int, sys.stdin.readline().split())
    gen0 = [row + dirs[dir][0], col + dirs[dir][1]]
    points = [[row, col], gen0]
    # print(f"GEN0", points)
    for g in range(gen):
        points = points + rotation(points[-1], points)
        # print(f"GEN{g + 1}", points)
    for point in points:
        board[point[0]][point[1]] = 1

answer = 0
for row in range(100):
    for col in range(100):
        if sum(board[row][col: col+2]) + sum(board[row + 1][col: col+2]) == 4:
            answer += 1

print(answer)