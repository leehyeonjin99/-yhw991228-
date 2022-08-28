import sys
from itertools import product

# f = open("/Users/hyounjinlee/development/Algorithm-study/beakjoon/삼성 SW 역량 테스트 기출 문제/log.txt", mode = "wt")

lengths = list(map(int, sys.stdin.readline().split()))
# 1: blue, 0: black
# 칸 정보 : [color, score, next_idxs]
board = {
    0: [0, 0, [1]],
    1: [0, 2, [2]],
    2: [0, 4, [3]],
    3: [0, 6, [4]],
    4: [0, 8, [5]],
    5: [1, 10, [6, 20]],
    6: [0, 12,[7]],
    7: [0, 14, [8]],
    8: [0, 16, [9]],
    9: [0, 18, [10]],
    10: [1, 20, [11, 23]],
    11: [0, 22, [12]],
    12: [0, 24, [13]],
    13: [0, 26, [14]],
    14: [0, 28, [15]],
    15: [1, 30, [16, 25]],
    16: [0, 32, [17]],
    17: [0, 34, [18]],
    18: [0, 36, [19]],
    19: [0, 38, [31]],
    20: [0, 13, [21]],
    21: [0, 16, [22]],
    22: [0, 19, [28]],
    23: [0, 22, [24]],
    24: [0, 24, [28]],
    25: [0, 28, [26]],
    26: [0, 27, [27]],
    27: [0, 26, [28]],
    28: [0, 25, [29]],
    29: [0, 30, [30]],
    30: [0, 35, [31]],
    31: [0, 40, [32]],
    32: [0, 0, []]
}

answer = 0
for round, horse_comb in enumerate(product(range(4), repeat = 10)):
    if horse_comb[:4] == (0, 1, 2, 3):
        break
    # f.write(f"ROUND {round} : {horse_comb}\n")
    horse_loc = [0, 0, 0, 0]
    game_check = True
    game_answer = 0
    for horse_idx, moving_length in zip(horse_comb, lengths):
        # f.write(f"Moving {horse_idx} with {moving_length} : ")
        if horse_loc[horse_idx] == 32:
            game_check = False
            # f.write("현재 종점이므로 움직일 수 없음\n")
            break
        # f.write(f"{horse_loc[horse_idx]} => ")
        for cnt in range(moving_length):
            if cnt == 0 and board[horse_loc[horse_idx]][0] == 1:
                horse_loc[horse_idx] = board[horse_loc[horse_idx]][-1][-1]
                continue
            horse_loc[horse_idx] = board[horse_loc[horse_idx]][-1][0]
            if horse_loc[horse_idx] == 32:
                break
        horse_except_loc = horse_loc.copy()
        horse_except_loc.pop(horse_idx)
        if horse_loc[horse_idx] != 32 and horse_loc[horse_idx] in horse_except_loc:
            game_check = False
            # f.write("이미 자리 있음\n")
            break
        game_answer += board[horse_loc[horse_idx]][1]
        # f.write(f"{horse_loc[horse_idx]} : {board[horse_loc[horse_idx]][1]}점 얻음 즉, {game_answer}점\n")
    if game_check:
        answer = max(answer, game_answer)

print(f"{answer}")