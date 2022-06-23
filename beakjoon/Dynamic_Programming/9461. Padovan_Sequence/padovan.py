import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(int(sys.stdin.readline()))

padovan=[1,1,1]
for i in range(3, max(L)):
    padovan.append(padovan[i-3]+padovan[i-2])

for num in L:
    print(padovan[num-1])
