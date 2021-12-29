'''import sys
import math
N,M=map(int, sys.stdin.readline().split())
if M>(N//2):
    M=N-M
result=math.factorial(N)/(math.factorial(M)*math.factorial(N-M))
print(result%10007)'''

import sys
import math
N,M=map(int, sys.stdin.readline().split())
result=math.factorial(N)//(math.factorial(M)*math.factorial(N-M))
print(result%10007)