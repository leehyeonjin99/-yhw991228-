import sys
N=int(sys.stdin.readline())
five=0
while N!=0:
    N=N//5
    five+=N
print(five)