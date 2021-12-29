import sys
N, M=map(int,sys.stdin.readline().split())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))
L=L[::-1]

count=0
for l in L:
    if M==0:
        break
    count+=M//l
    M=M%l
print(count)    