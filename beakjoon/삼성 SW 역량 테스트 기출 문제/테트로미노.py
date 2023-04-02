import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

three_by_two = [[drow, dcol] for drow in range(3) for dcol in range(2)]
two_by_three = [[drow, dcol] for drow in range(2) for dcol in range(3)]

three_by_two_all = list(combinations(three_by_two, 2))
three_by_two_remove = set([((1, 0), (1, 1))])
for (r1, c1), (r2, c2) in three_by_two_all:
    if abs(r1 - r2) == abs(c1 - c2):
        three_by_two_remove.add(((r1, c1), (r2, c2)))

two_by_three_all = list(combinations(two_by_three, 2))
two_by_three_remove = set([((0, 1), (1, 1))])
for (r1, c1), (r2, c2) in two_by_three_all:
    if abs(r1 - r2) == abs(c1 - c2):
        two_by_three_remove.add(((r1, c1), (r2, c2)))

answer = 0
for row in range(N):
    for col in range(M):
        if row + 3 < N:
            answer = max(answer, sum(board[row + drow][col] for drow in range(4)))
        if col + 3 < M:
            answer = max(answer, sum(board[row][col: col + 4]))

        if not (row + 2 < N and col + 1 < M):
            continue
        S = sum([board[row + drow][col + dcol] for (drow, dcol) in three_by_two])
        for (r1, c1), (r2, c2) in three_by_two_all:
            if ((r1, c1), (r2, c2)) in three_by_two_remove:
                continue
            answer = max(answer, S - board[row + r1][col + c1] - board[row + r2][col + c2])
        
        if not (row + 1 < N and col + 2 < M):
            continue
        S = sum([board[row + drow][col + dcol] for (drow, dcol) in two_by_three])
        for (r1, c1), (r2, c2) in two_by_three_all:
            if ((r1, c1), (r2, c2)) in two_by_three_remove:
                continue
            answer = max(answer, S - board[row + r1][col + c1] - board[row + r2][col + c2])

print(answer)