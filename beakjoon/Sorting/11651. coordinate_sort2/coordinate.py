import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int,sys.stdin.readline().split())))

L.sort(key=lambda x : (x[1],x[0]))

for point in L:
    print(f"{point[0]} {point[1]}")