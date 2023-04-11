import sys
N = int(sys.stdin.readline())
answer = 0
before = 0
money = list(map(int, sys.stdin.readline().split()))
for d in list(sys.stdin.readline())[:-1]:
    if d == 'B':
        before = (money[0] - 1 - before)
    elif d == 'S':
        before = (money[1] - 1 - before)
    elif d == 'G':
        before = (money[2] - 1 - before)
    elif d == 'P':
        before = (money[3] - 1 - before)
    elif d == 'D':
        before = money[3]
    answer += before

print(answer)