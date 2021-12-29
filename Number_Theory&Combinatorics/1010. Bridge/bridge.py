import sys
from math import factorial
N=int(sys.stdin.readline())
for i in range(N):
    a,b=map(int,sys.stdin.readline().split())
    print(factorial(b)//(factorial(a)*factorial(b-a)))