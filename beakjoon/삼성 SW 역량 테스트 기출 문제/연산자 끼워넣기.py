import sys
from collections import deque

N = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))
operator = list(map(int, sys.stdin.readline().split())) # +, -, *, //
m, M = 1000000000, -1000000000
que = deque([])
que.append([0, numbers[0], operator])

while que:
    num_idx, answer, now_operator = que.popleft()
    # print(answer, now_operator)
    if num_idx == N-1:
        m = min(m, answer)
        M = max(M, answer)
        continue
    for idx in range(4):
        if now_operator[idx] > 0:
            if idx == 0:
                next_answer = answer + numbers[num_idx + 1]
            elif idx == 1:
                next_answer = answer - numbers[num_idx + 1]
            elif idx == 2:
                next_answer = answer * numbers[num_idx + 1]
            else:
                next_answer = answer // numbers[num_idx + 1] if answer >=0 else -((-answer) // numbers[num_idx + 1])
            next_operator = now_operator.copy()
            next_operator[idx] -= 1
            que.append([num_idx + 1, next_answer, next_operator])
            # print(num_idx + 1, numbers[num_idx + 1], next_answer)

print(M)
print(m)
