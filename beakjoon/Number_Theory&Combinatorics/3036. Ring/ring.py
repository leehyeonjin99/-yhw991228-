import sys
import math
N=int(sys.stdin.readline())
L=list(map(int, sys.stdin.readline().split()))
for l in L[1:]:
    LCM=L[0]*l//math.gcd(L[0],l)
    print(f"{LCM//l}/{LCM//L[0]}")