import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
board = []
viruses = []
new_wall = []
for row in range(N):
    R = list(map(int, sys.stdin.readline().split()))
    board.append(R)
    for col in range(M):
        if R[col] == 2:
            viruses.append([row, col])
        elif R[col] == 0:
            new_wall.append([row, col])

def virus_spread(loc):
    direction = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    for dir in direction:
        next_row = loc[0] + dir[0]
        next_col = loc[1] + dir[1]
        # print(next_col, next_row)
        if 0 <= next_row < N and 0 <= next_col < M and new_board[next_row][next_col] == 0:
            new_board[next_row][next_col] = 2
            virus_spread([next_row, next_col])

def calc_safety(board):
    safety_count = 0
    for row in range(N):
        for col in range(M):
            if board[row][col] == 0:
                safety_count += 1
    return safety_count

answer = 0
# f = open("result.txt", 'w')
for new_wall_locs in combinations(new_wall, 3):
    new_board = [b.copy() for b in board]
    for new_wall_loc in new_wall_locs:
        new_board[new_wall_loc[0]][new_wall_loc[1]] = 1
    # f.write("======================Before")
    # for n_b in new_board:
    #     f.write(f"{n_b}\n")
    for virus in viruses:
        virus_spread(virus)
    # f.write("======================After")
    # for n_b in new_board:
    #     f.write(f"{n_b}\n")
    answer = max(answer, calc_safety(new_board))
# f.close()
print(answer)