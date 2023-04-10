import sys
word = list(sys.stdin.readline())[:-1]
alpha = {a: 0 for a in 'abcdefghijklmnopqrstuvwxyz'}
for a in word:
    alpha[a] += 1
print(' '.join(map(lambda x: str(x), list(alpha.values()))))