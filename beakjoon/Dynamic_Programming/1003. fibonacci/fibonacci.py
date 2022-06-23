import sys
N=int(sys.stdin.readline())
L=[]

for i in range(N):
    L.append(int(sys.stdin.readline()))

count0=[1,0]
count1=[0,1]

for i in range(2, max(L)+1):
    count0.append(count0[i-1]+count0[i-2])
    count1.append(count1[i-1]+count1[i-2])

for i in L:
    print(f"{count0[i]} {count1[i]}")
