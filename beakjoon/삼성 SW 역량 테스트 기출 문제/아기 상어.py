from os import remove
import sys
from collections import deque
N = int(sys.stdin.readline())
board = []
fishes = []
for row in range(N):
    row_fish = list(map(int, sys.stdin.readline().split()))
    board.append(row_fish)
    for col in range(N):
        if row_fish[col] == 9:
            now_shark_loc = [row, col]
        elif row_fish[col] in [1, 2, 3, 4, 5, 6]:
            fishes.append([row, col, row_fish[col]])

def check_small_fish():
    min_dist = N ** 2 + 1
    min_idx = 0
    for idx, (fish_row, fish_col, fish_weight) in enumerate(fishes):
        if fish_weight < shark_weight:
            plus_second = check_going_fish(fish_row, fish_col)
            # print("I am going ", fish_row, fish_col, "in", plus_second, "seconds")
            if plus_second:
                if plus_second < min_dist:
                    min_dist = plus_second
                    min_idx = idx
    if min_dist < N ** 2:
        answer = (fishes[min_idx][0], fishes[min_idx][1], min_dist)
        fishes.pop(min_idx)
        return answer
    return None

def check_going_fish(row, col):
    # print("Target :", row, col)
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    (shark_row, shark_col) = now_shark_loc
    que = deque([[shark_row, shark_col, 0]])
    visit = [[0 for _ in range(N)] for _ in range(N)]
    visit[shark_row][shark_col] = 1
    while que:
        now_row, now_col, second = que.popleft()
        # print(now_row, now_col)
        if now_row == row and now_col == col:
            return second
        for dir in dirs:
            next_row = now_row + dir[0]
            next_col = now_col + dir[1]
            if 0<=next_row<N and 0<=next_col<N and board[next_row][next_col] <= shark_weight and visit[next_row][next_col] == 0:
                # print("I can go ", next_row, next_col, "in", second + 1, "seconds")
                que.append([next_row, next_col, second + 1])
                visit[next_row][next_col] = 1
    return None

second = 0
shark_weight = 2
eating_fish = 0
while True:
    # print("="*20)
    # print("I am", shark_weight, "weight")
    fishes.sort(key = lambda x : (abs(now_shark_loc[0] - x[0]) + abs((now_shark_loc[1] - x[1])), x[0], x[1]))
    check = check_small_fish()
    if check == None:
        # print("I can't go anywhere")
        print(second)
        break
    else:
        going_row, going_col, plus_seconds = check
        board[now_shark_loc[0]][now_shark_loc[1]] = 0
        board[going_row][going_col] = 9
        now_shark_loc = [going_row, going_col]
        eating_fish += 1
        second += plus_seconds
        if shark_weight == eating_fish:
            eating_fish = 0
            shark_weight += 1
    # print(f"Passing {plus_seconds} : {second}")
    # print("Eating Fish with going", [going_row, going_col])
    # for r in board:
    #     print(*r)