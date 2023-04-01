import sys
input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
answer = N
for idx in range(N):
    num = A[idx] - B
    if num <= 0:
        continue
    answer += (num // C if num % C == 0 else num // C + 1)
print(answer)