import sys
N,M=map(int, sys.stdin.readline().split())
D=N-M
def count(N,k):
    count=0
    while N!=0:
        N=N//k
        count+=N
    return count
two=count(N,2)-count(M,2)-count(N-M,2)
five=count(N,5)-count(M,5)-count(N-M,5)
print(min(two,five))