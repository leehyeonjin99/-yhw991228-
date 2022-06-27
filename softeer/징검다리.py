import sys
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
result = [1 for _ in range(N)]
for end in range(1, N):
    for before in range(end):
        if A[before] < A[end]:
            result[end] = max(result[end], result[before] + 1)
print(max(result))