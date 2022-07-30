# 구명을 통과해야하는 붉은 구슬의 방문 여부만 판단 필요하다 생각했지만, 붉은 구슬과 푸른 구슬에 대한 방문 여부가 중요하다.

import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
board = []
for _ in range(N):
    sub_board = sys.stdin.readline()[:-1]
    if 'R' in sub_board:
        red_position = [_, sub_board.index('R')]
    if 'B' in sub_board:
        blue_position = [_, sub_board.index('B')]
    board.append(sub_board)

def move(now_x, now_y, dir_x, dir_y):
    next_x, next_y = now_x, now_y
    while board[next_x + dir_x][next_y + dir_y] != '#':
        next_x += dir_x
        next_y += dir_y
        if board[next_x][next_y] == 'O':
            return next_x, next_y, True
    return next_x, next_y, False

def bfs():
    visited = {}
    direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
    que = deque([[red_position, blue_position, 0]])
    visited[(red_position[0], red_position[1], blue_position[0], blue_position[1])] = True

    while que:
        (red_x, red_y), (blue_x, blue_y), count = que.popleft()
        if count >= 10:
            print(-1)
            return
        for dir in direction:
            next_red_x, next_red_y, red_goal = move(red_x, red_y, dir[0], dir[1])
            next_blue_x, next_blue_y, blue_goal = move(blue_x, blue_y, dir[0], dir[1])
            # print("RED", next_red_x, next_red_y, red_goal)
            # print("BLUE", next_blue_x, next_blue_y, blue_goal)

            if blue_goal:
                continue
            else:
                if red_goal:
                    print(count + 1)
                    return
                if next_red_x == next_blue_x and next_red_y == next_blue_y:
                    if abs(next_red_x - red_x) + abs(next_red_y - red_y) > abs(next_blue_x - blue_x) + abs(next_blue_y - blue_y):
                        next_red_x -= dir[0]
                        next_red_y -= dir[1]
                    else:
                        next_blue_x -= dir[0]
                        next_blue_y -= dir[1]
                if (next_red_x, next_red_y, next_blue_x, next_blue_y) not in visited:
                    visited[(next_red_x, next_red_y, next_blue_x, next_blue_y)] = True
                    que.append([[next_red_x, next_red_y], [next_blue_x, next_blue_y], count+1])
                    # print("ADD NEXT", [[next_red_x, next_red_y], [next_blue_x, next_blue_y], count+1])
                    
    print(-1)
    return

bfs()