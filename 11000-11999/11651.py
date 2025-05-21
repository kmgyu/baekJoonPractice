from sys import stdin
input = stdin.readline
t = int(input())
coor = []
for i in range(t):
    coor.append(list(map(int, input().split())))
coor.sort(key=lambda x: x[0])
coor.sort(key=lambda x: x[1])
for i in coor:
    print(*i)