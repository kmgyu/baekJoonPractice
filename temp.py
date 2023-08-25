import sys
from math import dist
input = sys.stdin.readline

def solve():
    while True:
        cnt = 0
        matrix[15][15] = -1
        for i in range(n):
            x, y = coor[i]
            if x == y == 15:
                cnt += 1
                if cnt == n: return
                continue
            distance = 1e9
            mover = ('', 0, 0)
            for key, value in move.items():
                dx, dy = value
                if x+dx > 30 or x+dx < 0 or y+dy > 30 or y+dy < 0: continue
                if matrix[x+dx][y+dy] != -1:
                    continue
                if (x+dx, y+dy) in middle[i]:continue
                d1 = abs(int(dist((x+dx, y+dy), (15, 15))))
                if d1 < distance:
                    distance = d1
                    mover = (key, dx, dy)
                    if d1 == 0: break
            answer[i].append(mover[0])
            middle[i].add((x+mover[1], y+mover[2]))
            matrix[x+mover[1]][y+mover[2]], matrix[x][y] = matrix[x][y], matrix[x+mover[1]][y+mover[2]]
            # print(*matrix, sep="\n")
            coor[i] = (x+mover[1], y+mover[2])

move = {'A':(-1, 0), 'Q':(-1, 1), 'W':(0, 1),
        'E':(1, 1), 'D':(1, 0), 'C':(1, -1),
        'X':(0, -1), 'Z':(-1, -1)}
n = int(input())
hero = [map(int, input().split()) for _ in range(n)]
matrix = [[-1]*31 for _ in range(31)]
answer = [[] for _ in range(n)]
coor = []
for i in range(n):
    x, y = hero[i]
    matrix[x+15][y+15] = i
    coor.append((x+15, y+15))
middle = [set() for _ in range(n)]
for i in range(n):
    middle[i].add(coor[i])
solve()
for ans in answer:
    print(*ans, sep="")