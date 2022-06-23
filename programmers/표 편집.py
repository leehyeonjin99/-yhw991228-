def solution(n, k, cmd):
    linked_list = {i: [i-1, i+1] for i in range(n)}
    linked_list[0] = [None, 1]
    linked_list[n-1] = [n-2, None]
    situation = ["O" for _ in range(n)]
    recent = []
    for command in cmd:
        command = command.split()
        if command[0] == 'U' or command[0] == 'D':
            for _ in range(int(command[1])):
                k = linked_list[k][0] if command[0] == 'U' else linked_list[k][1]
        if command[0] == 'C':
            situation[k] = 'X'
            prev, next = linked_list[k]
            recent.append([prev, k, next])
            k = prev if next == None else next
            if prev == None:
                linked_list[next][0] = None
            elif next == None:
                linked_list[prev][1] = None
            else:
                linked_list[next][0] = prev
                linked_list[prev][1] = next
        if command[0] == 'Z':
            prev, new, next = recent.pop()
            situation[new] = 'O'
            if prev == None:
                linked_list[next][0] = new
            elif next == None:
                linked_list[prev][1] = new
            else:
                linked_list[next][0] = new
                linked_list[prev][1] = new
    return ''.join(situation)
