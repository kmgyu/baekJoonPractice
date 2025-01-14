import sys
input = sys.stdin.readline

slave = 0
professor = 0
mans = []

n = int(input())
room = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(n):
        if room[i][j] == 2:
            slave = (i, j)
        elif room[i][j] == 5:
            professor = (i, j)
        elif room[i][j] == 1:
            mans.append((i, j))

dis = (slave[0]-professor[0])**2 + (slave[1]-professor[1])**2
if dis >= 25:
    cnt = 0
    for man in mans:
        if min(slave[0],professor[0]) <= man[0] <=max(slave[0],professor[0]) and min(slave[1],professor[1]) <= man[1] <=max(slave[1],professor[1]):
            cnt += 1
    if cnt >= 3:
        print(1)
        exit(0)
print(0)


