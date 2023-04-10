import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
def block_group():
    max_group = []
    max_size = 1
    max_rainbow = 0
    visited = [[0 for _ in range(N)] for _ in range(N)]
    for row in range(N):
        for col in range(N):
            if board[row][col] <= 0 or visited[row][col]:
                continue
            size = 1
            rainbow = 0
            group = [[row, col]]
            tmp_visited = [[0 for _ in range(N)] for _ in range(N)]
            que = deque([[row, col]])
            tmp_visited[row][col] = 1
            visited[row][col] = 1
            while que:
                now_row, now_col = que.popleft()
                for (drow, dcol) in zip(drows, dcols):
                    next_row, next_col = now_row + drow, now_col + dcol
                    if 0 <= next_row < N and 0 <= next_col < N and not tmp_visited[next_row][next_col] and (board[next_row][next_col] == board[row][col] or board[next_row][next_col] == 0):
                        tmp_visited[next_row][next_col] = 1
                        visited[next_row][next_col] = 1
                        group.append([next_row, next_col])
                        size += 1
                        if board[next_row][next_col] == 0:
                            rainbow += 1
                        que.append([next_row, next_col])
            if max_size < size or (max_size == size and (max_rainbow < rainbow or (max_rainbow == rainbow and max_group and (max_group[0][0] < row or (max_group[0][0] == row and max_group[0][1] < col))))):
                max_size = size
                max_group = group
                max_rainbow = rainbow
    return max_group, max_size

def downing():
    for col in range(N):
        for row in range(N - 2, -1, -1):
            v = board[row][col]
            if v == -1:
                continue
            check = False
            for next_row in range(row, N - 1):
                if board[next_row + 1][col] != -2:
                    check = True
                    break
            board[row][col] = -2
            board[next_row if check else next_row + 1][col] = v

def rotation():
    return [list(tmp) for tmp in zip(*board)][::-1]

def solution():
    global board
    answer = 0
    step = 0
    while True:
        max_group, max_size = block_group()
        if not max_group:
            return answer
        for (row, col) in max_group:
            board[row][col] = -2
        answer += max_size ** 2
        downing()
        board = rotation()
        downing()
        step += 1

print(solution())

