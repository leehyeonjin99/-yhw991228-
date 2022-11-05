import sys
R, C, M = map(int, sys.stdin.readline().split())
sharks = {}
fishing = [[[] for _ in range(C)] for _ in range(R)]
dirs = {1: [-1, 0], 2: [1, 0], 3: [0, 1], 4: [0, -1]}
for idx in range(M):
    r, c, s, d, z = map(int, sys.stdin.readline().split())
    sharks[idx] = [[r - 1, c - 1], s, dirs[d], z]
    fishing[r - 1][c - 1].append(idx)

answer = 0
for fisher_col in range(C):
    # print("=="*10)
    for row in range(R):
        if fishing[row][fisher_col]:
            answer += sharks[fishing[row][fisher_col][0]][-1]
            # print(f"Fisher Catch shark", (fishing[row][fisher_col][0], sharks[fishing[row][fisher_col][0]][-1]))
            del sharks[fishing[row][fisher_col][0]]
            fishing[row][fisher_col].pop()    
            break
    fishing = [[[] for _ in range(C)] for _ in range(R)]
    remove_shark_idxs = []
    for shark in sharks:
        # print(shark, "Shark moving")
        (shark_row, shark_col), shark_speed, (shark_drow, shark_dcol), shark_size = sharks[shark]
        for _ in range(shark_speed):
            if not (0 <= shark_row + shark_drow < R and 0 <= shark_col + shark_dcol < C):
                shark_drow = -shark_drow
                shark_dcol = -shark_dcol
            # print((shark_row, shark_col), end = " => ")
            shark_row += shark_drow
            shark_col += shark_dcol
            # print((shark_row, shark_col))
        sharks[shark][0] = [shark_row, shark_col]
        sharks[shark][2] = [shark_drow, shark_dcol]
        if fishing[shark_row][shark_col]:
            current_shark_idx = fishing[shark_row][shark_col][0]
            current_shark_size = sharks[current_shark_idx][-1]
            if current_shark_size < shark_size:
                remove_shark_idxs.append(current_shark_idx)
                fishing[shark_row][shark_col].pop()
                fishing[shark_row][shark_col].append(shark)
            else:
                remove_shark_idxs.append(shark)
        else:
            fishing[shark_row][shark_col].append(shark)

    for idx in remove_shark_idxs:
        del sharks[idx]
print(answer)