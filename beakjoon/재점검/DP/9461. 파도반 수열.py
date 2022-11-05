import sys

L = [0, 1, 1, 1, 2, 2]
problems = []

N = int(sys.stdin.readline())
for _ in range(N):
    problems.append(int(sys.stdin.readline()))

M = max(problems)
for idx in range(6, M + 1):
    L.append(L[idx - 1] + L[idx - 5])

for problem in problems:
    print(L[problem])