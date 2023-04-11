import sys

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    num = 1
    cnt = 1
    while True:
        if num % n == 0:
            print(cnt)
            break
        cnt += 1
        num = num * 10 + 1