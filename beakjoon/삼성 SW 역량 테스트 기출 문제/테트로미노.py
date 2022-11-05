import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))


answer = 0

six_block_1 = [[i, j] for i in range(2) for j in range(3)]
six_block_comb_1 = list(combinations(six_block_1, 2))
six_block_remove_1 = []
for comb in six_block_comb_1:
    comb_1 = comb[0]
    comb_2 = comb[1]
    if abs(comb_1[0] - comb_2[0]) == abs(comb_1[1] - comb_2[1]):
        six_block_remove_1.append(list(comb))
six_block_remove_1.append([[0, 1], [1, 1]])

six_block_2 = [[i, j] for i in range(3) for j in range(2)]
six_block_comb_2 = list(combinations(six_block_2, 2))
six_block_remove_2 = []
for comb in six_block_comb_2:
    comb_1 = comb[0]
    comb_2 = comb[1]
    if abs(comb_1[0] - comb_2[0]) == abs(comb_1[1] - comb_2[1]):
        six_block_remove_2.append(list(comb))
six_block_remove_2.append([[1, 0], [1, 1]])

# f= open("./result.txt", "wt")
for row in range(N):
    for col in range(M):
        # f.write(f"============= Start : {[row, col]}\n")
        if col + 3 < M:
            answer = max(answer, sum(board[row][col: col + 4]))
            # f.write(f"가로{sum(board[row][col: col + 4])} ")
        if row + 3 < N:
            answer = max(answer, board[row][col] + board[row + 1][col] + board[row + 2][col] + board[row + 3][col])
            # f.write(f"세로{board[row][col] + board[row + 1][col] + board[row + 2][col] + board[row + 3][col]} ")
        if col + 2 < M and row + 1 < N:
            S = sum(board[row][col: col + 3]) + sum(board[row + 1][col: col + 3])
            # f.write(f"\n가로 넓이 6 summation : {S}\n")
            for comb in six_block_comb_1:
                if list(comb) not in six_block_remove_1:
                    answer = max(answer, S - (board[row + comb[0][0]][col + comb[0][1]] + board[row + comb[1][0]][col + comb[1][1]]))
                    # f.write(f"{comb} : {S} - {(board[row + comb[0][0]][col + comb[0][1]] + board[row + comb[1][0]][col + comb[1][1]])} = {S - (board[row + comb[0][0]][col + comb[0][1]] + board[row + comb[1][0]][col + comb[1][1]])}\n")
        if col + 1 < M and row + 2 < N:
            S = sum(board[row][col: col + 2]) + sum(board[row + 1][col: col + 2]) + sum(board[row + 2][col: col + 2])
            # f.write(f"세로 넓이 6 summation : {S}\n")
            for comb in six_block_comb_2:
                if list(comb) not in six_block_remove_2:
                    answer = max(answer, S - (board[row + comb[0][0]][col + comb[0][1]] + board[row + comb[1][0]][col + comb[1][1]]))
                    # f.write(f"{comb} : {S} - {(board[row + comb[0][0]][col + comb[0][1]] + board[row + comb[1][0]][col + comb[1][1]])} = {S - (board[row + comb[0][0]][col + comb[0][1]] + board[row + comb[1][0]][col + comb[1][1]])}\n")
        # f.write("\n")
# f.close()
print(answer)