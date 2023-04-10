import sys
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    i = 5
    count = 0
    # 0의 개수를 알기 위해서는 소인수 분해시 5의 개수를 알면 된다.
    # 25의 경우 -> 5의 배수의 개수에서 count + 25의 배수의 개수에서 count = 2
    while i <= num:
        count += num // i
        i *= 5
    print(count)