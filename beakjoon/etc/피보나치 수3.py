import sys
a, b = 0, 1
p = int(sys.stdin.readline()) % (15 * 10**5)
for i in range(p):
    a, b = b, (a+b) % 1000000
print(a)