import sys
fnames = {}
answer = ''
for _ in range(int(sys.stdin.readline())):
    fname = sys.stdin.readline()[0]
    if fname not in fnames:
        fnames[fname] = 1
    elif fnames[fname] < 5:
        fnames[fname] += 1
        if fnames[fname] == 5:
            answer += fname

print(''.join(sorted(answer)) if answer else 'PREDAJA')