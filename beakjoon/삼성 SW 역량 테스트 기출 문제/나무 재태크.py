import sys

N, M, K = map(int, sys.stdin.readline().split())
food = [[5 for _ in range(N)] for _ in range(N)]
winter_add_food = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
trees = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    row, col, age = map(int, sys.stdin.readline().split())
    trees[row - 1][col - 1].append(age)
    trees[row - 1][col - 1].sort()

dirs = [[0, 1], [0, -1], [1, 0], [-1, 0], [-1, -1], [1, 1], [-1, 1], [1, -1]]
answer = M
for year in range(K):
    for row in range(N):
        for col in range(N):
            for idx, tree_age in enumerate(trees[row][col]):
                if food[row][col] < tree_age:
                    # trees[row][col][idx][0] = False
                    answer -= (len(trees[row][col]) - idx)
                    food[row][col] += sum(x // 2 for x in trees[row][col][idx:])
                    trees[row][col] = trees[row][col][:idx]
                    break
                else:
                    trees[row][col][idx] += 1
                    food[row][col] -= tree_age
    for row in range(N):
        for col in range(N):
            for idx, tree_age in enumerate(trees[row][col]):
                if tree_age % 5 == 0:
                    for dir in dirs:
                        next_row = row + dir[0]
                        next_col = col + dir[1]
                        if 0 <= next_row < N and 0 <= next_col < N:
                            trees[next_row][next_col] = [1] + trees[next_row][next_col]
                            answer += 1
            food[row][col] += winter_add_food[row][col]

print(answer)