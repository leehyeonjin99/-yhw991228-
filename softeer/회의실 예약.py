import sys
N, M = map(int, sys.stdin.readline().split())
scheduler = {}
classrooms = []
for _ in range(N):
    classroom = input()
    classrooms.append(classroom)
classrooms.sort()
for classroom in classrooms:
    scheduler[classroom] = []
for _ in range(M):
    classroom, start, end= sys.stdin.readline().split()
    scheduler[classroom].append([int(start), int(end)])
for idx, classroom in enumerate(scheduler):
    scheduler[classroom].sort(key = lambda x : (x[0], x[1]))
    print(f"Room {classroom}:")
    use = []
    not_use = []
    for schedule in scheduler[classroom]:
        if not use:
            use.append(schedule)
        else:
            check = True
            while use[-1][1] > schedule[0]:
                check = False
                use.pop()
            if check:
                use.append(schedule)
    if not use:
        print("1 available:")
        print("09-18")
    else:
        for cnt, schedule in enumerate(use):
            if cnt == 0:
                if schedule[0]>9:
                    not_use.append(f"09-{str(schedule[0]).zfill(2)}")
            if cnt!=0:
                if use[cnt-1][1] != schedule[0]:
                    not_use.append(f"{str(use[cnt-1][1]).zfill(2)}-{str(use[cnt][0]).zfill(2)}")
            if cnt == len(use) - 1:
                if schedule[1]<18:
                    not_use.append(f"{str(schedule[1]).zfill(2)}-18")
        if not_use:
            print(f"{len(not_use)} available:")
            for u in not_use:
                print(u)
        else:
            print("Not available")
    if idx != N-1 :
        print("-"*5)