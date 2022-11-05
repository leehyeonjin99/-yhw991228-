import sys
from collections import deque

# f = open("/Users/hyounjinlee/development/Algorithm-study/beakjoon/삼성 SW 역량 테스트 기출 문제/TC.txt", "w")

N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

def moving_left_right(board, dir):
    tmp_board = [tmp.copy() for tmp in board]
    check = [[False for _ in range(N)] for _ in range(N)]
    moving = False
    # print("Direction :", dir)
    col_range = range(0, N, 1) if dir[1] < 0 else range(N-1, -1, -1)
    for row in range(N):
        for col in col_range:
            next_row = row
            next_col = col
            if tmp_board[next_row][next_col] != 0:
                # print(next_row, next_col)
                while 0 <= next_row + dir[0] < N and 0 <= next_col + dir[1] < N and tmp_board[next_row + dir[0]][next_col + dir[1]] == 0:
                    moving = True
                    # print("Going :", [next_row + dir[0], next_col + dir[1]])
                    tmp_board[next_row + dir[0]][next_col + dir[1]] = tmp_board[next_row][next_col]
                    tmp_board[next_row][next_col] = 0
                    next_row += dir[0]
                    next_col += dir[1]
                if 0 <= next_row + dir[0] < N and 0 <= next_col + dir[1] < N and tmp_board[next_row + dir[0]][next_col + dir[1]] == tmp_board[next_row][next_col] and not check[next_row + dir[0]][next_col + dir[1]]:
                    moving = True
                    # print("Updating", [next_row + dir[0], next_col + dir[1]])
                    tmp_board[next_row + dir[0]][next_col + dir[1]] *= 2 
                    check[next_row + dir[0]][next_col + dir[1]] = True
                    tmp_board[next_row][next_col] = 0
                # print("Stepping", tmp_board)
    return tmp_board, moving

def moving_up_down(board, dir):
    tmp_board = [tmp.copy() for tmp in board]
    check = [[False for _ in range(N)] for _ in range(N)]
    moving = False
    row_range = range(0, N, 1) if dir[0] <0 else range(N-1, -1, -1)
    # print("Direction :", dir)
    for col in range(N):
        for row in row_range:
            next_row = row
            next_col = col
            if tmp_board[next_row][next_col] != 0:
                # print(next_row, next_col)
                while 0 <= next_row + dir[0] < N and 0 <= next_col + dir[1] < N and tmp_board[next_row + dir[0]][next_col + dir[1]] == 0:
                    moving = True
                    # print("Going :", [next_row + dir[0], next_col + dir[1]])
                    tmp_board[next_row + dir[0]][next_col + dir[1]] = tmp_board[next_row][next_col]
                    tmp_board[next_row][next_col] = 0
                    next_row += dir[0]
                    next_col += dir[1]
                if 0 <= next_row + dir[0] < N and 0 <= next_col + dir[1] < N and tmp_board[next_row + dir[0]][next_col + dir[1]] == tmp_board[next_row][next_col] and not check[next_row + dir[0]][next_col + dir[1]]:
                    moving = True
                    # print("Updating", [next_row + dir[0], next_col + dir[1]])
                    tmp_board[next_row + dir[0]][next_col + dir[1]] *= 2 
                    check[next_row + dir[0]][next_col + dir[1]] = True
                    tmp_board[next_row][next_col] = 0
                # print("Stepping", tmp_board)
    return tmp_board, moving

def max_board(board):
    M = 0
    for row in board:
        M = max(max(row), M)
    return M

def solution():
    que = deque([])
    que.append([board, 0])
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    M = 0
    
    while que:
        now_board, count = que.popleft()
        if count <= 5:
            M = max(M, max_board(now_board))
        if count == 5:
            continue
        else:
            for dir in direction:
                if dir[0] == 0:
                    next_board, moving_check = moving_left_right(now_board, dir)
                else:
                    next_board, moving_check = moving_up_down(now_board, dir)
                if moving_check:
                    que.append([next_board, count + 1])
                    # f.write(f"========================== {count+1}\n{now_board}\n{next_board}\n")
    
    print(M)

solution()

# tmp = moving_left_right(board, [1,0])[0]
# print(moving_left_right(board, [1,0])[1])
# print("/n")
# for t in tmp:
#     print(*t)