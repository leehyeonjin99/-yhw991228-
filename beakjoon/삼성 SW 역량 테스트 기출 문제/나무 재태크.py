import sys
input = sys.stdin.readline
N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
yangbun = [[5 for _ in range(N)] for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
trees_loc = set([])
for _ in range(M):
    x, y, z = map(int, input().split())
    x, y = x - 1, y - 1
    trees_loc.add((x, y))
    trees[x][y].append(z)

for year in range(K):
    # 봄, 여름
    for (row, col) in trees_loc:
        die_idx = -1
        die_sum = 0
        all_die = set([])
        trees[row][col].sort()
        for idx, tree_age in enumerate(trees[row][col]):
            if tree_age <= yangbun[row][col]:
                yangbun[row][col] -= tree_age
                trees[row][col][idx] += 1
            else:
                die_idx = idx if die_idx < 0 else die_idx
                die_sum += tree_age // 2
        yangbun[row][col] += die_sum
        if die_idx != -1:
            trees[row][col] = trees[row][col][:die_idx]
        if die_idx == 0:
            all_die.add((row, col))
    trees_loc -= all_die

    # 가을
    add_trees_loc = set([])
    for (row, col) in trees_loc:
        for tree_age in trees[row][col]:
            if tree_age % 5 != 0:
                continue
            for (drow, dcol) in [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]:
                next_row, next_col = row + drow, col + dcol
                if 0 <= next_row < N and 0 <= next_col < N:
                    add_trees_loc.add((next_row, next_col))
                    trees[next_row][next_col].append(1)
    trees_loc |= add_trees_loc

    # 겨울
    for row in range(N):
        for col in range(N):
            yangbun[row][col] += A[row][col]

answer = 0
for (row, col) in trees_loc:
    answer += len(trees[row][col])
print(answer)