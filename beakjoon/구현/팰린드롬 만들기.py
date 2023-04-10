import sys
word = sys.stdin.readline()[:-1]
N = len(word)
for L in range(N, 2 * N):
    half = L // 2
    add = L - N
    if L % 2 == 0 and word[add: half] == word[half:][::-1]:
        break
    elif L % 2 == 1 and word[add: half] == word[half + 1:][::-1]:
        break
print(L)