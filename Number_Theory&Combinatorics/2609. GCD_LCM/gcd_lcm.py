import sys
A,B=map(int,sys.stdin.readline().split())
m=min(A, B)
M=max(A, B)
lcm=1
gcd=M
for i in range(1,m+1,1):
    if (M%i==0) & (m%i==0):
        lcm=i

while (1):
    if gcd%m==0:
        break
    gcd+=M
print(f"{lcm}\n{gcd}")
