import sys
N=int(sys.stdin.readline())
L=list(map(int,sys.stdin.readline().split()))
L.sort()
sum=0
for i,num in enumerate(L):
    sum+=(N-i)*num
print(sum)