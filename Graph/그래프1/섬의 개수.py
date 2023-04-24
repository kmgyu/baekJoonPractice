from collections import deque
from sys import stdin,setrecursionlimit
setrecursionlimit(10**6)
#파이썬은 재귀길이가 정해져있어 의도적으로 늘려줘야한다.
input = stdin.readline

def dfs(x, y):
    if graph[x][y]:
        graph[x][y] = False
    else:
        return 0
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            if x == i and y == j:
                continue
            if graph[i][j]:
                dfs(i, j)
    return 1

while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    graph = [[False] * (w+2) for _ in range(h+2)]  # padding
    for i in range(h):
        li = list(input().split())
        for j in range(w):
            if li[j] == '1':
                graph[i+1][j+1] = True
    cnt = 0
    for i in range(1, h+1):
        for j in range(1, w+1):
            if graph[i][j]:
                cnt += dfs(i,j)
    print(cnt)

