import sys

N = int(sys.stdin.readline())

def solution():
    answer = []
    num = 0
    cnt = 0
    for word in words:
        if word.isdigit():
            num = num * 10 + int(word)
            cnt += 1
        else:
            if cnt:
                answer.append(num)
            num = 0
            cnt = 0
    return answer

nums = []
for _ in range(N):
    words = list(sys.stdin.readline())
    nums += solution()

nums.sort()
for num in nums:
    print(num)