import sys

room_num = int(sys.stdin.readline())
candidators = list(map(int, sys.stdin.readline().split()))
main, sub = map(int, sys.stdin.readline().split())

total = 0
for candidator_num in candidators:
    candidator_num -= main
    if candidator_num < 0: 
        candidator_num = 0
    sub_num, remain = int(candidator_num // sub), candidator_num % sub
    if remain > 0:
        sub_num += 1
    total += (sub_num + 1)

print(total)