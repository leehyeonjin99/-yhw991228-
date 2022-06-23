import sys
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(sys.stdin.readline()[:-1])
L=list(set(L))
L.sort(key=lambda word : (len(word), word))
for word in L:
    print(word)