import sys, heapq
N = int(sys.stdin.readline())
left, right = [], []
for num in range(1, N+1):
    input_num = int(sys.stdin.readline())
    if len(left) == len(right):
        heapq.heappush(left, (-input_num, input_num))
    else:
        heapq.heappush(right, (input_num, input_num))

    if right and left[0][1] > right[0][0]:
        min = heapq.heappop(right)[0]
        max = heapq.heappop(left)[1]
        heapq.heappush(left, (-min, min))
        heapq.heappush(right, (max, max))
    
    print(left[0][1])
