from collections import deque
from sys import stdin
input = stdin.readline
n = int(input())
graph = [[False] * (n+2) for _ in range(n+2)]  # padding
for i in range(n):
    li = list(input())
    for j in range(n):
        if li[j] == '1':
            graph[i+1][j+1] = True

home = []

def dfs(x, y):
    cnt = 0
    if graph[x][y]:
        cnt += 1
        graph[x][y] = False
    else:
        return 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if x == i and y == j:
                continue
            if graph[i][j] and (i == x or j == y):
                cnt += dfs(i, j)
    return cnt

for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j]:
            home.append(dfs(i, j))
home.sort()
print(len(home))
print(*home, sep="\n")

