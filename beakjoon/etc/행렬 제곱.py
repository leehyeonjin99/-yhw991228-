import sys

def mul_add(A, B):
    S = 0
    for a, b in zip(A, B):
        S += a * b % 1000
    return S

def matrix_mul(A, B):
    n = len(A)
    result = [[0 for _ in range(n)] for _ in range(n)]
    B = [list(tmp) for tmp in zip(*B)]
    for i in range(n):
        for j in range(n):
            result[i][j] = mul_add(A[i], B[j]) % 1000
    return result

def square(A, n):
    if n == 1:
        for i in range(len(A)):
            for j in range(len(A)):
                A[i][j] %= 1000
        return A
    if n % 2 == 0:
        tmp = square(A, n // 2)
        return matrix_mul(tmp, tmp)
    else:
        tmp = square(A, n - 1)
        return matrix_mul(tmp, A)

N, B = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

for row in square(matrix, B):
    print(*row)