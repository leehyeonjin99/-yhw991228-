import sys
from tabnanny import check

N, L = map(int,sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

def check_way(board):
    count = 0
    for row in range(N):
        check = True
        runway = [0 for _ in range(N)]
        # print(row, end=" ")
        for col in range(N-1):
            now_board = board[row][col]
            next_board = board[row][col + 1]
            if now_board == next_board:
                # print("평지", end=" ")
                continue
            elif next_board - now_board == 1:
                # print("오르막", end=" ")
                if 0 <= col - L + 1 and len(set(board[row][col - L + 1: col + 1])) == 1 and 1 not in runway[col - L + 1: col + 1]:
                    runway[col - L + 1: col + 1] = [1 for _ in range(L)]
                else:
                    check = False
            elif next_board - now_board == -1:
                # print("내리막", end=" ")
                if col + L < N  and len(set(board[row][col + 1: col + L + 1])) == 1 and 1 not in runway[col + 1: col + L + 1]:
                    runway[col + 1: col + L + 1] = [1 for _ in range(L)]
                else:
                    check = False
            else:
                # print("낭떨어지", end=" ")
                check = False
            if not check:
                # print("False")
                break
        if check:
            # print("True")
            count += 1
    # print("="*10)
    return count

turning_board = list(zip(*board))
print(check_way(board) + check_way(turning_board))