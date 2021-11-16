import sys
num=list(sys.stdin.readline())
num.sort(reverse=True)
for i in num:
    print(i,end='')