import sys
input = sys.stdin.readline
N, L = map(int, input().split())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

def find():
    answer = 0
    for row in range(N):
        last = -1
        check = True
        for col in range(1, N):
            if board[row][col - 1] == board[row][col]:
                continue
            elif board[row][col] - board[row][col - 1] == 1 and col >= L and len(set(board[row][col - L : col])) == 1 and last < col - L:
                last = col - 1
                continue
            elif board[row][col] - board[row][col - 1] == -1 and col + L - 1 < N and len(set(board[row][col: col + L])) == 1 and last < col:
                last = col + L - 1
                continue
            else:
                check = False
                break
        if check:
            answer += 1
    return answer

R = find()
board = [tmp for tmp in zip(*board)]
C = find()
print(R + C)