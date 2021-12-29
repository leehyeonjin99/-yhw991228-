import sys
N,M=map(int, sys.stdin.readline().split())
if M>(N//2):
    M=N-M
result=1
for i in range(1,M+1):
    result=result*(N-i+1)/i
print(int(result))