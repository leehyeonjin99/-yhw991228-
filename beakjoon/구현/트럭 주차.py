import sys
A, B, C = map(int, sys.stdin.readline().split())
count = {time: 0 for time in range(1, 101)}
start = []
end = []
for _ in range(3):
    s, e = map(int, sys.stdin.readline().split())
    for t in range(s, e):
        count[t] += 1

answer = 0
for t in range(1, 101):
    c = count[t]
    if c == 1:
        answer += A
    elif c == 2:
        answer += (B * 2)
    elif c == 3:
        answer += (C * 3)
print(answer)