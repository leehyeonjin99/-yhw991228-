import sys

N = int(sys.stdin.readline())

red = [[0 for _ in range(4)] for _ in range(4)]
blue = [[0 for _ in range(6)] for _ in range(4)]
green = [[0 for _ in range(4)] for _ in range(6)]
score = 0
tile_count = 0

def downing(board):
    board_tmp = [tmp.copy() for tmp in board]
    for row in range(len(board_tmp))[::-1]:
        if 1 not in board_tmp[row]:
            continue
        next_cnt = 1
        while row + next_cnt < len(board_tmp) and 1 not in board_tmp[row + next_cnt]:
            next_cnt += 1
        if next_cnt == 1:
            continue
        board_tmp[row], board_tmp[row + next_cnt - 1] = board_tmp[row + next_cnt - 1], board_tmp[row]
    return board_tmp


def blue_row_col_check(tiles):
    global blue
    count = 0
    for row_col, idxs in enumerate(zip(*tiles)):
        if row_col == 0:
            continue
        if row_col == 1:
            blue_tmp = list(zip(*blue))
            for idx in idxs:
                if sum(blue_tmp[idx]) == len(blue_tmp[0]):
                    blue_tmp[idx] = [0 for _ in range(len(blue_tmp[0]))]
                    count += 1
    if count:
            blue_tmp = downing([list(tmp) for tmp in blue_tmp])
    if 1 in blue_tmp[0] or 1 in blue_tmp[1]:
        move_cnt = 2 if 1 in blue_tmp[0] else 1
        blue_tmp = [[0 for _ in range(len(blue_tmp[0]))] for _ in range(move_cnt)] + blue_tmp[:-move_cnt]
    for _ in range(3):
        blue_tmp = list(zip(*blue_tmp))
    blue = [list(tmp) for tmp in blue_tmp]
    return count

def green_row_col_check(tiles):
    global green
    count = 0
    for row_col, idxs in enumerate(zip(*tiles)):
        if row_col == 0:
            for idx in idxs:
                if sum(green[idx]) == len(green[0]):
                    green[idx] = [0 for _ in range(len(green[0]))]
                    count += 1
        if row_col == 1:
            continue
    if count:
        green = downing(green)
    if 1 in green[0] or 1 in green[1]:
        move_cnt = 2 if 1 in green[0] else 1
        green = [[0 for _ in range(len(green[0]))] for _ in range(move_cnt)] + green[:-move_cnt]
    return count

for _ in range(N):
    # print("="*20)
    # print("ROUND ", _)
    # t = 1 : (x, y)
    # t = 2 : (x, y), (x, y + 1)
    # t = 3 : (x, y), (x, + 1, y)
    t, x, y = map(int, sys.stdin.readline().split())

    tiles = [[x, y]]
    if t == 2:
        tiles.append([x, y + 1])
    elif t == 3:
        tiles.append([x + 1, y])

    # blue board
    blue_tiles =  [[x, 0 if idx == 0 else 1] for idx, (x, y) in enumerate(tiles)] if t == 2 else [[x, 0] for (x, y) in tiles]
    blue_break = False
    while not blue_break:
        next_blue_tiles = [blue_tile.copy() for blue_tile in blue_tiles]
        next_blue_tiles = [[x, y + 1] for (x, y) in next_blue_tiles]
        for (x, y) in next_blue_tiles:
            if not(0 <= x < 4 and 0 <= y < 6) or  blue[x][y] == 1:
                for (x, y) in blue_tiles:
                    blue[x][y] = 1
                score += blue_row_col_check(blue_tiles)
                blue_break = True
                break
        blue_tiles = [blue_tile.copy() for blue_tile in next_blue_tiles]
    
    # green board
    green_tiles = [[0 if idx == 0 else 1, y] for idx, (x, y) in enumerate(tiles)] if t == 3 else [[0, y] for (x, y) in tiles]
    # print("green_tiles :", green_tiles)
    green_break = False
    while not green_break:
        next_green_tiles = [green_tile.copy() for green_tile in green_tiles]
        next_green_tiles = [[x + 1, y] for (x, y) in next_green_tiles]
        for (x, y) in next_green_tiles:
            if not(0 <= x < 6 and 0 <= y < 4) or  green[x][y] == 1:
                for (x, y) in green_tiles:
                    green[x][y] = 1
                score += green_row_col_check(green_tiles)
                green_break = True
                break
        green_tiles = [green_tile.copy() for green_tile in next_green_tiles]
    # print("BLUE")
    # for b in blue:
    #     print(*b)
    # print("GREEN")
    # for g in green:
    #     print(*g)

print(score)
cnt = 0
for b in blue:
    cnt += sum(b)
for g in green:
    cnt += sum(g)
print(cnt)