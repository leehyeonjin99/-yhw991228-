from collections import deque
import sys

N, M, oil = map(int, sys.stdin.readline().split())
board = []

for row in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))

taxi = list(map(lambda x : int(x) - 1, sys.stdin.readline().split()))

passenger_list = list(range(1, M + 1))
passengers_start = {idx : [] for idx in range(1, M + 1)}
passengers_end = {idx : [] for idx in range(1, M + 1)}

for idx in range(1, M + 1):
    start_row, start_col, end_row, end_col = map(int, sys.stdin.readline().split())
    passengers_start[idx] = [start_row - 1, start_col - 1]
    # board[start_row - 1][start_col - 1] = 2
    passengers_end[idx] = [end_row - 1, end_col - 1]

def check_shortest_dist():

    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    # shortest_dist = {idx : sys.maxsize for idx in passenger_list}
    dist_idx = {}
    check_cnt = 0
    
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque([[taxi, 0]])
    visited[taxi[0]][taxi[1]] = 1

    while que:
        (now_row, now_col), now_dist = que.popleft()

        for passenger_idx, (start_row, start_col) in passengers_start.items():
            if now_row == start_row and now_col == start_col:
                if now_dist not in dist_idx:
                    dist_idx[now_dist] = [[passenger_idx, [now_row, now_col]]]
                else:
                    dist_idx[now_dist].append([passenger_idx, [now_row, now_col]])
                check_cnt += 1
                break
        
        if check_cnt == len(passenger_list):
            tmp = sorted(list(dist_idx.items()))[0]
            dist = tmp[0]
            idx = sorted(tmp[1], key = lambda x: (x[1][0], x[1][1]))[0][0]
            return (idx, dist)

        for drow, dcol in dirs:
            next_row, next_col = now_row + drow, now_col + dcol
            if 0 <= next_row < N and 0 <= next_col < N and board[next_row][next_col] != 1 and visited[next_row][next_col] == 0:
                que.append([[next_row, next_col], now_dist + 1])
                visited[next_row][next_col] = 1
    
    return False, False

def start_end_dist(passenger_idx):
    dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque([[passengers_start[passenger_idx], 0]])
    visited[passengers_start[passenger_idx][0]][passengers_start[passenger_idx][1]] = 1

    while que:
        (now_row, now_col), now_dist = que.popleft()
        if [now_row, now_col] == passengers_end[passenger_idx]:
            return now_dist
        if now_dist > oil:
            return None
        
        for drow, dcol in dirs:
            next_row, next_col = now_row + drow, now_col + dcol
            if 0 <= next_row < N and 0 <= next_col < N and not board[next_row][next_col] and not visited[next_row][next_col]:
                que.append([[next_row, next_col], now_dist + 1])
                visited[next_row][next_col] = 1
    return None

passenger_clear = True
while passenger_list:
    shortest_passenger_idx, shortest_passenger_dist = check_shortest_dist()
    if not shortest_passenger_idx:
        passenger_clear = False
        # print("********** 갈 수 있는 곳이 없습니다 ************")
        break
    # print(f"========== SHORTEST PASSENGER {shortest_passenger_idx} with {shortest_passenger_dist} dist ==========")
    passenger_list.remove(shortest_passenger_idx)

    board[passengers_start[shortest_passenger_idx][0]][passengers_start[shortest_passenger_idx][1]] = 0
    taxi = [passengers_start[shortest_passenger_idx][0], passengers_start[shortest_passenger_idx][1]]
    oil -= shortest_passenger_dist
    # print("승객에게 도착했습니니다 => oil :", oil)
    if oil <= 0:
        passenger_clear = False
        # print("************ 연료가 소진되었습니다. *************")
        break

    going_dist = start_end_dist(shortest_passenger_idx)
    if going_dist == None:
        passenger_clear = False
        # print("********* 도착지로 갈 수 없습니다 *********")
        break
    taxi = passengers_end[shortest_passenger_idx]
    del(passengers_start[shortest_passenger_idx])
    del(passengers_end[shortest_passenger_idx])
    oil -= going_dist
    # print(f"도착지까지 {going_dist}만에 도착했습니다. => oil :", oil)
    if oil < 0:
        passenger_clear = False
        # print("************* 도착지에 도착하는 과정에서 연료가 소진되었습니다. ****************")
        break

    oil += 2 * going_dist
    # print("무사히 도착하여 연료가 추가되었습니다. => oil :", oil)

print(oil if passenger_clear else -1)