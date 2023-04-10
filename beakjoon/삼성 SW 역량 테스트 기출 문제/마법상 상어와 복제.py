import sys
M, S = map(int, sys.stdin.readline().split())
board = [[[] for _ in range(4)] for _ in range(4)]
fishes_loc = set([])
smells_loc = {1:set([]), 2: set([])}
for _ in range(M):
    r, c, d = map(int, sys.stdin.readline().split())
    r, c, d = r - 1, c - 1, d -1
    fishes_loc.add((r, c))
    board[r][c].append(d)
s_row, s_col = map(int, sys.stdin.readline().split())
s_row, s_col = s_row - 1, s_col - 1

dirs = {0: [0, -1], 1: [-1, -1], 2: [-1, 0], 3: [-1, 1], 4: [0, 1], 5: [1, 1], 6: [1, 0], 7: [1, -1]}

def fish_moving():
    next_board = [[[] for _ in range(4)] for _ in range(4)]
    add_fishes_loc = set([])
    fish_cnt = 0
    for (row, col) in fishes_loc:
        for dir_idx in board[row][col]:
            check = False
            for rot in range(8): 
                next_dir_idx = (dir_idx - rot) % 8
                next_row, next_col = row + dirs[next_dir_idx][0], col + dirs[next_dir_idx][1]
                if 0 <= next_row < 4 and 0 <= next_col < 4 and (next_row, next_col) not in smells_loc[1] and (next_row, next_col) not in smells_loc[2] and not (next_row == s_row and next_col == s_col):
                    next_board[next_row][next_col].append(next_dir_idx)
                    add_fishes_loc.add((next_row, next_col))
                    fish_cnt += 1
                    break
            # if not check:
            #     next_board[row][col].append(dir_idx)
            #     add_fishes_loc.add((row, col))
    return next_board, add_fishes_loc, fish_cnt

from collections import deque
drows = [1, -1, 0, 0]
dcols = [0, 0, 1, -1]
dnames = ['3', '1', '4', '2']
def shark_moving(board):
    max_fish = -1
    max_fish_loc = []
    max_move_type = ''
    max_move_locs = []
    now_fish_loc = []
    # if board[s_row][s_col]:
    #     now_fish_loc.append((s_row, s_col))
    que = deque([[s_row, s_col, 0, '', [(s_row, s_col)], now_fish_loc, 0]]) # 행, 열, 이동 횟수, 이동 방법, 이동 위치, 물고기 위치, 제거 물고기 개수
    while que:
        now_row, now_col, now_move, now_move_type, now_locs, now_fish_loc, now_fish = que.popleft()
        if now_move == 3:
            if max_fish < now_fish or (max_fish == now_fish and now_move_type < max_move_type):
                max_fish, max_move_type, max_move_locs, max_fish_loc = now_fish, now_move_type, now_locs, now_fish_loc
            continue
        for (drow, dcol, dname) in zip(drows, dcols, dnames):
            next_row, next_col = now_row + drow, now_col + dcol
            if 0 <= next_row < 4 and 0 <= next_col < 4 and (next_row, next_col):
                if board[next_row][next_col] and (next_row, next_col) not in now_locs:
                    que.append([next_row, next_col, now_move + 1, now_move_type + dname, now_locs + [(next_row, next_col)], now_fish_loc + [(next_row, next_col)], now_fish + len(board[next_row][next_col])])
                else:
                    que.append([next_row, next_col, now_move + 1, now_move_type + dname, now_locs + [(next_row, next_col)], now_fish_loc , now_fish])
    return max_move_locs, max_fish, max_fish_loc

def solution():
    global s_row, s_col, board, fishes_loc
    total_fish = M
    for step in range(S):
        # print("=============== ROUND ", step)
        
        
        # 물고기 이동
        next_board, add_fishes_loc, add_fish_cnt = fish_moving()
        if step == 4 or step == 3:
            print("이동 물고기")
            for tmp in next_board:
                print(*tmp)
        total_fish += add_fish_cnt
        shark_move_locs, reduced_fish, reduced_fish_loc = shark_moving(next_board)
        total_fish -= reduced_fish
        (s_row, s_col) = shark_move_locs[-1]
        

        # 물고기 제거
        smells_loc[2] = smells_loc[1]
        smells_loc[1] = set([])
        for (row, col) in reduced_fish_loc:
            next_board[row][col] = []
            add_fishes_loc.remove((row, col))
            smells_loc[1].add((row, col))
        fishes_loc |= add_fishes_loc

        if step == 3 or step == 4:
            print("상어 이동")
            for tmp in next_board:
                print(*tmp)
        

        # 보드 업데이트
        for row in range(4):
            for col in range(4):
                board[row][col] += next_board[row][col]
        if step == 3 or step == 4:
            print("최종 상태")
            for tmp in board:
                print(*tmp)
            # print("물고기 냄새 :", smells_loc)
            print("상어 위치 :", (s_row, s_col))
            print(total_fish)
    return total_fish

print(solution())