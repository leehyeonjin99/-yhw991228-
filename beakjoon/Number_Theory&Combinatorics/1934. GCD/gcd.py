import sys
import math
N=int(sys.stdin.readline())
L=[]
for i in range(N):
    L.append(list(map(int, sys.stdin.readline().split())))
for l in L:
    g=math.gcd(l[0],l[1])
    print(int(l[0]*l[1]/g))