import sys

N = int(sys.stdin.readline())
city = []
for _ in range(N):
    city.append(list(map(int, sys.stdin.readline().split())))

answer = sys.maxsize
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            if y - d1 < 0:
                break
            for d2 in range(1, N):
                if x + d1 + d2 >= N or y + d2 >= N:
                    break
            
                people_sum = {idx: 0 for idx in range(1, 6)}
                # area = [[0 for _ in range(N)] for _ in range(N)]
                for row in range(N):
                    for col in range(N):
                        if row + col < (x + y) and row < x + d1 and col <= y:
                            people_sum[1] += city[row][col]
                            # area[row][col] = 1
                        elif row - col < x - y and row <= x + d2 and y < col:
                            people_sum[2] += city[row][col]
                            # area[row][col] = 2
                        elif row - col > x - y + 2 * d1 and x + d1 <= row and col < y - d1 + d2:
                            people_sum[3] += city[row][col]
                            # area[row][col] = 3
                        elif row + col > x + y + 2 * d2 and x + d2 < row and y - d1 + d2 <= col:
                            people_sum[4] += city[row][col]
                            # area[row][col] = 4
                        elif x + y <= row + col <= x + y + 2 * d2 and x - y <= row - col <= x - y + 2 * d1:
                            people_sum[5] += city[row][col]
                            # area[row][col] = 5
                m, M = min(people_sum.values()), max(people_sum.values())
                # if x == 2 and y == 2 and d1 == 1 and d2 == 1:
                #     print("="*10)
                #     for a in area:
                #         print(*a)
                answer = min(answer, M - m)

print(answer)