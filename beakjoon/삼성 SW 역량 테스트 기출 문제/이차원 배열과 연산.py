import sys
from collections import Counter

r, c, k = map(int, sys.stdin.readline().split())
r, c = r-1, c-1
board = []
for _ in range(3):
    board.append(list(map(int, sys.stdin.readline().split())))

def count_sort():
    max_row_size = 0
    for row in range(len(board)):
        num_count = dict(Counter(board[row])).items()
        num_count = sorted(num_count, key = lambda item: (item[1], item[0]))
        row_tmp = [item for items in num_count if items[0] for item in items]
        max_row_size = max(max_row_size, len(row_tmp))
        board[row] = row_tmp
    for row in range(len(board)):
        if len(board[row]) < max_row_size:
            for _ in range(max_row_size - len(board[row])):
                board[row].append(0)

want = False
for time in range(100):
    if r < len(board) and c < len(board[0]) and board[r][c] == k:
        want = True
        break
    # 행의 크기가 더 큰 경우 => 행 연산 실행
    if len(board[0]) <= len(board):
        count_sort()
    else:
        board = list(zip(*board))
        count_sort()
        for _ in range(3):
            board = list(zip(*board))

if want:
    print(time)
else:
    if r < len(board) and c < len(board[0]) and board[r][c] == k:
        print(100)
    else:
        print(-1)