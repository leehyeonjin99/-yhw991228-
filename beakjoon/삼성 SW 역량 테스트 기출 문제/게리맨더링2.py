import sys
input = sys.stdin.readline
N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

answer = sys.maxsize
for x in range(1, N - 1):
    for y in range(1, N - 1):
        for d1 in range(1, N - 1):
            if x - d1 < 0:
                break
            for d2 in range(1, N - 1):
                if x + d2 >= N or y + d1 + d2 >= N:
                    break
                gu = {idx: 0 for idx in range(1, 6)}
                for c_x in range(N):
                    for c_y in range(N):
                        if x + y <= c_x + c_y <= x + y + 2 * d2 and x - y - 2 * d1 <= c_x - c_y <= x - y:
                            gu[5] += board[c_x][c_y]
                        elif c_x < x and c_y <= y + d1:
                            gu[1] += board[c_x][c_y]
                        elif c_x <= x - d1 + d2 and y + d1 < c_y:
                            gu[2] += board[c_x][c_y]
                        elif x -  d1 + d2 < c_x and y + d2 <= c_y:
                            gu[4] += board[c_x][c_y]
                        else:
                            gu[3] += board[c_x][c_y]
                pops = sorted(list(gu.values()))
                answer = min(answer, pops[-1] - pops[0])

print(answer)