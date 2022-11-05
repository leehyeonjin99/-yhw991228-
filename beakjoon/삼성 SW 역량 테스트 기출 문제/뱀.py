import sys

N = int(sys.stdin.readline())
board = [[0 for _ in range(N)] for _ in range(N)]

apple_num = int(sys.stdin.readline())
for _ in range(apple_num):
    x, y = map(int, sys.stdin.readline().split())
    board[x-1][y-1] = 1

direction_num = int(sys.stdin.readline())
direction = []
before_time = 0
for _ in range(direction_num):
    time, dir = sys.stdin.readline().split()
    direction.append([int(time) - before_time, dir])
    before_time = int(time)
direction.append([N, 'D'])
# print(direction)

snake_location = [[0, 0]]
dxdy = [[0, 1], [1, 0], [0, -1], [-1, 0]]
dxdy_idx = 0
dir_idx = 0
time = 0
now_x, now_y = 0, 0

while True:
    # print(snake_location)
    time += 1
    if direction[dir_idx][0] > 0:
        # print(dxdy_idx)
        next_x, next_y = now_x + dxdy[dxdy_idx][0], now_y + dxdy[dxdy_idx][1]
        # print(f"Moving {now_x, now_y} => {next_x, next_y}")
        direction[dir_idx][0] -= 1
        if direction[dir_idx][0] == 0:
            # print(f"Turning to", "Right" if direction[dir_idx][1] == 'D' else "Left")
            dxdy_idx = dxdy_idx + 1 if direction[dir_idx][1] == 'D' else dxdy_idx - 1
            dir_idx += 1
            if dxdy_idx >= 4:
                dxdy_idx = dxdy_idx % 4
            if dxdy_idx < -4:
                dxdy_idx = -((-dxdy_idx) % 4)

    else:
        break

    if 0<=next_x<N and 0<=next_y<N and [next_x, next_y] not in snake_location:
        is_apple = (board[next_x][next_y] == 1)
        if is_apple:
            snake_location.append([next_x, next_y])
            board[next_x][next_y] = 0
            # print("Eating Apple!!")
        else:
            snake_location = snake_location[1:]
            snake_location.append([next_x, next_y])
        now_x, now_y = next_x, next_y
    else:
        # print("Facing Wall or ME")
        break

print(time)