import sys

def rotation_side(side, direction):
    cube[side] = list(zip(*cube[side][::-1]))
    if direction == '-':
        for _  in range(2):
            cube[side] = list(zip(*cube[side][::-1]))
    for r_idx in range(3):
        cube[side][r_idx] = list(cube[side][r_idx])


def rotation_neigh(side, direction):
    if side == 'L':
        if direction == '+':
            cube['B'][0][0], cube['U'][0][0], cube['F'][0][0], cube['D'][0][0] = cube['D'][0][0], cube['B'][0][0], cube['U'][0][0], cube['F'][0][0]
            cube['B'][1][0], cube['U'][1][0], cube['F'][1][0], cube['D'][1][0] = cube['D'][1][0], cube['B'][1][0], cube['U'][1][0], cube['F'][1][0]
            cube['B'][2][0], cube['U'][2][0], cube['F'][2][0], cube['D'][2][0] = cube['D'][2][0], cube['B'][2][0], cube['U'][2][0], cube['F'][2][0]
        else:
            cube['B'][0][0], cube['U'][0][0], cube['F'][0][0], cube['D'][0][0] = cube['U'][0][0], cube['F'][0][0], cube['D'][0][0], cube['B'][0][0]
            cube['B'][1][0], cube['U'][1][0], cube['F'][1][0], cube['D'][1][0] = cube['U'][1][0], cube['F'][1][0], cube['D'][1][0], cube['B'][1][0]
            cube['B'][2][0], cube['U'][2][0], cube['F'][2][0], cube['D'][2][0] = cube['U'][2][0], cube['F'][2][0], cube['D'][2][0], cube['B'][2][0]
    if side == 'R':
        if direction == '+':
            cube['B'][0][2], cube['U'][0][2], cube['F'][0][2], cube['D'][0][2] = cube['U'][0][2], cube['F'][0][2], cube['D'][0][2], cube['B'][0][2]
            cube['B'][1][2], cube['U'][1][2], cube['F'][1][2], cube['D'][1][2] = cube['U'][1][2], cube['F'][1][2], cube['D'][1][2], cube['B'][1][2]
            cube['B'][2][2], cube['U'][2][2], cube['F'][2][2], cube['D'][2][2] = cube['U'][2][2], cube['F'][2][2], cube['D'][2][2], cube['B'][2][2]
        else:
            cube['B'][0][2], cube['U'][0][2], cube['F'][0][2], cube['D'][0][2] = cube['D'][0][2], cube['B'][0][2], cube['U'][0][2], cube['F'][0][2]
            cube['B'][1][2], cube['U'][1][2], cube['F'][1][2], cube['D'][1][2] = cube['D'][1][2], cube['B'][1][2], cube['U'][1][2], cube['F'][1][2]
            cube['B'][2][2], cube['U'][2][2], cube['F'][2][2], cube['D'][2][2] = cube['D'][2][2], cube['B'][2][2], cube['U'][2][2], cube['F'][2][2]
    if side == 'U':
        if direction == '+':
            cube['L'][0][2], cube['B'][2][2], cube['R'][2][0], cube['F'][0][0] = cube['F'][0][0], cube['L'][0][2], cube['B'][2][2], cube['R'][2][0]
            cube['L'][1][2], cube['B'][2][1], cube['R'][1][0], cube['F'][0][1] = cube['F'][0][1], cube['L'][1][2], cube['B'][2][1], cube['R'][1][0]
            cube['L'][2][2], cube['B'][2][0], cube['R'][0][0], cube['F'][0][2] = cube['F'][0][2], cube['L'][2][2], cube['B'][2][0], cube['R'][0][0]
        else:
            cube['L'][0][2], cube['B'][2][2], cube['R'][2][0], cube['F'][0][0] = cube['B'][2][2], cube['R'][2][0], cube['F'][0][0], cube['L'][0][2]
            cube['L'][1][2], cube['B'][2][1], cube['R'][1][0], cube['F'][0][1] = cube['B'][2][1], cube['R'][1][0], cube['F'][0][1], cube['L'][1][2]
            cube['L'][2][2], cube['B'][2][0], cube['R'][0][0], cube['F'][0][2] = cube['B'][2][0], cube['R'][0][0], cube['F'][0][2], cube['L'][2][2]
    if side == 'D':
        if direction == '+':
            cube['F'][2][0], cube['R'][2][2], cube['B'][0][2], cube['L'][0][0] = cube['L'][0][0], cube['F'][2][0], cube['R'][2][2], cube['B'][0][2]
            cube['F'][2][1], cube['R'][1][2], cube['B'][0][1], cube['L'][1][0] = cube['L'][1][0], cube['F'][2][1], cube['R'][1][2], cube['B'][0][1]
            cube['F'][2][2], cube['R'][0][2], cube['B'][0][0], cube['L'][2][0] = cube['L'][2][0], cube['F'][2][2], cube['R'][0][2], cube['B'][0][0]
        else:
            cube['F'][2][0], cube['R'][2][2], cube['B'][0][2], cube['L'][0][0] = cube['R'][2][2], cube['B'][0][2], cube['L'][0][0], cube['F'][2][0]
            cube['F'][2][1], cube['R'][1][2], cube['B'][0][1], cube['L'][1][0] = cube['R'][1][2], cube['B'][0][1], cube['L'][1][0], cube['F'][2][1]
            cube['F'][2][2], cube['R'][0][2], cube['B'][0][0], cube['L'][2][0] =cube['R'][0][2], cube['B'][0][0], cube['L'][2][0], cube['F'][2][2]
    if side == 'F':
        if direction == '+':
            cube['U'][2][0], cube['R'][2][0], cube['D'][0][2], cube['L'][2][0] = cube['L'][2][0], cube['U'][2][0], cube['R'][2][0], cube['D'][0][2]
            cube['U'][2][1], cube['R'][2][1], cube['D'][0][1], cube['L'][2][1] = cube['L'][2][1], cube['U'][2][1], cube['R'][2][1], cube['D'][0][1]
            cube['U'][2][2], cube['R'][2][2], cube['D'][0][0], cube['L'][2][2] = cube['L'][2][2], cube['U'][2][2], cube['R'][2][2], cube['D'][0][0]
        else:
            cube['U'][2][0], cube['R'][2][0], cube['D'][0][2], cube['L'][2][0] = cube['R'][2][0], cube['D'][0][2], cube['L'][2][0], cube['U'][2][0]
            cube['U'][2][1], cube['R'][2][1], cube['D'][0][1], cube['L'][2][1] = cube['R'][2][1], cube['D'][0][1], cube['L'][2][1], cube['U'][2][1]
            cube['U'][2][2], cube['R'][2][2], cube['D'][0][0], cube['L'][2][2] = cube['R'][2][2], cube['D'][0][0], cube['L'][2][2], cube['U'][2][2]
    if side == 'B':
        if direction == '+':
            cube['U'][0][2], cube['L'][0][2], cube['D'][2][0], cube['R'][0][2] = cube['R'][0][2], cube['U'][0][2], cube['L'][0][2], cube['D'][2][0]
            cube['U'][0][1], cube['L'][0][1], cube['D'][2][1], cube['R'][0][1] = cube['R'][0][1], cube['U'][0][1], cube['L'][0][1], cube['D'][2][1]
            cube['U'][0][0], cube['L'][0][0], cube['D'][2][2], cube['R'][0][0] = cube['R'][0][0], cube['U'][0][0], cube['L'][0][0], cube['D'][2][2]
        else:
            cube['U'][0][2], cube['L'][0][2], cube['D'][2][0], cube['R'][0][2] = cube['L'][0][2], cube['D'][2][0], cube['R'][0][2], cube['U'][0][2]
            cube['U'][0][1], cube['L'][0][1], cube['D'][2][1], cube['R'][0][1] = cube['L'][0][1], cube['D'][2][1], cube['R'][0][1], cube['U'][0][1]
            cube['U'][0][0], cube['L'][0][0], cube['D'][2][2], cube['R'][0][0] = cube['L'][0][0], cube['D'][2][2], cube['R'][0][0], cube['U'][0][0]

answers = []
test_case = int(sys.stdin.readline())
for _ in range(test_case):
    cube = {'U': [['w', 'w', 'w'] for _ in range(3)],
            'D': [['y', 'y', 'y'] for _ in range(3)],
            'L': [['g', 'g', 'g'] for _ in range(3)],
            'R': [['b', 'b', 'b'] for _ in range(3)],
            'F': [['r', 'r', 'r'] for _ in range(3)],
            'B': [['o', 'o', 'o'] for _ in range(3)]}
    rotation_count = int(sys.stdin.readline())
    side_dir = list(sys.stdin.readline().split())
    for side, dir in side_dir:
        rotation_side(side, dir)
        rotation_neigh(side, dir)
        # print(cube)
    answers.append(cube['U'])

for up in answers:
    for row in up:
        print(*row)     