import sys
A, B, C = map(int, sys.stdin.readline().split())
def square(A, B):
    if B == 1:
        return A % C
    half = square(A, B // 2)
    if B % 2 == 0:
        return (half * half) % C
    else:
        return (half * half * A ) % C 

print(square(A, B))