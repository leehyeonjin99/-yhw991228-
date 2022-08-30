from collections import deque
import copy
import sys

board = []
fishes = {idx: [] for idx in range(1, 17)}
dirs = [[-1, 0], [-1, -1], [0, -1], [1, -1], [1, 0], [1, 1], [0, 1], [-1, 1]]
for row in range(4):
    info = list(map(int, sys.stdin.readline().split()))
    row_fish = []
    for col in range(4):
        row_fish.append(info[2 * col])
        fishes[info[2 * col]] = [info[2 * col + 1] - 1, [row, col]]
    board.append(row_fish)

def shark_check(board, shark_loc, shark_dir):
    fishes_loc = []
    shark_row, shark_col = shark_loc
    while 0 <= shark_row + shark_dir[0] < 4 and 0 <= shark_col + shark_dir[1] < 4:
        shark_row += shark_dir[0]
        shark_col += shark_dir[1]
        if board[shark_row][shark_col]:
            fishes_loc.append([shark_row, shark_col])
    return fishes_loc


shark_loc = [0, 0]
shark_dir = dirs[fishes[board[0][0]][0]]
fish_sum = board[0][0]
reamin_fishes = list(range(1, 17))
reamin_fishes.remove(board[0][0])
board[0][0] = 0
que = deque([[board, shark_loc, shark_dir, fishes, fish_sum, reamin_fishes]])
answer = 0

while que:
    now_board, now_shark_loc, now_shark_dir, now_fishes, now_fish_sum, now_remain_fishes = que.popleft()
    # print("="*20)
    # print(f"My Location is {now_shark_loc} with {now_shark_dir} and My Score is {now_fish_sum}")
    # for tmp in now_board:
    #     print(*tmp)
    next_fishes = copy.deepcopy(now_fishes)
    for fish in now_remain_fishes:
        row, col = next_fishes[fish][1]
        for rotation_idx in range(8):
            now_dir = dirs[next_fishes[fish][0]]
            next_row = row + now_dir[0]
            next_col = col + now_dir[1]
            if 0 <= next_row < 4 and 0 <= next_col < 4 and not (next_row == now_shark_loc[0] and next_col == now_shark_loc[1]):
                next_fishes[fish][1] = [next_row, next_col]
                if now_board[next_row][next_col]:
                    next_fishes[now_board[next_row][next_col]][1] = [row, col]
                now_board[row][col], now_board[next_row][next_col] = now_board[next_row][next_col], now_board[row][col]
                break
            next_fishes[fish][0] = (next_fishes[fish][0] + 1) % 8

    # 물고기 이동 확인
    # print("AFTER MOVING FISH!!")
    # for tmp in now_board:
    #     print(*tmp)
    
    can_eat_fishes = shark_check(now_board, now_shark_loc, now_shark_dir)

    # 상어 이동
    if can_eat_fishes:
        # print(can_eat_fishes)
        for (fish_row, fish_col) in can_eat_fishes:

            next_board = [tmp.copy() for tmp in now_board]
            next_remain_fishes = now_remain_fishes.copy()

            next_shark_loc = [fish_row, fish_col]
            next_shark_dir = dirs[next_fishes[now_board[fish_row][fish_col]][0]]
            next_fish_sum = now_fish_sum + now_board[fish_row][fish_col]
            next_remain_fishes.remove(now_board[fish_row][fish_col])
            next_board[fish_row][fish_col] = 0
            que.append([next_board, next_shark_loc, next_shark_dir, next_fishes, next_fish_sum, next_remain_fishes])
            # print(f"{[fish_row, fish_col]}, {now_board[fish_row][fish_col]} Eating => {next_fish_sum}")
            # for tmp in next_board:
            #     print(*tmp)
    else:
        answer = max(answer, now_fish_sum)

print(answer)