import sys
N = int(sys.stdin.readline())
score = [0, 0]
one_time = 0
two_time = 0
time = 0
winner = 0
for _ in range(N):
    tnum, t = sys.stdin.readline().split()
    tnum = int(tnum)
    m, s = map(int, t.split(':'))
    t = m * 60 + s
    score[tnum - 1] += 1
    if score[0] == score[1]:
        winner = 0
        if tnum == 1:
            two_time += (t - time)
        else:
            one_time += (t - time)
    if winner == 0 or (winner == 1 and score[0] < score[1]) or (winner == 2 and score[0] > score[1]):
        # print(f"START {tnum} Win at {m, s}")
        time = t
    if score[0] < score[1]:
        winner = 2 
    elif score[0] > score[1]:
        winner = 1
    # print(f"{tnum} / {score} / {m}: {s}, {time}")
if score[0] < score[1]:
    two_time += (48 * 60 - time)
elif score[0] > score[1]:
    one_time += (48 * 60 - time)

print(f"{f'{one_time // 60}'.zfill(2)}:{f'{one_time % 60}'.zfill(2)}")
print(f"{f'{two_time // 60}'.zfill(2)}:{f'{two_time % 60}'.zfill(2)}")

