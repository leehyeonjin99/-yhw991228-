import sys

N=int(sys.stdin.readline())
L=[]

for i in range(N):
    info=sys.stdin.readline().split()
    L.append([info[0],info[1]])

L.sort(key=lambda x: (int(x[0])))

for info in L:
    print(f"{info[0]} {info[1]}")
