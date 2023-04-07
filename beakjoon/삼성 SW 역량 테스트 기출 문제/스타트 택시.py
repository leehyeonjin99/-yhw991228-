import sys
from collections import deque

N, M, taxi_oil = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    board.append(list(map(int, sys.stdin.readline().split())))
taxi_row, taxi_col = map(int, sys.stdin.readline().split())
taxi_row, taxi_col = taxi_row - 1, taxi_col - 1
customers = {}
for idx in range(M):
    s_row, s_col, e_row, e_col = map(int, sys.stdin.readline().split())
    s_row, s_col, e_row, e_col = s_row - 1, s_col - 1, e_row - 1, e_col - 1
    board[s_row][s_col] = 2
    customers[(s_row, s_col)] = (e_row, e_col)

def find_customer():
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque([[taxi_row, taxi_col, 0]])
    min_dist = N * N + 1
    min_loc = (N + 1, N + 1)
    while que:
        now_row, now_col, now_dist = que.popleft()
        if board[now_row][now_col] == 2 and now_dist <= min_dist:
            min_dist = now_dist
            if now_dist == min_dist:
                if now_row < min_loc[0] or (now_row == min_loc[0] and now_col < min_loc[1]):
                    min_loc = [now_row, now_col]
            else:
                min_loc = [now_row, now_col]
            continue
        for (drow, dcol) in [[-1, 0], [0, -1], [1, 0], [0, 1]]:
            next_row = now_row + drow
            next_col = now_col + dcol
            if 0 <= next_row < N and 0 <= next_col < N and board[next_row][next_col] != 1 and not visited[next_row][next_col]:
                visited[next_row][next_col] = 1
                que.append([next_row, next_col, now_dist + 1])
    return min_loc, min_dist

def take_customer(s_row, s_col, e_row, e_col):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    que = deque([[s_row, s_col, 0]])
    while que:
        now_row, now_col, now_dist = que.popleft()
        if now_row == e_row and now_col == e_col:
            return now_dist
        for (drow, dcol) in zip([1, -1, 0, 0], [0, 0, 1, -1]):
            next_row = now_row + drow
            next_col = now_col + dcol
            if 0 <= next_row < N and 0 <= next_col < N and board[next_row][next_col] != 1 and not visited[next_row][next_col]:
                visited[next_row][next_col] = 1
                que.append([next_row, next_col, now_dist + 1])
    return -1

def solution():
    global taxi_oil, taxi_row, taxi_col, board
    customer_cnt = 0
    while customer_cnt < M:
        (customer_row, customer_col), customer_dist = find_customer()
        if customer_dist == N * N + 1:
            return  -1
        end_dist = take_customer(customer_row, customer_col, *customers[(customer_row, customer_col)])
        if end_dist == -1 or taxi_oil < customer_dist + end_dist:
            return -1
        customer_cnt += 1
        board[customer_row][customer_col] = 0
        (taxi_row, taxi_col) = customers[(customer_row, customer_col)]
        taxi_oil = taxi_oil - customer_dist + end_dist
    return taxi_oil

print(solution())