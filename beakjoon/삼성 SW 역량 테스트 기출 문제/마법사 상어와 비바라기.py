import sys

N, M = map(int, sys.stdin.readline().split())
A = []
moving = []
for _ in range(N):
    A.append(list(map(int, sys.stdin.readline().split())))
for _ in range(M):
    moving.append(list(map(int, sys.stdin.readline().split())))

dirs = {1: [0, -1], 2: [-1, -1], 3: [-1, 0], 4: [-1, 1], 5: [0, 1], 6: [1, 1], 7: [1, 0], 8: [1, -1]}
clouds = [(N - 2, 0), (N - 2, 1), (N - 1, 0), (N - 1, 1)]

for d, s in moving:
    (drow, dcol) = dirs[d]
    now_clouds = set([])
    for (row, col) in clouds:
        next_row, next_col = (row + drow * s) % N, (col + dcol * s) % N
        A[next_row][next_col] += 1
        now_clouds.add((next_row, next_col))
    tmp_A = [tmp.copy() for tmp in A]
    for (row, col) in now_clouds:
        for dir_idx in range(2, 9, 2):
            (drow, dcol) = dirs[dir_idx]
            next_row, next_col = row + drow, col + dcol
            if 0 <= next_row < N and 0 <= next_col < N and tmp_A[next_row][next_col] > 0:
                A[row][col] += 1
    clouds = []
    for row in range(N):
        for col in range(N):
            if A[row][col] >= 2 and (row, col) not in now_clouds:
                A[row][col] -= 2
                clouds.append((row, col))
print(sum(sum(tmp) for tmp in A))